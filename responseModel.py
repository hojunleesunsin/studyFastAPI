from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    email: str
    name: str = None
    age: float

def get_item_from_db(id):
    # 매우 간단한 아이템 반환
    return {
        "email": "hongpc0099@gmail.com", 
        "name": "호준이순신", 
        "age": 27.3,
        "dis_price": 45.0
    }
  
@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int):
    item = get_item_from_db(item_id)
    return item