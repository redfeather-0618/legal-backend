from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# 1. 定義「商品」的資料結構（規定必須有哪些欄位）
class Item(BaseModel):
    name: str          # 名稱，必須是字串
    price: float       # 價格，必須是數字
    is_offer: bool = None  # 是否特價，選填（預設 None）

# 2. 定義一個 POST 路由來接收新增的商品
@app.post("/items/")
def create_item(item: Item):
    # 計算折扣價（邏輯處理）
    discount_price = item.price * 0.9 if item.is_offer else item.price
    
    return {
        "message": "商品新增成功！",
        "item_name": item.name,
        "original_price": item.price,
        "final_price": discount_price
    }
