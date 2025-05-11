from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm



app = FastAPI()

oauth2 = OAuth2PasswordBearer(tokenUrl="login")



class User(BaseModel):
    username: str
    full_name: str
    email: str
    disabled: bool


class UserDB(User):
    password: str


users_db = {
    "simonskik":{
        "username": "simonskik",
        "full_name": "Simon Gomez",
        "email": "cristobalgomezaraya@gmail.com",
        "disabled": False,
        "password": "123456"
    },
    "Pupi":{
        "username": "pupita",
        "full_name": "Valentina Vargas",
        "email": "valentina.vovargas@gmail.com",
        "disabled": True,
        "password": "654321"
    },
    "PepinoKIller":{
        "username": "PeinoKIller",
        "full_name": "Simon Vargas",
        "email": "simon.goku2006@gmail.com",
        "disabled": False,
        "password": "123456"
    }
}

def search_user(username: str):
    if username in users_db:
        return UserDB(users_db[username])
    

@app.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(status_code=400, detail="el usuario no es correcto")
    
    user = search_user(form.username)
    if not form.password == user.password:
        raise HTTPException(status_code=400, detail="la contrasena no es correcta")

    return {"access_token": 'owo' , "token_type": "bearer"}