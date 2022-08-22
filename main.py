from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from redis_om import get_redis_connection,HashModel
app= FastAPI()


origins=[
    'http://localhost:3000'
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

redis=get_redis_connection(
    host="redis-15336.c1.asia-northeast1-1.gce.cloud.redislabs.com",
    port=15336,
    password="VXEjnnYFZMxqY89pBu0LLO8joPJxpvNx",
    decode_responses=True

)

class Product(HashModel):
    name:str
    price:float
    quantity:int
    class Meta:
        database=redis


@app.post('/product')
def create(product:Product):
    return product.save()

@app.post('/product/{pk}')
def gets(pk:str):
    return Product.get()
