import json
import random

# Charger le fichier menu.json
def load_menu(file_path="menu.json"):
    with open(file_path, "r") as file:
        menu = json.load(file)
    return menu

# Générer une commande aléatoire
def generate_random_order(menu, k):
    order = []
    num_items = random.randint(1, k)  # Entre 1 et k items par commande
    for _ in range(num_items):
        # Choisir aléatoirement entre pizza ou boisson
        item_type = random.choice(['pizzas', 'boissons'])
        if item_type in menu:
            # Choisir un item aléatoire parmi les options disponibles
            item = random.choice(menu[item_type])
            order.append(item["nom"])
    return order

# Générer n commandes
def generate_orders(menu, n, k):
    orders = []
    for i in range(1, n + 1):
        order = generate_random_order(menu, k)
        orders.append({"commande_id": i, "items": order})
    return orders

# Sauvegarder les commandes dans un fichier JSON
def save_orders(orders, file_path="commandes.json"):
    with open(file_path, "w") as file:
        json.dump(orders, file, indent=4)

# Main Function
if __name__ == "__main__":
    n = int(input("Entrez le nombre de commandes à générer : "))
    k = int(input("Entrez le nombre maximum d'items par commande : "))

    menu = load_menu("menu.json")
    orders = generate_orders(menu, n, k)
    save_orders(orders, "commandes.json")

    print(f"{n} commandes ont été générées et sauvegardées dans 'commandes.json'.")
