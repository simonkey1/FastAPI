from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/usersjson")
async def usersjson():
    return [{"name": "Simon", "surname": "Gómez", "url" : "https://www.google.cl", "age": 25},
            {"name": "Valentina", "surname": "Vargas", "url" : "https://www.google.cl", "age": 23},
            {"name": "Simón", "surname": "Vargas", "url" : "https://www.google.cl","age": 16},
            {"name": "Pía", "surname": "Vargas", "url" : "https://www.google.cl","age": 21},
            {"name": "Manuel", "surname": "Ortiz", "url" : "https://www.google.cl","age": 67}]



# Entidad usuarios

class User():
    name: str
    surname: str
    url: str
    age: int


            

