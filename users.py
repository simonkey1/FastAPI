from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Entidad usuarios


class User(BaseModel):
    name: str
    surname: str
    url: str
    age: int


@app.get("/usersjson")
async def usersjson():
    return [{"name": "Simon", "surname": "Gómez", "url" : "https://www.google.cl", "age": 25},
            {"name": "Valentina", "surname": "Vargas", "url" : "https://www.google.cl", "age": 23},
            {"name": "Simón", "surname": "Vargas", "url" : "https://www.google.cl","age": 16},
            {"name": "Pía", "surname": "Vargas", "url" : "https://www.google.cl","age": 21},
            {"name": "Manuel", "surname": "Ortiz", "url" : "https://www.google.cl","age": 67}]



@app.get("/usersclass")
async def userclass():
    return User(name='Chita', surname="Gloria", url="https://yahoo.com", age=65)

            

