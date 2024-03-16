from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from models.sales import Sales

templates = Jinja2Templates(directory="templates")
products = APIRouter()

class Product:
    def __init__(self, id, name, price, images):
        self.id = id
        self.name = name
        self.price = price
        self.images = images

@products.get('/', response_class=HTMLResponse)
async def display_products(request: Request):
    products_list = [
        Product(id=1, name="laptop1", price=1000, images=["laptop1.jpg"]),
        Product(id=2, name="laptop2", price=5000, images=["laptop2.jpg"]),
        Product(id=3, name="laptop3", price=3000, images=["laptop3.jpg"]),
        Product(id=4, name="laptop4", price=5000, images=["laptop6.jpg"]),
        Product(id=5, name="laptop5", price=2000, images=["laptop5.jpg"]),
        Product(id=6, name="laptop6", price=15000, images=["laptop6.jpgjpg"]),
        Product(id=7, name="Calculator", price=250, images=["calculator.jpg"]),
        Product(id=8, name="Crosswise", price=20, images=["crosswise.jpg"]),
        Product(id=9, name="Highlighter", price=50, images=["highlighter.jpg"]),
        Product(id=10, name="Scissor", price=30, images=["scissor.jpg"]),
        Product(id=11, name="Glue", price=20, images=["glue.jpg"]),
        Product(id=12, name="Pentel Pen", price=30, images=["pentel_pen.jpg"])
        # Update image paths and add as many images as needed
    ]
    return templates.TemplateResponse("index.html", {"request": request, "products": products_list})

@products.post('/sales/', response_class=HTMLResponse)
async def buy_product(request: Request, sales_data: Sales):
    # Here you would save the sales_data to your database
    # For now, let's just return the received data
    return {"message": "Sale created successfully"}
