from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from routes import sales

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Mount static files
app.mount("/images", StaticFiles(directory="images"), name="images")

# Include routers
app.include_router(sales.router)

@app.get('/purchase-success', response_class=HTMLResponse)
async def purchase_success():
    with open("purchase_success.html", "r") as file:
        html_content = file.read()
    return html_content

@app.get('/', response_class=HTMLResponse)
async def display_products(request: Request):
    products_list = [
        {"id": 1, "name": "Laptop1", "price": 1000, "images": ["laptop1.jpg"]},
        {"id": 2, "name": "Laptop2", "price": 5000, "images": ["laptop2.jpg"]},
        {"id": 3, "name": "Laptop3", "price": 3000, "images": ["laptop3.jpg"]},
        {"id": 4, "name" : "Laptop4", "price" : 5000, "images" : ["laptop6.jpg"]},
        {"id": 5, "name" : "Laptop5", "price" :2000, "images" :["laptop5.jpg"]},
        {"id": 6, "name" : "Laptop6", "price" : 15000, "images" : ["laptop6.jpg"]},
        {"id": 7, "name" : "Calculator", "price" : 250, "images" : ["calculator.jpg"]},
        {"id": 8, "name" : "Crosswise", "price" : 20, "images" : ["crosswise.jpg"]},
        {"id": 9, "name" : "Highlighter", "price" : 50, "images" : ["highlighter.jpg"]},
        {"id" : 0, "name" : "Scissor", "price" : 30, "images" : ["scissors.jpg"]},
        {"id" : 11, "name" :"Glue", "price" : 20, "images" : ["glue.jpg"]},
        {"id" : 12, "name" :"Pentel Pen", "price" : 30, "images" :["pentel_pen.jpg"]}
    ]
    return templates.TemplateResponse("index.html", {"request": request, "products": products_list})
