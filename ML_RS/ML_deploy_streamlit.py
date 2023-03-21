import pandas as pd
from surprise import Dataset, Reader, SVD
from surprise.model_selection import train_test_split
import streamlit as st

encabezado = st.container()
ingreso_datos = st.container()
modelo_ml = st.container()
recomendacion = st.container()

# Cargamos los dataset
data_score = pd.read_csv('ML_RS/score_movies_EDA.csv')
data_plat = pd.read_csv('ML_RS/plataformas_EDA.csv', usecols = [0,2], names = ['movieId', 'name'], skiprows=1)

with encabezado:
    st.title('Proyecto de Machine Learning - Sistema de Recomendación')
    st.text('''Este trabajo es un modelo de machine learning, realizado con la libreria
    Surprise,el cual consiste en un sistema de recomendación de películas.''')


with ingreso_datos:

    st.header('Ingreso de datos')

    # Obtenemos los datos del input del usuario
    usuarios = list(data_score.userId.unique())
    user = int(st.text_input('Ingrese el Id del usuario',usuarios[0]))

    if user in usuarios:
        st.success('El Id del usuario ingresado es correcto')
    else:
        st.error('El Id del usuario ingresado no es correcto')

    movies = list(data_plat.movieId.unique())
    movie = st.text_input('Ingrese el Id de la película',movies[0])

    if movie in movies:
        st.success('El Id del título ingresado es correcto')
    else:
        st.error('El Id del título ingresado no es correcto')
with modelo_ml:

    # Cargamos el dataset, para el modelo
    reader = Reader(rating_scale=(1, 5))
    N_filas = 100000 
    data = Dataset.load_from_df(data_score[['userId', 'movieId', 'rating']][:N_filas], reader=reader)

    # Separamos los datos en un set de prueba y otro de entrenamiento del modelo.
    trainset, testset = train_test_split(data, test_size=.25)

    # Aplicamos el modelo de Singular Value Decomposition(SVD)
    modelo = SVD(n_factors=5, n_epochs=20, lr_all=0.002, reg_all=0.002)
    modelo.fit(trainset)
    predictions = modelo.test(testset)


with recomendacion:
    st.header('Recomendación del modelo')

    prediction = modelo.predict(user, movie)

    # Si la predicción es mayor o igual a 3.5, se recomienda la película
    if prediction.est >= 3.5:
        st.write(f"El título {data_plat[data_plat.movieId==movie].name.values[0].title()} es recomendado para el usuario {user}", prediction.est)
    else:
        st.write(f"El título {data_plat[data_plat.movieId==movie].name.values[0].title()} no es recomendado para el usuario {user}", prediction.est)