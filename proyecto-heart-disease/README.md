# Predicción de riesgo cardiovascular a 10 años con Machine Learning

Proyecto final del curso de Machine Learning. Se aborda la **predicción del riesgo de enfermedad
coronaria a 10 años** como un problema de clasificación binaria supervisada y prospectiva, a
partir de 15 atributos de un examen clínico de rutina (demográficos, de hábitos y clínicos, sin
exámenes invasivos ni de esfuerzo), usando el dataset del **Framingham Heart Study** (Kaggle).

## Objetivo

Construir y evaluar modelos que estimen la probabilidad de que una persona sin enfermedad
cardiovascular manifiesta desarrolle enfermedad coronaria en los próximos 10 años, y analizar qué
variables la explican, con especial atención a la calidad de los datos, los sesgos del conjunto y
los riesgos de *data leakage*.

**Por qué este dataset.** El Framingham Heart Study reclutó personas de la comunidad **sin
enfermedad cardiovascular manifiesta** y las siguió durante 10 años, registrando quién
desarrollaba la enfermedad. Todas sus variables se obtienen en un chequeo de rutina — no se
necesitan exámenes invasivos ni de esfuerzo —, lo que encaja directamente con el problema real de
detección temprana y prevención primaria que motiva este proyecto.

**Preguntas de investigación**

1. ¿Qué variables medibles en un chequeo de rutina discriminan mejor el riesgo de enfermedad
   coronaria a 10 años, y son coherentes con los factores de riesgo cardiovascular documentados?
2. ¿Un modelo lineal (regresión logística) alcanza un desempeño comparable al de modelos no
   lineales, o estos aportan una mejora significativa?
3. ¿Cómo afectan el fuerte desbalance de clases (~15 % de casos positivos) y los patrones de
   valores faltantes al desempeño, la calibración de las probabilidades y la equidad del modelo
   entre subgrupos (sexo, nivel educativo)?

## Integrantes

- Luis Cahuana
- <!-- integrante 2 -->
- <!-- integrante 3 -->

## Estado del proyecto

| Entrega | Contenido | Estado |
| --- | --- | --- |
| **P1** (semana 7) | Formulación del problema, descripción del dataset y análisis exploratorio (EDA) | ✅ `notebooks/01-eda.ipynb` |
| **P2** (semana 16) | Preprocesamiento, baseline, comparación de modelos, evaluación y discusión | ⏳ pendiente |

## Estructura del repositorio

```
proyecto-heart-disease/
├── README.md               # este archivo
├── requirements.txt        # dependencias de Python
├── data/
│   ├── framingham.csv      # dataset (4 240 participantes x 16 columnas)
│   └── README.md           # fuente, licencia y diccionario de variables
├── figures/                # figuras generadas por los notebooks (PNG, 200 dpi) para el informe
└── notebooks/
    ├── nb_utils.py         # estilo de gráficos (matplotlib) compartido por los notebooks
    └── 01-eda.ipynb        # P1: problema, dataset, calidad de datos, EDA, sesgo y leakage
```

## Cómo ejecutar

Requiere Python ≥ 3.10.

```sh
python -m venv .venv
# Windows: .venv\Scripts\activate    |    Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt

cd notebooks
jupyter lab          # abrir 01-eda.ipynb y ejecutar todas las celdas
```

Para reproducir el notebook completo desde la terminal (regenera también las figuras en `figures/`):

```sh
cd notebooks
jupyter nbconvert --to notebook --execute --inplace 01-eda.ipynb
```

Los notebooks deben ejecutarse **desde la carpeta `notebooks/`**, porque las rutas a los datos
(`../data/framingham.csv`) y a las figuras (`../figures/`) son relativas a ella.

## Datos

El dataset se incluye en `data/framingham.csv`. Véase [`data/README.md`](data/README.md) para la
fuente original, el diseño del estudio, la licencia (no especificada formalmente por el
redistribuidor de Kaggle) y el diccionario de variables.

## Referencias

- T. R. Dawber, G. F. Meadors y F. E. Moore Jr., "Epidemiological approaches to heart disease:
  the Framingham Study," *American Journal of Public Health*, vol. 41, n.º 3, pp. 279–286, 1951.
- Kaggle, *Framingham Heart Study Dataset*.
  https://www.kaggle.com/datasets/aasheesh200/framingham-heart-study-dataset
- Organización Mundial de la Salud, "Cardiovascular diseases (CVDs) — Fact sheet," 2021.
  https://www.who.int/news-room/fact-sheets/detail/cardiovascular-diseases-(cvds)
