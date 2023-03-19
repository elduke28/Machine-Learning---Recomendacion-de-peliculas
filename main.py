from fastapi import FastAPI
import pandas as pd

#app = FastAPI()
app = FastAPI(title= "API para consultar datos, en plataformas de Streaming",
    description= "Amazon, Disney, Hulu, Netflix")


@app.on_event('startup')
def startup():
    global df; global df_score; global plataformas
    df = pd.read_csv('https://github.com/elduke28/Poyecto-individual/blob/main/Datasets/Plataformas.csv', delimiter=';', low_memory=False)
    df_score = pd.read_csv('https://github.com/elduke28/Poyecto-individual/blob/main/Datasets/score_users.csv', low_memory=False)
    plataformas = ['amazon', 'hulu', 'netflix', 'disney']


# Título de más duración, por plataforma, año y tipo de duración:  
# URL para realizar la consulta /get_max_duration(año,'plataforma','[min o season]')
@app.get('/get_max_duration({year},{platform},{duration_type})')
def get_max_duration(year:int, platform:str, duration_type:str):
    platform = platform.replace("'","")
    platform = platform.lower()
    if platform not in plataformas: return f'Sin datos para la plataforma {platform}' # Verificacion de plataforma
    duration_type = duration_type.replace("'","")
    duration_type = duration_type.lower()
    if duration_type not in ('min','season')  : return 'Se debe especificar el tipo de duración como "min" o "season"'   # Verificación de tipo
    max_duration = df[(df.plataform == platform) & (df.release_year == year) & (df.duration_type == duration_type)]
    if max_duration.shape[0] == 0: return f'Sin datos del año {year}'  # Verificacion de año
    # Retornamos el valor del título
    id_max = max_duration.duration_int.idxmax()
    return f'El título de la plataforma {platform}, del año {year} con mayor duración es: {max_duration.loc[id_max].title.title()}, con una duración de: {max_duration.loc[id_max].duration_int} {duration_type}.'

# Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año. El scored debe ser una numero comprendido entre 1 a 100
@app.get('/get_score_count({platform},{scored},{year})')
async def get_score_count(platform: str, scored: float, year:int):
    platform = platform.replace("'","")
    platform = platform.lower()
    if platform not in plataformas: return f'Sin datos para la plataforma: {platform}'
    if not 1 <= scored <= 100 :  return f'El scored no esta dentro del rango 1 a 100'
    df_add_score = pd.merge(df, df_score, how='inner', on = 'id')
    score_count = df_add_score[(df_add_score.plataform == platform) & (df_add_score.release_year == year) & ((df_add_score.score > scored) )]
    if score_count.shape[0] == 0: return f'Sin datos del año {year}'
    return f'La cantidad de peliculas de la plataforma {platform}, del año {year}, con un scored mayor a {scored} es de: {score_count.id.count()}.'

# Total de películas por plataforma:
# URL para realizar la consulta /get_count_platform('platform')
@app.get('/get_count_platform({platform})')
async def get_count_platform(platform:str):
    platform = platform.replace("'","")
    platform = platform.lower()
    if platform not in plataformas: return f'Sin datos para la plataforma: {platform}'
    count = df[(df.plataform == platform)].id.count()
    return f'La cantidad total de títulos de la plataforma {platform} es de: {count}.'



# Actor con mayor ocurrencias, por plataforma y año:
# URL para realizar la consulta /get_actor('Netflix',2018)
@app.get('/get_actor({platform},{year})')
async def get_actor(platform:str,year:int):
    platform = platform.replace("'","")
    platform = platform.lower()
    if platform not in plataformas: return f'Sin datos para {platform}'
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
    return f'El actor que más se repite en la plataforma {platform}, en el año {year}, es {actores[repeticiones.index(max(repeticiones))].title()}, con un total de {max(repeticiones)} repeticiones.'
