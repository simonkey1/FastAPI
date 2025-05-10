from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class Product(BaseModel):
    id: int
    name: str
    category: str
    amount: int
    price: int

    

@app.get("/products")
async def products():
    return ["Producto 1", "Producto 2", "Producto 3", "Producto 4", "Producto 5"]