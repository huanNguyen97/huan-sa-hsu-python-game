# Import from owner
from typing import List
from model.game.game_model_mysql import Game
from database.db_MySQL import SessionLocal
from model.firebase.firebase_Config import db_firebase
from model.cartItem.cart_model_firebase import Cart


# Call db
db = SessionLocal()


class Game_DAO():
    def getAll() -> List[Game]:
        game_list = db.query(Game).all()
        return game_list
    

    def getShoppingCart(username: str):
        name = GameSub_DAO.cutGmail(username) 
        cart_temp = {}          # Gain cart object
        cart_list = []          # Cart total, include total_price and cart_list
        checking_status = 0     # Status for checking
        total_price = 0         # Gain total price
        cart_real_list = []     # Gain only cart in list
        cart_list_firebase = db_firebase.child("Cart_Inside_Temporary").child(name).get()

        try:
            for item in cart_list_firebase.each():
                cart_temp = item.val()
                cart_list.append(cart_temp)
        except:
            checking_status = 1
        
        for item in cart_list:
            if type(item) == float:
                total_price = item
            else:
                cart_real_list.append(item)
        
        if checking_status == 1:
            return 0, [0, 1, 2]
        else:
            return total_price, cart_real_list
    

    def addToCart(cart: Cart):
        user = GameSub_DAO.cutGmail(cart.username) 
        data = {
            "id_game": cart.id_game,
            "name": cart.name,
            "image_url": cart.image_url,
            "quantity": cart.quantity,
            "single_price": cart.single_price,
            "sum_price": cart.sum_price,
            "id_item": cart.id_item
        }
        cart_list_firebase = db_firebase.child("Cart_Inside_Temporary").child(user).get()

        if cart_list_firebase.each() == None:
            data["id_item"] = 1
            db_firebase.child("Cart_Inside_Temporary").child(user).set({"Total_price_temp": cart.sum_price})
            db_firebase.child("Cart_Inside_Temporary").child(user).child("item1").set(data)
        else:
            pre_price = 0
            count = 0
            for item in cart_list_firebase.each():
                if (type(item.val())) == float:
                    pre_price = item.val()
                count += 1
            data["id_item"] = count
            db_firebase.child("Cart_Inside_Temporary").child(user).update({"Total_price_temp": pre_price + cart.sum_price})
            db_firebase.child("Cart_Inside_Temporary").child(user).child("item" + str(count)).set(data)
        
        return 1


    def deleteFromCart(username: str, id_item: int):
        pre_price = 0
        user = GameSub_DAO.cutGmail(username)
        cart_list_firebase = db_firebase.child("Cart_Inside_Temporary").child(user).get() 
        for item in cart_list_firebase.each():
            if (type(item.val())) == float:
                pre_price = item.val()
            elif id_item == item.val()["id_item"]:
                db_firebase.child("Cart_Inside_Temporary").child(user).update({"Total_price_temp": pre_price - item.val()["sum_price"]})
                db_firebase.child("Cart_Inside_Temporary").child(user).child("item" + str(id_item)).remove()
                break
            else:
                pass

        return 1
    

    def createPayment(username: str):
        user = GameSub_DAO.cutGmail(username) 
        total_price, cart_real_list = Game_DAO.getShoppingCart(username)
        payment_list_firebase = db_firebase.child("Payment_History").child(user).get()

        if payment_list_firebase.each() == None:
            count = 0
            id_payment = 1
            Total_price = total_price
            db_firebase.child("Payment_History").child(user).child("payment1").set({"id_payment": id_payment, "Total_price": Total_price})

            for item in cart_real_list:
                count += 1
                db_firebase.child("Payment_History").child(user).child("payment1").child("item" + str(count)).set(item)
        else:
            count_payment = 0
            count_item = 0
            payment_existing = db_firebase.child("Payment_History").child(user).get()
            
            for payment in payment_existing.each():
                count_payment += 1
            id_payment = count_payment + 1
            Total_price = total_price
            db_firebase.child("Payment_History").child(user).child("payment" + str(id_payment)).set({"id_payment": id_payment, "Total_price": Total_price})

            for item in cart_real_list:
                count_item += 1
                db_firebase.child("Payment_History").child(user).child("payment" + str(id_payment)).child("item" + str(count_item)).set(item)
        
        db_firebase.child("Cart_Inside_Temporary").child(user).remove()
        return 1


    def readPayment(username: str):
        user = GameSub_DAO.cutGmail(username)
        list_firebase = db_firebase.child("Payment_History").child(user).get()
        payment_list = []

        if list_firebase.each() == None:
            return 0, [0, 0]
        else:
            for payment in list_firebase.each():
                payment_list.append(payment.val())
            return 1, payment_list

# To make sure main class DAO of game can work, need
# new one class same sub_class to write more conditions
# and main class DAO just have main def()
class GameSub_DAO():
    def cutGmail(username: str):
        name_firebase = username[:-10]
        return name_firebase