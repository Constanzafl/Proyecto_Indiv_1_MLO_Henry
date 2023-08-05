from fastapi import FastAPI

app = FastAPI(title='Trabajo 1 MLO Henry Constanza Florio', description='Funciones')

@app.get('/')
def index():
    return "Hola mundo"

