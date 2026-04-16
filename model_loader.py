from models.user import User
from models.menu_item import MenuItem
from models.order import Order
from models.order_item import OrderItem
from models.payment import Payment
from models.review import Review
from models.promo_code import PromoCode
from db import Base, engine

def load_models():
    Base.metadata.create_all(bind=engine)