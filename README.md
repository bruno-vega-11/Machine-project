# Predicción de riesgo coronario a 10 años con Machine Learning

Proyecto del curso de Machine Learning, basado en el dataset del **Framingham Heart Study**.

## Problema

Las enfermedades cardiovasculares son la primera causa de muerte en el mundo. La forma más
efectiva de reducirlas es **identificar a personas sanas con alto riesgo futuro** para intervenir a
tiempo (cambios de hábitos, control de presión o colesterol), antes de que ocurra un evento.

El riesgo depende de muchos factores a la vez (edad, presión arterial, glucosa, tabaquismo, entre
otros) y ninguno por separado basta para anticiparlo. Por eso se usa Machine Learning: para
aprender de los datos cómo combinar esos factores y estimar el riesgo de cada persona.

## Objetivo

Estimar la probabilidad de que una persona desarrolle enfermedad coronaria en los 10 años
siguientes a partir de los datos de un chequeo de rutina, e identificar qué variables explican ese
riesgo.

## Integrantes

- Valeria Valentina Ríos Gómez
- Luis Enrique Cahuana García
- Bruno Gonzalo Vega Napan
- Nicolas Valentino Días Flores

## Estructura del repositorio

```
proyecto-heart-disease/
├── README.md
├── requirements.txt       # dependencias de Python
├── .gitignore
├── data/
│   ├── README.md          # fuente, licencia y diccionario de variables
│   └── framingham.csv     # dataset (4 240 filas x 16 columnas)
├── notebooks/
│   ├── 01-eda.ipynb       # análisis exploratorio de datos
│   └── 02-modelo.ipynb    # preprocesamiento, modelos, evaluación, interpretación y equidad
├── src/
│   ├── __init__.py
│   ├── config.py          # rutas, grupos de variables, etiquetas y colores
│   ├── plotting.py        # estilo de gráficos y guardado de figuras
│   └── preprocessing.py   # presión de pulso, imputación de faltantes y escalado (pipeline del proyecto)
└── results/
    ├── figures/           # figuras generadas por los notebooks
    └── tables/            # métricas y tablas de resultados (CSV) usadas en el informe
```

Los notebooks se ejecutan en orden: `01-eda.ipynb` y luego `02-modelo.ipynb`. El segundo tarda unos
3 minutos (la búsqueda de hiperparámetros del Random Forest es la parte más lenta).

## Cómo ejecutar

Requiere Python 3.10 o superior.

1. Clonar el repositorio y crear un entorno virtual:

   ```sh
   git clone <url-del-repositorio>
   cd proyecto-heart-disease
   python -m venv .venv
   ```

2. Activar el entorno e instalar las dependencias:

   ```sh
   # Windows
   .venv\Scripts\activate
   # Linux / macOS
   source .venv/bin/activate

   pip install -r requirements.txt
   ```

3. Abrir y ejecutar los notebooks, en orden:

   ```sh
   jupyter lab notebooks/01-eda.ipynb
   jupyter lab notebooks/02-modelo.ipynb
   ```

   O ejecutarlos completos desde la terminal, lo que también regenera las figuras de
   `results/figures/` y las tablas de `results/tables/`:

   ```sh
   jupyter nbconvert --to notebook --execute --inplace notebooks/01-eda.ipynb
   jupyter nbconvert --to notebook --execute --inplace notebooks/02-modelo.ipynb
   ```

   Todos los resultados son reproducibles: el *split*, la validación cruzada y los modelos usan la
   semilla fija `SEED = 42` de `src/config.py`.
