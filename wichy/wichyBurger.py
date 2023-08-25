from wichy.wichy import wichy


class WichyBurger(wichy):
    def __init__(self, ingredients, bun, drink="", side="", sauce=""):
        super().__init__(ingredients, 90, drink, side, sauce)
        self.__bun = bun

    # menu

    @classmethod
    def vegan_meal(cls):
        ing = ['veg mayo', "tomato", "veg meat patty", "lettuces", "veg mozzarella sticks"]
        return cls(ing, "wheat", 'cola', 'frise', "ranch")

    @classmethod
    def meat_lovers_meal(cls):
        ing = ['mayo', "tomato", "meat patty", "bacon", "meat patty", "lettuces", "BBQ"]
        return cls(ing, "wheat", 'cola diet', 'animal style frise', "buffalo")

    @classmethod
    def cheese_lover_meal(cls):
        ing = ['cheddar', "tomato", "stuffed meat patty", "lettuces", "mozzarella sticks"]
        return cls(ing, "wheat", 'sprit', 'cheese frise', "cheese")

    @classmethod
    def chicken_meal(cls):
        ing = ['mayo', "tomato", "chicken patty", "lettuces", "mozzarella sticks"]
        return cls(ing, "wheat", 'cola', 'frise', "ranch")

    @classmethod
    def keto_meal(cls):
        ing = ['mayo', "tomato", "meat patty", "mozzarella sticks"]
        return cls(ing, "lettuces", 'cola diet', 'vegi frise', "ranch")

    @classmethod
    def special_meal(cls):
        ing = ['mayo', "tomato", "stuffed meat patty", "lettuces", " mozzarella sticks", "bacon"]
        return cls(ing, "wheat", 'fayrouz', 'frise', "special")

    def __str__(self):
        return f'''
        bun: {self.__bun}
        ingredients: {self.ingredients}
        bun: {self.__bun}
        side: {self.side}
        drink: {self.drink}
        sauce: {self.sauce}
        price: {self.total_price()}'''
