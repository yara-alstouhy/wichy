from wichy import wichy, wichyBurger as burger, wichyPizza as pizza, wichyPasta as pasta


# functions


def check(item):
    i = ""
    while i != 'y' and i != 'n':
        i = input(f'''do you want {item} : (y / n)''')
        i = i.lower()
        if i == 'y':
            item = input(f'''please enter your {item}: ''')
            if item == "":
                error()
                i = ""
            else:
                return item
        elif i != "n":
            error()
        else:
            return "none"


def ingredients():
    ing = []
    z = 0
    print('''please enter your ingredients on by one
    and when are done enter: e
    ''')
    while z != 'e':
        z = input("enter your ingredient: ")
        if z == 'e' and len(ing) == 0:
            print("ERROR: not enough ingredients")
            z = ""
        elif z == 'e' and len(ing) > 0:
            return ing
        else:
            ing.append(z)


def error():
    print("ERROR: WRONG INPUT")


# prompts

print("welcome to wichy")
x = 0
order = []
total = 0

while x != "5":
    x = input('''how can we help you today
        please enter a number from 1 to 5
        1- pizza
        2- pasta
        3- burger
        4- chart
        5- check out
        ''')
    if x == "1":
        pi = 0
        while pi != '6':
            pi = input('''****************************************** our menu ******************************************
                     please enter a number from 1 to 6
                     1-vegan pizza
                      {"green pepper", "red pepper","veg mozzarella", "olives"}
                      ["pan", 'frise', 'cola', "ranch"]
                      
                     2-meat lovers pizza
                      {"red pepper", "tomato", "pepperoni", "bacon", "BBQ"}
                      ["thin", 'animal style frise', 'cola diet', "buffalo"]

                     3-cheese lover pizza
                      {'cheddar',"gouda ", "mozzarella "}
                      ["stuffed", 'cheese frise', 'sprit']

                     4-big tasty pizza
                      {"chopped patty","big tasty sauce","red pepper", "tomato"}
                      ["thin", 'frise', 'fayrouz', "special"]

                      5-custom order
                      {choose you toppings}
                      [crust , drink (opt), side (opt) ,side sauce(opt)]

                      6-back
            ''')
            if pi == "1":
                order.append(pizza.WichyPizza.vegan_pizza())
                print("veg pizza added successfully")
                var = pizza.WichyPizza.vegan_pizza().total_price()
                total += var

            elif pi == "2":
                order.append(pizza.WichyPizza.meat_lovers_pizza())
                print("meat lovers pizza added successfully")
                var = pizza.WichyPizza.meat_lovers_pizza().total_price()
                total += var
            elif pi == "3":
                order.append(pizza.WichyPizza.cheese_lover_pizza())
                print("cheese lover pizza added successfully")
                var = pizza.WichyPizza.cheese_lover_pizza().total_price()
                total += var
            elif pi == "4":
                order.append(pizza.WichyPizza.big_tasty_pizza())
                print("big tasty pizza added successfully")
                var = pizza.WichyPizza.big_tasty_pizza().total_price()
                total += var
            elif pi == "5":
                ing = ingredients()
                bun = input('''please enter your crust type: ''')
                side = check("side")
                drink = check("drink")
                side_sauce = check("side sauce")
                new = pizza.WichyPizza(ing, bun, drink, side, side_sauce)
                order.append(new)
                var = new.total_price()
                total += var
                print(f"your total is {var}")
                print("order added successfully")

            elif pi == "6":
                print(f'''your total is {total}''')
            else:
                error()

    elif x == "2":
        pa = 0
        while pa != '6':
            pa = input('''****************************************** our menu ******************************************
                        please enter a number from 1 to 6
                        1-pasta salad
                         {"corn", "green pepper", "red pepper"}
                         ["macaroni", "veg white", 'salad', 'cola']

                        2-bashamel
                         {'cheddar', "meat", "mozzarella"}
                         ["penne", "bashamel", 'sambosa', 'sprit', "yogurt"]

                        3-chicken ravioli
                         {"chicken", "cream cheese", "corn", "green pepper"}
                         ["ravioli", "pesto", "mozzarella sticks", 'cola', "sweet chili"]

                        4-kids meal
                         {'cheese'}
                         ["macaroni", "cheese", 'strips', 'juice', "ketchup"]

                         5-custom order
                         {choose you toppings}
                         [pasta type , pasta sauce , drink (opt), side (opt) ,side sauce(opt)]

                         6-back
               ''')
            if pa == "1":
                order.append(pasta.WichyPasta.pasta_salad())
                print("pasta salad added successfully")
                var = pasta.WichyPasta.pasta_salad().total_price()
                total += var
            elif pa == "2":
                order.append(pasta.WichyPasta.bashamel())
                print("bashamel added successfully")
                var = pasta.WichyPasta.bashamel().total_price()
                total += var
            elif pa == "3":
                order.append(pasta.WichyPasta.chicken_ravioli())
                print("chicken ravioli added successfully")
                var = pasta.WichyPasta.chicken_ravioli().total_price()
                total += var
            elif pa == "4":
                order.append(pasta.WichyPasta.kids_meal())
                print("kids meal added successfully")
                var = pasta.WichyPasta.kids_meal().total_price()
                total += var
            elif pa == "5":
                ing = ingredients()
                pasta_type = input('''please enter your pasta type: ''')
                pasta_sauce = input('''please enter your pasta sauce: ''')
                side = check("side")
                drink = check("drink")
                side_sauce = check("side_sauce")
                new = pasta.WichyPasta(ing, pasta_type, pasta_sauce, drink, side, side_sauce)
                order.append(new)
                var = new.total_price()
                total += var
                print(f"your total is {var}")
                print("order added successfully")

            elif pa == "6":
                print(f'''your total is {total}''')
            else:
                error()

    elif x == "3":
        bu = 0
        while bu != '7':
            bu = input('''****************************************** our menu ******************************************
                     please enter a number from 1 to 6
                     1-meat lovers meal
                      {'mayo', "tomato", "meat patty", "bacon", "meat patty", "lettuces", "BBQ"}
                      ["wheat", 'animal style frise', 'cola diet', "buffalo"]

                     2-cheese lover  meal
                      {'cheddar', "tomato", "stuffed meat patty", "lettuces", "mozzarella sticks"}
                      ["wheat", 'cheese frise', 'sprit', "cheese"]

                     3-chicken meal
                      {'mayo', "tomato", "chicken patty", "lettuces", "mozzarella sticks"}
                      ["wheat", 'frise', 'cola', "ranch"]

                     4-keto meal
                      {'mayo', "tomato", "meat patty", "mozzarella sticks"}
                      ["lettuces", 'vegi frise', 'cola diet', "ranch"]

                     5-special meal
                      {'mayo', "tomato", "stuffed meat patty", "lettuces", " mozzarella sticks", "bacon"}
                      ["wheat", 'frise', 'fayrouz', "special"]

                      6-custom order
                      {choose you toppings}
                      [crust , drink (opt), side (opt) ,side sauce(opt)]
]
                      7-back
            ''')
            if bu == "1":
                order.append(burger.WichyBurger.meat_lovers_meal())
                print("meat lovers meal added successfully")
                var = burger.WichyBurger.meat_lovers_meal().total_price()
                total += var
            elif bu == "2":
                order.append(burger.WichyBurger.cheese_lover_meal())
                print("cheese lover  meal added successfully")
                var = burger.WichyBurger.cheese_lover_meal().total_price()
                total += var
            elif bu == "3":
                order.append(burger.WichyBurger.chicken_meal())
                print("chicken meal added successfully")
                var = burger.WichyBurger.chicken_meal().total_price()
                total += var
            elif bu == "4":
                order.append(burger.WichyBurger.keto_meal())
                print("keto meal added successfully")
                var = burger.WichyBurger.keto_meal().total_price()
                total += var
            elif bu == "5":
                order.append(burger.WichyBurger.special_meal())
                print("keto meal added successfully")
                var = burger.WichyBurger.special_meal().total_price()
                total += var
            elif bu == "6":
                ing = ingredients()
                bun = input('''please enter your bun type: ''')
                side = check("side")
                drink = check("drink")
                side_sauce = check("side sauce")
                new = burger.WichyBurger(ing, bun, drink, side, side_sauce)
                order.append(new)
                var = new.total_price()
                total += var
                print(f"your total is {var}")
                print("order added successfully")

            elif bu == "7":
                print(f'''your total is {total}''')
            else:
                error()

    elif x == "4":
        for i in order:
            print(f'''{i}''')
        print(f"your total: {total}")

    elif x == "5":
        if total == 0:
            print("sorry that you didn't like any of our product today "
                  "thank you for using wichy have a great day")

        else:
            t = False
            while not t:
                ask = ""
                while ask != "y" and ask != "n":
                    ask = input(f'''your total is: {total}
                      do you have a promo code: (y/n)
                    ''')
                    if ask == 'y':
                        code = input("please enter your promo code: ")
                        [total, t] = wichy.wichy.promo_code(code, total)
                    elif ask != "n":
                        error()
                    else:
                        t = True
            print("thank you for using wichy have a great day")
    else:
        error()
