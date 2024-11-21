from fastapi import FastAPI
from typing_extensions import reveal_type

app = FastAPI()

@app.get("/")
async def root():
    return {"message":"hello world"}

items = [
    {"id":1 , "name":"book" , "price":"15" , "stock": True},
    {"id":2 , "name":"game" , "price":"50" , "stock": True},
    {"id":3 , "name":"cd" , "price":"30" , "stock": True},
    {"id":4 , "name":"magazine" , "price":"10" , "stock": False},
    {"id":5 , "name":"book" , "price":"10" , "stock": True},
    {"id":6 , "name":"game" , "price":"10" , "stock": True}
]

@app.get("/items")
async def list_items(
        start : int = 0 ,
        end :int =10,
        id : int = None,
        name: str = None

):
    if id:
        item = next((item for item in items if item["id"]==id),None)
        if item :
            return item
        else:
            return {"message":"item not found"}
    if name:
        filtered=[]
        for item in items :
            if item["name"] == name:
                filtered.append(item)
        return filtered

    return items[start:start+end]

@app.get("/items/prices")
async def sort_price(range : int = None):
    sorted_price = sorted(items , key= lambda x:x["price"] , reverse=True)

    if range:
        price_range = [item for item in sorted_price if item["price"] <= str(range)]

        return price_range
    else:
        return sorted_price

@app.get("/items/stock")
async def get_stock(in_stock:bool = True):
    if not in_stock:
        item = [item for item in items if item["stock"] == False]

        return item
    else:
        item = [item for item in items if item["stock"] == True]
        return item
