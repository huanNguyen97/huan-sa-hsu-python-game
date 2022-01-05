# Import from fastapi 
from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware

# Import from owner
from layer.BUS.user_BUS import User_BUS
from model.user.user_model_mysql import User
from layer.BUS.game_BUS import Game_BUS
from model.game.game_model_mysql import Game
from model.cartItem.cart_model_firebase import Cart

# Create app
app = FastAPI()


# Allow origins (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Main app 
# ------------------------------------------------------
# ------------------------------------------------------
# Login
@app.post("/login")
async def login(
    username: str = Form(...),
    password: str = Form(...)
):
    user_input = User(
        username=username,
        password=password
    )
    user_login = User_BUS.login_BUS(user_input)
    return {"user": user_login}


# Register
@app.post("/register")
async def register(
    username: str = Form(...), 
    password: str = Form(...),
    image_url: str = Form(...),
    type_user: str = Form(...)
):
    user = User(
        id=None, 
        username=username,
        password=password,
        image_url=image_url,
        type_user=type_user
    )
    game_status = User_BUS.register_BUS(user)
    return { "status": game_status }


# Read all game 
@app.get("/")
async def getAll():
    game_list = Game_BUS.getAll()
    return { "game_list": game_list }


# Read shopping cart temporary
@app.get("/cart-temp/{username}")
async def getShoppingCart(username: str):
    total_price, cart_list_temp = Game_BUS.getShoppingCart(username)
    return { 
        "total_price": total_price,
        "cart_list_temp": cart_list_temp 
    }


# Add to cart
@app.post("/add-to-cart/{username}")
async def addToCart(
    username: str,
    id_game: str = Form(...),
    name: str = Form(...),
    image_url: str = Form(...),
    single_price: float = Form(...),
    quantity: int = Form(...),
    sum_price: float = Form(...)
):
    id_item = 0
    cart_item = Cart(username, id_game, name, image_url, single_price, quantity, sum_price, id_item)
    game_status = Game_BUS.addToCart(cart_item)
    return {" game_status": game_status}


# Delete item in cart
@app.post("/delete-item/{username}/{id_item}")
async def delete(username: str, id_item: int):
    game_status = Game_BUS.deleteFromCart(username, id_item)
    return { "game_status": game_status }


# Create payment
@app.post("/create-payment/{username}")
async def create_payment(username: str):
    game_status = Game_BUS.createPayment(username)
    return { "game_status": game_status }


# Read payment
@app.get("/read-payment/{username}")
async def read_payment(username: str):
    game_status, payment_list = Game_BUS.readPayment(username)
    return {
        "game_status": game_status,
        "payment_list": payment_list
    }
# ------------------------------------------------------
# ------------------------------------------------------
# End app