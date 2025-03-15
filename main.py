from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return {"message": "¡Hola, mundo!"}

@app.get("/libros/{id}")
def obtener_libro(id: int):
    return {"id": id}