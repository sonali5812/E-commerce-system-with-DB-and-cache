from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
import uuid

from app.database import SessionLocal
from app.models import CartItem, DiscountCode, OrderStats
from app.redis_client import redis_client

NTH_ORDER = 2
DISCOUNT_PERCENT = 10

api_ins = FastAPI()

class Item(BaseModel):
    name: str
    qty: int
    price: float

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@api_ins.post("/add")
def add_item(item: Item, db: Session = Depends(get_db)):
    db_item = CartItem(**item.dict())
    db.add(db_item)
    db.commit()
    return {"message": "Item added to cart"}

@api_ins.post("/generate_discount")
def generate_discount(db: Session = Depends(get_db)):
    stats = db.query(OrderStats).first()
    if not stats or stats.total_orders % NTH_ORDER != 0:
        return {"info": "Discount not generated"}

    code = f"OFFER-{uuid.uuid4().hex[:4]}"
    discount = DiscountCode(code=code, percent=DISCOUNT_PERCENT)
    db.add(discount)
    db.commit()

    return {"discount_code": code}

@api_ins.post("/checkout")
def checkout(discount_code=None, db: Session = Depends(get_db)):
    cart_items = db.query(CartItem).all()
    if not cart_items:
        raise HTTPException(status_code=400, detail="cart empty")

    total = sum(i.price * i.qty for i in cart_items)
    item_cnt = sum(i.qty for i in cart_items)

    discount_amt = 0
    if discount_code:
        d = db.query(DiscountCode).filter(
            DiscountCode.code == discount_code,
            DiscountCode.is_used == False
        ).first()

        if not d:
            raise HTTPException(status_code=400, detail="Invalid discount")

        discount_amt = (d.percent / 100) * total
        d.is_used = True

    final_amt = total - discount_amt

    stats = db.query(OrderStats).first()
    if not stats:
        stats = OrderStats(
            total_orders=0,
            total_items_qty=0,
            total_amt=0,
            total_discount=0
        )
        db.add(stats)
        db.flush()  # ensures object is initialized

    stats.total_items_qty += item_cnt
    stats.total_amt += final_amt
    stats.total_discount += discount_amt

    db.query(CartItem).delete()
    db.commit()

    redis_client.delete("admin_data")

    return {"message": "Order placed", "amount": final_amt}

@api_ins.get("/admin_data")
def admin_data(db: Session = Depends(get_db)):
    cached = redis_client.get("admin_data")
    if cached:
        return {"source": "redis", "data": cached}

    stats = db.query(OrderStats).first()
    data = {
        "total_items": stats.total_items_qty if stats else 0,
        "total_amount": stats.total_amt if stats else 0,
        "total_discount": stats.total_discount if stats else 0
    }

    redis_client.setex("admin_data", 60, str(data))
    return {"source": "db", "data": data}









































# from pydantic import BaseModel
# from fastapi import FastAPI, HTTPException
# import uuid


# # maintain cart, orders, discount codes etc
# cart = []
# orders = 0
# discount_codes = []

# # Assume every 2th order we get the discount
# NTH_ORDER = 2
# DISCOUNT_PERCENT = 10

# admin_data = {
#     "total_items_qty": 0,
#     "total_amt": 0,
#     "total_discount": 0,
#     "discount_codes": []
# }

# # Creating a base model so that if invalid input is given it can be handled

# class Item(BaseModel):
#     name : str
#     qty : int
#     price : float

# # Create fastAPI instance
# api_ins = FastAPI()

# # Create methods and APIs for cart and checkout
# # lets assume we are making for 1 user, for multiple users we can maintain a mapping of carts for each user

# @api_ins.post("/add")
# def add_item(item:Item):
#     cart.append(item)
#     return {"message": "Item added in cart", "cart": cart}

# @api_ins.post("/generate_discount")
# def generate_discount():
#     global orders
#     if orders != 0 and orders%NTH_ORDER == 0:

#         # lets assume every discount code starts is in format "OFFER-4cd3"
#         temp = f"OFFER-{uuid.uuid4().hex[:4]}"
#         admin_data["discount_codes"].append(temp)
#         discount_codes.append(temp)
#         return {"dicsount code generated": temp}
#     return {"info": "Discount can not be generated."}

# @api_ins.post("/checkout")
# def checkout(discount_code=None):
#     global orders
#     if len(cart) == 0:
#         raise HTTPException(status_code=400, detail="cart empty")
    
#     total = 0
#     item_cnt = 0
#     for item in cart:
#         total = total + (item.price * item.qty)
#         item_cnt = item_cnt + item.qty
#     if discount_code and discount_code in discount_codes:
#         discount = (DISCOUNT_PERCENT/100)*total
#         discount_codes.remove(discount_code)
#     else:
#         discount = 0

#     final_amt = total-discount

#     # we can further maintain details of orders but for this task we need only count of orders
#     orders += 1

#     # update admin data
#     admin_data["total_items_qty"] += item_cnt
#     admin_data["total_amt"] += final_amt
#     admin_data["total_discount"] += discount

#     cart.clear()
#     return {"message": "Order Completed Successfully.", "order_count":orders, "total_amount":total, "after_discount":final_amt}

# # create a GET API to see admin data
# @api_ins.get("/admin_data")
# def get_admin_data():
#     return {
#         "total items sold" : admin_data["total_items_qty"],
#         "total sold amount" : admin_data["total_amt"],
#         "total discount given" : admin_data["total_discount"],
#         "all discount codes used" : admin_data["discount_codes"]
#     }









