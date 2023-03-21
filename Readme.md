<h1 align=center> PROYECTO INDIVIDUAL</h1>
<h2 align=center> Machine Learning Operations (MLOps)</h2>

<p align="center"> <img src="img\Devops-vs-Mlops.jpg"  height=250 ></p>
<br>
El presente proyecto, se realizó en la etapa de Labs del bootcamp de Data Science en Henry. El mismo consite en la realización de un sistema de recomendación de películas y series, de distintas plataformas de streaming, asumiendo el rol de MLOPs Engenieer.

<hr>

## Objetivos
En primera instancia, ingestar los datos desde diversos datasets de plataformas de streaming. Sobre los mismos hacer las transformaciones necesarias, unificando el dataset. Mediante `FastApi` desarrollar una API y realizar el deployment de la API en `Render`. Luego obtener el Análisis Exploratorio de Datos (EDA). Finalmente preparar el modelo de machine learning para el sistema de recomendación con la librería `Surprise` y generar un deployment del mismo con la librería `Streamlit`.

:blue_circle: **INICIO** :blue_circle:

* **Datasets**: Bases de datos
* **API**: Aplicación desarrollada en FastAPi. Se encuentra: <br> 
:small_blue_diamond: _main.py_ contiene el codigo de la API, con las consultas requeridas. <br> 
:small_blue_diamond: _requierements.txt_ contiene las dependencias necesarias para el funcionamiento de la API.
* **ETL**: Transformaciones realizadas a los datasets
* **EDA**: Análisis exploratorio de los datos. <br>
:small_blue_diamond: _EDA.ipynb_ cuaderno de notebook, el cual contiene el análisis realizado.<br>
:small_blue_diamond: _.csv_ datasets luego de haber realizado el EDA.
* **ML_RS**: Modelo de machine learning para el sistema de recomenación de películas y series <br> 
:small_blue_diamond: *ML_Surprise.ipynb* cuaderno de notebook, el cual contiene la realización del modelo, con la optimización de sus parámetros.<br>
:small_blue_diamond: *ML_deploy_streamlit.py* contiene el codigo, para el deployment del sistema de recomendación en Streamlit.
<br><br>

## API

Luego de la realización del ETL, se implementó una API mediante el framework `FastAPI` y se realizó el deployment en `Render`. 
<p style = 'text-align:center;'>  <img src="img\Fastapi_render.png" height=100 ></p>

### Consultas

* Película con mayor duración con filtros de AÑO, PLATAFORMA Y TIPO DE DURACIÓN.: [get_max_duration](https://pi-ml-ops-duque.onrender.com/docs#/default/get_max_duration_get_max_duration__year___platform___duration_type___get)


* Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año: [get_score_count](https://pi-ml-ops-duque.onrender.com/docs#/default/get_score_count_get_score_count__platform___scored___year___get)

* Cantidad de películas por plataforma: [get_count_platform](https://pi-ml-ops-duque.onrender.com/docs#/default/get_count_platform_get_count_platform__platform___get)

* Actor que más se repite según plataforma y año.: [get_actor](https://pi-ml-ops-duque.onrender.com/docs#/default/get_actor_get_actor__platform___year___get)
<br><br>

## EDA

En el mismo se visualizaron los valores nulos, se identificaron y eliminaron duplicados, se imputaron valores faltantes y se procedio a la eliminación de columnas irrelevantes.
El analisis exploratorio de datos se realizó con:    
:small_blue_diamond:**pandas:** Se utilizó para visualizar rapidamente los nulos y duplicados de los datasets, además del formato de los mismos.  
:small_blue_diamond:**ydata_profiling:** Se utilizó para obtener un EDA automatizado del dataset.   
:small_blue_diamond:**matplotlib y seaborn:** Se utilizó en conjunto para graficar.
<br><br>

## Sistema de Recomendación

<p style = 'text-align:center;'>  <img src="img\streamlit.jpg" height=100 ></p>

Luego de realizar el EDA, se seleccionó de los atributos relevantes (usuario, movieId, rating) para el modelo de recomendación, implementando la librería `Surprise`.
Se incorporó el framework `Streamlit` para generar una interfase gráfica, y determinar mediante el modelo si un título se recomienda o no a un usuario.
Finalmente desplegué esta aplicación en huggingface para acceder a ella desde internet.

