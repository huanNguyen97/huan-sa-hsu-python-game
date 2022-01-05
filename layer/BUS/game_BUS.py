# import from python
from typing import List

# Import from owner
from layer.DAO.game_DAO import Game_DAO
from model.game.game_model_mysql import Game
from model.cartItem.cart_model_firebase import Cart


class Game_BUS():
    def getAll() -> List[Game]:
        game_list = Game_DAO.getAll()
        return game_list
    

    def getShoppingCart(username: str):
        total_price, cart_list_temp = Game_DAO.getShoppingCart(username)
        return total_price, cart_list_temp
    
    
    def addToCart(cart: Cart):
        game_status = Game_DAO.addToCart(cart)
        return game_status
    

    def deleteFromCart(username: str, id_item: int):
        game_status = Game_DAO.deleteFromCart(username, id_item)
        return game_status
    

    def createPayment(username: str):
        game_status = Game_DAO.createPayment(username)
        return game_status
    

    def readPayment(username: str):
        game_status, payment_list = Game_DAO.readPayment(username)
        return game_status, payment_list