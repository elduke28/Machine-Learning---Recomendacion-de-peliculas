""" from fastapi import FastAPI
from sqlalchemy.orm import Session
from database import SessionLocal, engine """

app = FastAPI(title= "API para consultar datos, en plataformas de Streaming",
    description= "Amazon, Disney, Hulu, Netflix")

""" # Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



# Cargamos información sobre el proyecto
@app.get('/')
def index():
    return 'PI_ML_Ops para Henry de Duque de Arce Matias Damian'

# Cargamos información sobre la API
@app.get('/about')
async def about():
    return 'API creada con FastAPI y uvicorn'

@app.get('/')
async def read_data():
    with engine.connect() as conn:
        result = conn.execute(plataforma.select()).fetchall


@app.on_event('startup')
def startup():
    global db_plataforma; global plataformas
    db_plataform = pd.read_csv('Datasets/All_titles.csv')
    plataformas = ['Amazon', 'Hulu', 'Netflix', 'Disney']

 """

#Codigo desde chatGPT

import pymysql.cursors
from fastapi import FastAPI

#app = FastAPI()

# Conectar a la base de datos
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    db='pi_ml_ops',
    cursorclass=pymysql.cursors.DictCursor
)

""" # Modelo de ejemplo
class Item(BaseModel):
    name: str
    price: float
 """
# Ruta para obtener todos los items
@app.get("/items")
async def get_items():
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM items")
        items = cursor.fetchall()
        return items

""" # Ruta para agregar un nuevo item
@app.post("/items")
async def create_item(item: Item):
    with connection.cursor() as cursor:
        sql = "INSERT INTO items (name, price) VALUES (%s, %s)"
        cursor.execute(sql, (item.name, item.price))
        connection.commit()
        return {"message": "Item created"} """
