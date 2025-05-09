from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Entidad usuarios


class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int


users_list = [User(id=1, name='Simon', surname='Gómez', url="htts://www.google.cl", age=25),
         User(id=2, name='Valentina', surname='Vargas', url="htts://www.google.cl", age=23),
         User(id=3, name='Simón', surname='Vargas', url="htts://www.google.cl", age=16),
         User(id=4, name='Pía', surname='Vargas', url="htts://www.google.cl", age=21),
         User(id=4, name='Manuel', surname='Ortiz', url="htts://www.google.cl", age=67)]

@app.get("/usersjson")
async def usersjson():
    return [{"name": "Simon", "surname": "Gómez", "url" : "https://www.google.cl", "age": 25},
            {"name": "Valentina", "surname": "Vargas", "url" : "https://www.google.cl", "age": 23},
            {"name": "Simón", "surname": "Vargas", "url" : "https://www.google.cl","age": 16},
            {"name": "Pía", "surname": "Vargas", "url" : "https://www.google.cl","age": 21},
            {"name": "Manuel", "surname": "Ortiz", "url" : "https://www.google.cl","age": 67}]

    

@app.get("/users")
async def users():
    return users_list


# Path


@app.get("/user/{id}")
async def user(id: int):
    return search_user(id)

# Query

@app.get("/userquery/")
async def user(id: int):
    return search_user(id)

def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error: no se ha encontrado el usuario"}  