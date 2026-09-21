# Datos

## Fuente

**Framingham Heart Study** — el estudio de cohorte cardiovascular más influyente de la historia de
la epidemiología. Comenzó en 1948 en el pueblo de Framingham, Massachusetts (EE. UU.), donde se
reclutaron 5 209 adultos de 28 a 62 años **libres de enfermedad cardiovascular manifiesta** en ese
momento — alrededor de dos tercios de la población adulta del pueblo, captados puerta a puerta, no
a través de un hospital [1]. Fue este estudio el que en los años 60 estableció, con evidencia
longitudinal, que el colesterol, la presión arterial y el tabaquismo son *factores de riesgo* de
enfermedad cardíaca.

El archivo `framingham.csv` de esta carpeta es un subconjunto curado de 4 240 observaciones y 16
columnas, ampliamente utilizado en cursos de ciencia de datos y disponible en Kaggle [2]. El rango
de edad del subconjunto (32–70 años) es ligeramente superior al de la cohorte en su reclutamiento
(28–62), lo que sugiere que corresponde a un examen de seguimiento posterior de los mismos
participantes, no al examen inicial de 1948.

## Diccionario de variables

| Variable | Tipo | Valores / unidad | Descripción |
| --- | --- | --- | --- |
| `male` | binaria | 1 = hombre, 0 = mujer | Sexo |
| `age` | entero | años | Edad en el examen basal |
| `education` | ordinal | 1–4 | Nivel educativo (proxy socioeconómico) |
| `currentSmoker` | binaria | 1 = sí, 0 = no | Fumador activo |
| `cigsPerDay` | numérica | cigarrillos/día | Consumo diario de tabaco (0 si no fuma) |
| `BPMeds` | binaria | 1 = sí, 0 = no | Toma medicación antihipertensiva |
| `prevalentStroke` | binaria | 1 = sí, 0 = no | ACV previo |
| `prevalentHyp` | binaria | 1 = sí, 0 = no | Hipertenso al momento del examen |
| `diabetes` | binaria | 1 = sí, 0 = no | Diabetes diagnosticada |
| `totChol` | numérica | mg/dL | Colesterol total |
| `sysBP` | numérica | mm Hg | Presión arterial sistólica |
| `diaBP` | numérica | mm Hg | Presión arterial diastólica |
| `BMI` | numérica | kg/m² | Índice de masa corporal |
| `heartRate` | numérica | latidos/min | Frecuencia cardíaca en reposo |
| `glucose` | numérica | mg/dL | Glucosa en sangre |
| `TenYearCHD` | binaria | 1 = evento, 0 = sin evento | **Variable objetivo**: ¿desarrolló enfermedad coronaria en los 10 años siguientes al examen? |

Todas las variables predictoras se miden en el mismo examen basal, **antes** de la ventana de
seguimiento de 10 años en la que ocurre (o no) el desenlace — por diseño, no hay variables que
presupongan un examen o una sospecha posterior.

## Problemas de calidad conocidos

Documentados en detalle en `notebooks/01-eda.ipynb`:

- Faltantes reales (no codificados) en 7 columnas, afectando al 13,7 % de las filas: `glucose`
  (9,15 %), `education` (2,48 %), `BPMeds` (1,25 %), `totChol` (1,18 %), `cigsPerDay` (0,68 %),
  `BMI` (0,45 %), `heartRate` (0,02 %). El patrón se acerca más a MAR (asociado a variables
  observadas como el sexo) que a MNAR.
- No hay valores nulos ocultos, duplicados, ni inconsistencias internas (`diaBP` nunca supera a
  `sysBP`; el estatus de fumador es siempre coherente con `cigsPerDay`).
- Fuerte desbalance de clases: 15,19 % de casos positivos (`TenYearCHD = 1`).
- La cohorte es predominantemente blanca y de una única localidad de Nueva Inglaterra; la
  literatura documenta que el score de riesgo derivado de Framingham calibra mal en poblaciones
  no blancas [3][4].

## Referencias

[1] T. R. Dawber, G. F. Meadors y F. E. Moore Jr., "Epidemiological approaches to heart disease:
the Framingham Study," *American Journal of Public Health*, vol. 41, n.º 3, pp. 279–286, 1951.

[2] Kaggle, *Framingham Heart Study Dataset*.
https://www.kaggle.com/datasets/aasheesh200/framingham-heart-study-dataset

[3] D. Gaziano *et al.*, "Prediction of cardiovascular death in racial/ethnic minorities using
Framingham risk factors," *Circulation: Cardiovascular Quality and Outcomes*, 2009.

[4] "The Role of Race in Cardiovascular Disease Risk Prediction," *PMC*, 2024.
