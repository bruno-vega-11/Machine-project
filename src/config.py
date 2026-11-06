"""Rutas, grupos de variables y etiquetas compartidas por los notebooks del proyecto.

Las rutas se resuelven a partir de la ubicación de este archivo, así que no dependen
del directorio desde el que se ejecute el notebook.
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "framingham.csv"
FIG_DIR = ROOT / "results" / "figures"

SEED = 42

TARGET = "TenYearCHD"
NUM = ["age", "totChol", "sysBP", "diaBP", "BMI", "heartRate", "glucose", "cigsPerDay"]
BIN = ["male", "currentSmoker", "BPMeds", "prevalentStroke", "prevalentHyp", "diabetes"]
ORD = ["education"]

ETIQUETAS = {
    "age": "edad (años)",
    "totChol": "colesterol total (mg/dL)",
    "sysBP": "presión sistólica (mm Hg)",
    "diaBP": "presión diastólica (mm Hg)",
    "BMI": "índice de masa corporal (kg/m²)",
    "heartRate": "frecuencia cardíaca en reposo (lpm)",
    "glucose": "glucosa (mg/dL)",
    "cigsPerDay": "cigarrillos por día",
    "male": "sexo (1 = hombre)",
    "currentSmoker": "fumador activo",
    "BPMeds": "medicación antihipertensiva",
    "prevalentStroke": "ACV previo",
    "prevalentHyp": "hipertensión previa",
    "diabetes": "diabetes",
    "education": "nivel educativo (1-4)",
    "TenYearCHD": "enfermedad coronaria a 10 años",
}

# color de la clase 0 (sin evento) y de la clase 1 (con evento)
C0, C1 = "#0072B2", "#D55E00"
