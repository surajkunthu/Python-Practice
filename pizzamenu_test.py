# Expected output
# Welcome to Julie's Pizzeria
# Our available toppings are:
# Cheese (Free)
# Pepperoni ($1 Extra)

pizza_toppings = ["cheese", "pepperoni"]

def format_topping(topping):
    if topping == "cheese":
        return f"{topping.title()} (Free)"
    else:
        return f"{topping.title()} ($1 Extra)"

def print_menu(toppings):
    print("Welcome to Julie's Pizzeria")
    print("our available toppings are:")
    for topping in pizza_toppings:
        print(format_topping(topping))

print_menu("Cheese")
