




#List of menu items
menu_items = [
    'Café',
    'Tarta',
    'Helado',
    'Waffle',
    'Bebida',
    'Rollo de Canela',
    'Sándwich Carne Mechada',
    'Churrasco'
]
# Dictionary of stock values for each item
stock = {
    'Café' : 50,
    'Tarta' : 6,
    'Helado' : 100,
    'Waffle' : 30,
    'Bebida' : 30,
    'Rollo de Canela': 4,
    'Sándwich Carne Mechada': 6,
    'Churrasco': 15
}
# Dictionary of prices for each item
prices = {
    'Café' : 1900,
    'Tarta': 3000,
    'Helado': 3500,
    'Waffle': 3600,
    'Bebida': 1000,
    'Rollo de Canela': 2500,
    'Sándwich Carne Mechada': 5150,
    'Churrasco': 3500
}

# Variable to store the total value of each item
item_values = {item: stock[item] * prices[item] for item in menu_items}

# Variable to store the value of all stock combined
total_stock_worth = sum(item_values.values())

# Prints the menu, item and prices per unit
print("Menú:\n")
for item in menu_items:
    print(f"{item}: ${prices[item]:} CLP c/u")

# Prints the item and amount of stock
print("\nExistencias de Artículos: ")
for item in stock:
    print(f"{item}: {stock[item]}")

# Prints the total value of the stock for each item
print("\nValores Totales de Artículos:")
for item in menu_items:
    print(f"{item}: ${item_values[item]} CLP")

# Prints the total value 
print("\nValor Total: ${:}".format(total_stock_worth),"CLP")

