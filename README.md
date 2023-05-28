# IAA TP

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

- [Data extraction from Spotify (one genre for test)]('./data_traction_all_genres.ipynb')
- [Data extraction from Spotify (all genres)]('./data_traction_all_genres.ipynb')

## Explanation

WIP

## ToDo:

✅ Hecho, ⚠️ En progreso, ❌ Sin hacer

- ✅ Conseguir playlists dado un género
- ✅ Conseguir tracks a partir de las playlists
- ✅ Conseguir audio features a partir de los tracks
- ⚠️ Limpiar dataframes durante todo el proceso y manipular errores (si surgen)
- ⚠️ Documentar procesos
- ✅ Generar script utils/etl.py con funciones usadas en la notebook (y crear las que falten)
- ✅ Ejecutar funciones de utils/etl.py para generar datasets de audio features para cada género
