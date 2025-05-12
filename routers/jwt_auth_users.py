from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta

app = FastAPI()

oauth2 = OAuth2PasswordBearer(tokenUrl="login")


ALGORITHM = "HS256"
ACCESS_TOKEN_DURATION = 1

crypt = CryptContext(schemes=["bcrypt"])



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
        "password": "$2a$12$VEs1Y7qVWiyv25qlopAFIefvNHwIwkfi2U5ptsI41/sd3jU9NxIeW"
    },
    "pupita":{
        "username": "pupita",
        "full_name": "Valentina Vargas",
        "email": "valentina.vovargas@gmail.com",
        "disabled": True,
        "password": "$2a$12$RI4Pmdz.ffnYIEvs3A0mNeS6.jZy0YpdnaFrPLrIb0V7dAK3dWRaO"
    },
    "PepinoKIller":{
        "username": "PeinoKIller",
        "full_name": "Simon Vargas",
        "email": "simon.goku2006@gmail.com",
        "disabled": False,
        "password": "$2a$12$MMB.K0csfMx5objLUtLIEubRYszxYH8gsR3HarmjG3FtMJH2kdR4W"
    }
}



def search_user_db(username: str):
    if username in users_db:
        return UserDB(**users_db[username])
    

@app.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="el usuario no es correcto")
    
    user = search_user_db(form.username)


    

    if not crypt.verify(form.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="la contrasena no es correcta")

    access_token_expiration = timedelta(minutes = ACCESS_TOKEN_DURATION)

    return {"access_token": user.username , "token_type": "bearer"}
