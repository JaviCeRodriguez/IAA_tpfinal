# IAA TP

![data lake carpincho](assets/carpincho.jpg)

## How to install project

```shell
>> git clone https://github.com/JaviCeRodriguez/IAA_tpfinal.git
>> cd ./IAA_tpfinal
>> python3 -m virtualenv venv
>> venv/Scripts/activate # or source venv/bin/activate
(venv) >> pip install -r requirements.txt
```

Create `.env` file and put same keys from `.env.example` with his values (or get credentials from [Web API Dashboard](https://developer.spotify.com/dashboard) of Spotify)

## Notebooks

| Título | Ver notebook en colab |
|:-------|:----------------------|
| [Prediction genres (ETL + EDA + Model)](prediction_genres.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JaviCeRodriguez/IAA_tpfinal/blob/main/prediction_genres.ipynb) |
| [ETL for extract genres by playlist](spotify_get_playlist_test.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JaviCeRodriguez/IAA_tpfinal/blob/main/spotify_get_playlist_test.ipynb) |

## Explanation

View PDF document about this proyect: `TP IAA - Géneros de canciones en Spotify.pdf`

## ToDo:

✅ Hecho, ⚠️ En progreso, ❌ Sin hacer

#### ETL

- ✅ Conseguir playlists dado un género
- ✅ Conseguir tracks a partir de las playlists
- ✅ Conseguir audio features a partir de los tracks
- ✅ Limpiar dataframes durante todo el proceso y manipular errores (si surgen)
- ✅ Documentar procesos
- ✅ Generar script utils/etl.py con funciones usadas en la notebook (y crear las que falten)
- ✅ Ejecutar funciones de utils/etl.py para generar datasets de audio features para cada género

#### Preprocessing (pre EDA)

- ✅ Explorar dataframe
- ✅ Analizar y hacer decisiones sobre tracks con duplicados de géneros y/o con más de uno distintos
- ✅ Generar dataset preprocesado

#### EDA

- ✅ Realizar análisis en géneros seleccionados y obtener estadísticas básicas
- ✅ Analizar si hay ciertos patrones en las audio features
- ✅ Chequear posibles correlaciones
- ✅ Generar un reporte mediante gráficos

#### Model trainning

- ✅ Evaluar modelos de clasificación
- ✅ Implementación de modelos teniendo en cuenta los criterios definidos en el EDA
- ✅ Obtener métricas de cada modelo y elegir el mejor
- ✅ Predecir géneros a partir del modelo elegido
- ✅ Generar reporte (diapositiva)