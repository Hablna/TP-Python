import json

with open("menu.json", "r") as fp:
    Ingredients = json.load(fp)

class Ingredient:
    def __init__(self, name: str):
        self.name = name

class Pizza:
    def __init__(self, name:str, size:float, price: float):
        self.name = name
        self.size = size
        self.price = price

        #une methode add_ingredient qui permet d'ajouter un ingredient à la pizza
    def add_ingredient(self, ingredient):
        self.ingredient = ingredient
        return self.ingredient

class Drink:
    def __init__(self, name:str, volume: float, price: float):
        self.name = name
        self.volume = volume
        self.price = price

class Order:
    def __init__(self, order_id: int, products: str):
        self.order_id = order_id
        self.products = products
    def add_product(self, product):
        self.product = product
        return self.product
    def total(self):
        pass

with open("commandes.json","r") as fp:
    Commandes = json.load(fp)
#print(Ingredient["boissons"])

