MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

pera = {
    "money": 0,
}

show = False
successful = False
def data(dec):
    if successful == True:
        show = f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}"
        return show
    else:
        water1 = resources['water']
        milk1 = resources['milk']
        coffee1 = resources['coffee']
        if dec == "espresso":
            water1 = water1 - 50
            milk1 = milk1 - 0
            coffee1 = coffee1 - 18
            resources.update(water=water1)
            resources.update(milk=milk1)
            resources.update(coffee=coffee1)
        elif dec == "latte":
            water1 = water1 - 200
            milk1 = milk1 - 150
            coffee1 = coffee1 - 54
            resources.update(water=water1)
            resources.update(milk=milk1)
            resources.update(coffee=coffee1)
        elif dec == "cappuccino":
            water1 = water1 - 250
            milk1 = milk1 - 100
            coffee1 = coffee1 - 54
            resources.update(water=water1)
            resources.update(milk=milk1)
            resources.update(coffee=coffee1)
        elif dec == "report":
            show = f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}"
            return show


def kaching(deci, quart, dim, nick, pen):
    total = 0
    cost1 = 1.5
    cost2 = 2.5
    cost3 = 3.0

    if quart.isnumeric():
        quart = int(quart)
    else:
        quart = 0
    if dim.isnumeric():
        dim = int(dim)
    else:
        dim = 0
    if nick.isnumeric():
        nick = int(nick)
    else:
        nick = 0
    if pen.isnumeric():
        pen = int(pen)
    else:
        pen = 0
    qr = int(quart) * 0.25
    dm = int(dim) * 0.10
    nc = int(nick) * 0.05
    pn = int(pen) * 0.01

    if deci == "espresso":
        total = total + qr + dm + nc + pn
        if total >= cost1:
            total = total - cost1
            pr = f"Here is ${total:.1f} in change.\nHere is your espresso ☕️. Enjoy!"
            return pr
        else:
            warning = "Sorry that's not enough money. Money refunded."
            return warning
    elif deci == "latte":
        total = total + qr + dm + nc + pn
        if total >= cost2:
            total = total - cost2
            pr = f"Here is ${total:.1f} in change.\nHere is your espresso ☕️. Enjoy!"
            return pr
        else:
            warning = "Sorry that's not enough money. Money refunded."
            return warning

    elif deci == "cappuccino":
        total = total + qr + dm + nc + pn
        if total >= cost3:
            total = total - cost3
            pr = f"Here is ${total:.1f} in change.\nHere is your espresso ☕️. Enjoy!"
            return pr
        else:
            warning = f"Sorry that's not enough money. Money refunded."
            return warning


money = 0
holder = True
while holder:
    decision = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if decision != "report" and decision != "latte" and decision != "espresso" and decision != "cappuccino" and decision != "off":
        print("Sorry, wrong input.")
    else:
        if decision == "off":
            print("Sayonara~")
            holder = False
        if decision != "report" and decision != "off":
            if resources['water'] < MENU[f'{decision}']['ingredients']['water']:
                money -= MENU[f'{decision}']['cost']
                res = "Sorry there is not enough water."
                print(res)
            elif resources['milk'] < MENU[f'{decision}']['ingredients']['milk']:
                money -= MENU[f'{decision}']['cost']
                res1 = "Sorry there is not enough milk."
                print(res1)
            elif resources['coffee'] < MENU[f'{decision}']['ingredients']['coffee']:
                money -= MENU[f'{decision}']['cost']
                res2 = "Sorry there is not enough coffee."
                print(res2)
            else:
                q = input("How many quarters?: ")
                if q.isnumeric():
                    q = q
                else:
                    q = "0"
                d = input("How many dimes?: ")
                if d.isnumeric():
                    d = d
                else:
                    d = "0"
                n = input("How many nickles?: ")
                if n.isnumeric():
                    n = n
                else:
                    d = "0"
                p = input("How many pennies?: ")
                if p.isnumeric():
                    p = p
                else:
                    p = "0"
                if kaching(decision, q, d, n, p, ) == "Sorry that's not enough money. Money refunded.":
                    successful = True
                    if successful == True:
                        money += 0
                    else:
                        if decision == "espresso":
                            money += 1.5
                        if decision == "latte":
                            money += 2.5
                        if decision == "cappuccino":
                            money += 3.0
                print(kaching(decision, q, d, n, p, ))
                data(decision)
        else:
            if decision != "off":
                print(data(decision))
                print(f"Money: ${money}")
