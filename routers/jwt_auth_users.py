from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta

router = APIRouter()

oauth2 = OAuth2PasswordBearer(tokenUrl="login")


ALGORITHM = "HS256"
ACCESS_TOKEN_DURATION = 15
SECRET = "1db75359a1eb0ff751ac9045f34c7151d4ecf059ef21eff85f5a8afd78320973" 

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
        "username": "PepinoKIller",
        "full_name": "Simon Vargas",
        "email": "simon.goku2006@gmail.com",
        "disabled": False,
        "password": "$2a$12$MMB.K0csfMx5objLUtLIEubRYszxYH8gsR3HarmjG3FtMJH2kdR4W"
    }
}



def search_user(username: str):
    if username in users_db:
        return User(**users_db[username])

def search_user_db(username: str):
    if username in users_db:
        return UserDB(**users_db[username])
    

async def auth_user(token=Depends(oauth2)):

    exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Credenciales de autentificacion invalidas.",
        headers={"WWW-Authenticate": "Bearer"}
    )

    try:
        payload = jwt.decode(token, SECRET, algorithms=ALGORITHM)
        username = payload.get("sub")
        if username is None:
            raise exception
    except JWTError:
        raise exception

    user = search_user(username)
    if user is None:
        raise exception

    return user
        

async def  current_user(user: User = Depends(auth_user)):
    if user.disabled:
        raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, 
                detail="Credenciales de autentificacion invalidas.", 
                headers={"WWW-Authenticate": "Bearer"})
    return user

@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="el usuario no es correcto")
    
    user = search_user_db(form.username)

    if not crypt.verify(form.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="la contrasena no es correcta")


    access_token = {
            "sub": user.username,
            "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_DURATION),
            "iat": datetime.utcnow()  # opcional, issued at
}

    return {"access_token": jwt.encode(access_token, SECRET, algorithm=ALGORITHM) , "token_type": "bearer"}

@router.get('/users/me')
async def me(user: User = Depends(current_user)):
    return user


