from fastapi import FastAPI
from model_loader import load_models
from routers import user, menu_item, order, order_item, payment, review, promo_code

app = FastAPI(title="DAN Restaurant API")

load_models()

app.include_router(user.router)
app.include_router(menu_item.router)
app.include_router(order.router)
app.include_router(order_item.router)
app.include_router(payment.router)
app.include_router(review.router)
app.include_router(promo_code.router)

@app.get("/")
def root():
    return {"message": "Restaurant API is running!"}