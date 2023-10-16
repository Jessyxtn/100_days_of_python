

WATER = 2000
MILK = 200
COFFEE = 1000
ESPRESSO = 2.90
LATTE = 3.50
CAPPUCINO = 4.40

def report(ingredients):
    print(f"Water: {ingredients['water']}ml")
    print(f"Milk: {ingredients['milk']}ml")
    print(f"Coffee: {ingredients['coffee']}g")
    return ingredients

def coffee():
    print("Please insert coins.")
    two_dollars = input("How many $2 coins? ")
    one_dollars = input("How many $1 coins? ")
    fifty_cents = input("How many $0.50 coins? ")
    twenty_cents = input("How many $0.20 coins? ")

    total = (int(two_dollars) * 2) + (int(one_dollars) * 1)
    total += (int(fifty_cents) * 0.5) + (int(twenty_cents) * 0.2)

    return total

def espresso(ingredients):

    if ingredients["water"] < 50:
        print("Insufficient water.")
        return ingredients
    elif ingredients["coffee"] < 20:
        print("Insufficient coffee.")
        return ingredients

    money = coffee()
    if money < ESPRESSO:
        print("Insufficient fund. Money refunded.")
        return ingredients

    money -= ESPRESSO
    ingredients["water"] -= 50
    ingredients["coffee"] -= 20

    print(f"Here is ${money:.2f} change.")
    print("Enjoy your coffee! <3")

    return ingredients

def latte(ingredients):

    if ingredients["water"] < 200:
        print("Insufficient water.")
        return ingredients
    elif ingredients["milk"] < 200:
        print("Insufficient milk.")
        return ingredients
    elif ingredients["coffee"] < 10:
        print("Insufficient coffee.")
        return ingredients

    money = coffee()
    if money < LATTE:
        print("Insufficient fund. Money refunded.")
        return ingredients

    money -= LATTE
    ingredients["water"] -= 200
    ingredients["milk"] -= 200
    ingredients["coffee"] -= 10

    print(f"Here is ${money:.2f} change.")
    print("Enjoy your coffee! <3")

    return ingredients

def cappucino(ingredients):

    if ingredients["water"] < 200:
        print("Insufficient water.")
        return ingredients
    elif ingredients["milk"] < 100:
        print("Insufficient milk.")
        return ingredients
    elif ingredients["coffee"] < 10:
        print("Insufficient coffee.")
        return ingredients

    money = coffee()
    if money < CAPPUCINO:
        print("Insufficient fund. Money refunded.")
        return ingredients

    money -= CAPPUCINO
    ingredients["water"] -= 200
    ingredients["milk"] -= 100
    ingredients["coffee"] -= 10

    print(f"Here is ${money:.2f} change.")
    print("Enjoy your coffee! <3")

    return ingredients
    

if __name__ == "__main__":
    
    ingredients = {
        "water" : WATER,
        "milk" : MILK, 
        "coffee" : COFFEE
    }
    
    functions = {
        "report" : report, 
        "espresso" : espresso,
        "cappucino" : cappucino, 
        "latte" : latte
    }

    while True:
        request = input("What would you like? (espresso/latte/cappucino) ").lower()
        if request in functions:
            ingredients = functions[request](ingredients)
        else:
            break
        

