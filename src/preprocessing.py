"""Preprocesamiento compartido por los notebooks de modelado.

Implementa las decisiones descritas en el informe (sección "Preprocesamiento e
Ingeniería de Características"):

1. ``AnadirPresionPulso``: crea ``pulsePressure = sysBP - diaBP``.
2. ``ImputarFaltantes``: mediana por sexo para ``glucose``, ``totChol`` y ``BMI``;
   ``cigsPerDay`` = 0 si no fuma y mediana de los fumadores si fuma; moda para
   ``education`` y ``BPMeds``; mediana global para ``heartRate``.
3. ``RobustScaler`` para las numéricas continuas; binarias y ``education`` sin cambios.

Todo lo que aprende de los datos (medianas, modas, escalas) se guarda en ``fit``. Al
usarse dentro de un ``Pipeline``, se ajusta solo con las filas de entrenamiento de cada
partición, así que no hay fuga de información hacia validación o prueba.
"""

from __future__ import annotations

import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import RobustScaler

from src.config import BIN, NUM, ORD


class AnadirPresionPulso(BaseEstimator, TransformerMixin):
    """Agrega la presión de pulso, ``pulsePressure = sysBP - diaBP``.

    No aprende nada de los datos: es una resta fila por fila.
    """

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = X.copy()
        X["pulsePressure"] = X["sysBP"] - X["diaBP"]
        return X


class ImputarFaltantes(BaseEstimator, TransformerMixin):
    """Imputa los faltantes con estadísticos aprendidos solo en ``fit``.

    - ``cols_por_sexo``: mediana del mismo sexo (``male``); mediana global como respaldo.
      Con ``por_sexo=False`` se usa directamente la mediana global (para comparar).
    - ``cigsPerDay``: 0 si ``currentSmoker == 0``; mediana de los fumadores si fuma.
    - ``cols_moda``: valor más frecuente (siempre una categoría válida).
    - ``cols_global``: mediana global.
    """

    def __init__(self, cols_por_sexo=("glucose", "totChol", "BMI"),
                 cols_moda=("education", "BPMeds"), cols_global=("heartRate",),
                 por_sexo=True):
        self.cols_por_sexo = cols_por_sexo
        self.cols_moda = cols_moda
        self.cols_global = cols_global
        self.por_sexo = por_sexo

    def fit(self, X, y=None):
        self.med_sexo_ = {c: X.groupby("male")[c].median().to_dict() for c in self.cols_por_sexo}
        self.med_global_ = {c: float(X[c].median()) for c in (*self.cols_por_sexo, *self.cols_global)}
        self.moda_ = {c: X[c].mode().iloc[0] for c in self.cols_moda}
        self.cigs_fumador_ = float(X.loc[X["currentSmoker"] == 1, "cigsPerDay"].median())
        return self

    def transform(self, X):
        X = X.copy()
        for c in self.cols_por_sexo:
            if self.por_sexo:
                X[c] = X[c].fillna(X["male"].map(self.med_sexo_[c]))
            X[c] = X[c].fillna(self.med_global_[c])
        falta = X["cigsPerDay"].isna()
        X.loc[falta & (X["currentSmoker"] == 0), "cigsPerDay"] = 0
        X.loc[falta & (X["currentSmoker"] == 1), "cigsPerDay"] = self.cigs_fumador_
        for c in self.cols_global:
            X[c] = X[c].fillna(self.med_global_[c])
        for c in self.cols_moda:
            X[c] = X[c].fillna(self.moda_[c])
        return X


def build_preprocessor(pulse_pressure: bool = True, imputar_por_sexo: bool = True) -> Pipeline:
    """Construye el preprocesamiento del proyecto: (presión de pulso) -> imputación -> escalado.

    Los parámetros permiten las comparaciones del notebook: con o sin ``pulsePressure``,
    e imputación por sexo frente a mediana global.
    """
    num = NUM + (["pulsePressure"] if pulse_pressure else [])
    escalado = ColumnTransformer(
        [("num", RobustScaler(), num), ("pasan", "passthrough", BIN + ORD)],
        verbose_feature_names_out=False,
    ).set_output(transform="pandas")
    pasos = [("pulso", AnadirPresionPulso())] if pulse_pressure else []
    pasos += [("imputar", ImputarFaltantes(por_sexo=imputar_por_sexo)), ("escalar", escalado)]
    return Pipeline(pasos)
