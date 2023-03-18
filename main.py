import pymysql.cursors
from fastapi import FastAPI
import pandas as pd

#app = FastAPI()
app = FastAPI(title= "API para consultar datos, en plataformas de Streaming",
    description= "Amazon, Disney, Hulu, Netflix")


# Conectar a la base de datos
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    db='pi_ml_ops',
    cursorclass=pymysql.cursors.DictCursor
)

@app.on_event('startup')
def startup():
    global plataformas
    plataformas = ['amazon', 'hulu', 'netflix', 'disney']

@app.get("/menu")
def menu():
    return ("Funciones de mi API: (1) get_max_duration() (2) get_score_count() (3) get_count_platform (4) get_actor")

# Título de más duración, por plataforma y por año:  
# URL para realizar la consulta /get_max_duration(año,'plataforma','[min o season]')
@app.get('/get_max_duration({year},{platform},{duration_type})')
def get_max_duration(year:int, platform:str, duration_type:str):
    platform = platform.replace("'","")
    platform = platform.lower()
    if platform not in plataformas: return f'Sin datos para la plataforma {platform}' # Verificacion de plataforma
    duration_type = duration_type.replace("'","")
    duration_type = duration_type.lower()
    if duration_type not in ('min','season')  : return 'Se debe especificar el tipo de duración como "min" o "season"'   # Verificación de tipo
    with connection.cursor() as cursor:
        cursor.execute('''SELECT * FROM plataforma where release_year=(%s) and plataform=(%s) and duration_type=(%s) 
                        order by duration_int desc limit 1''',(year,platform,duration_type))
        Max_duration = cursor.fetchall()
        Max_duration = Max_duration[0]
    return f'El título de la plataforma {platform}, del año {year} con mayor duración es: {Max_duration["title"].title()}, con una duración de: {Max_duration["duration_int"]} {duration_type}'
 #agregas los otros datos

# Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año. El scored debe ser una numero comprendido entre 1 a 100
@app.get("/get_score_count({platform},{scored},{year})")
async def get_score_count(platform: str, scored: float, year:int):
    platform = platform.replace("'","")
    platform = platform.lower()
    if platform not in plataformas: return f'Sin datos para la plataforma: {platform}'
    if not 1 <= scored <= 100 :  return f'El scored no esta dentro del rango 1 a 100'
    with connection.cursor() as cursor:
        cursor.execute('''select count(id) cantidad from plataforma p join score_usuarios s on (s.movie_id=p.id) 
                        where p.plataform = (%s) and p.release_year = (%s) and s.score > (%s)''',(platform,year,scored))
        Total_movies = cursor.fetchall()
    if Total_movies[0]["cantidad"] == 0: return f'Sin datos para el año {year}'
    return f'La cantidad de peliculas de la plataforma {platform}, del año {year}, con un scored mayor a {scored} es de: {Total_movies[0]["cantidad"]}'

# Total de películas, por plataforma:
# URL para realizar la consulta /get_count_platform('platform')
@app.get('/get_count_platform({platform})')
async def get_count_platform(platform:str):
    platform = platform.replace("'","")
    platform = platform.lower()
    if platform not in plataformas: return f'Sin datos para la plataforma: {platform}'
    with connection.cursor() as cursor:
        cursor.execute('SELECT count(*) cantidad FROM plataforma where plataform = (%s)',(platform) )
        Total_movies = cursor.fetchall()
    return f'La cantidad total de peliculas de la plataforma {platform} es de: {Total_movies[0]["cantidad"]}'



# Actor con mayor ocurrencias, por plataforma y por año:
# URL para realizar la consulta /get_actor('Netflix',2018)
@app.get('/get_actor({platform},{year})')
async def get_actor(platform:str,year:int):
    platform = platform.replace("'","")
    platform = platform.lower()
    if platform not in plataformas: return f'Sin datos para {platform}'
    with connection.cursor() as cursor:
        cursor.execute("select * from plataforma")
        Total_movies = cursor.fetchall() 
    df = pd.DataFrame(Total_movies)
    actores, repeticiones = list(), list()  
    cast_list = list(df[(df.plataform == platform) & (df.release_year == year)].cast.fillna('Sin_dato'))
    for each in cast_list:  
        if not(each == 'Sin_dato'):    
            lista = each.split(",")
            for elem in lista: 
                elem = elem.strip()
                if elem in actores: 
                    repeticiones[actores.index(elem)] += 1
                else:    
                    actores.append(elem)
                    repeticiones.append(1)
    if actores == []: return f'Sin datos para el año {year}' 
    return f'El actor que más se repite en la plataforma {platform}, en el año {year}, es {actores[repeticiones.index(max(repeticiones))].title()}, con un total de {max(repeticiones)} repeticiones'