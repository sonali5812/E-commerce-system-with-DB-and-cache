from sqlalchemy import Column, Integer, String, Float, Boolean
from app.database import Base

class CartItem(Base):
    __tablename__ = "cart"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    qty = Column(Integer)
    price = Column(Float)

class DiscountCode(Base):
    __tablename__ = "discount_codes"

    id = Column(Integer, primary_key=True)
    code = Column(String, unique=True)
    percent = Column(Float)
    is_used = Column(Boolean, default=False)

class OrderStats(Base):
    __tablename__ = "order_stats"

    id = Column(Integer, primary_key=True)
    total_orders = Column(Integer, default=0)
    total_items_qty = Column(Integer, default=0)
    total_amt = Column(Float, default=0)
    total_discount = Column(Float, default=0)
