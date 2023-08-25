from wichy.wichy import wichy


class WichyPizza(wichy):
    def __init__(self, ingredients, crust, side, drink, sauce=""):
        super().__init__(ingredients, 80, drink, side, sauce)
        self.__crust = crust

    @classmethod
    def vegan_pizza(cls):
        ing = ["green pepper", "red pepper", "veg mozzarella", "olives"]
        return cls(ing, "pan", 'cola', 'frise', "ranch")

    @classmethod
    def meat_lovers_pizza(cls):
        ing = ["red pepper", "tomato", "pepperoni", "bacon", "BBQ"]
        return cls(ing, "thin", 'cola diet', 'animal style frise', "buffalo")

    @classmethod
    def cheese_lover_pizza(cls):
        ing = ['cheddar', "gouda ", "mozzarella "]
        return cls(ing, "stuffed", 'sprit', 'cheese frise')

    @classmethod
    def big_tasty_pizza(cls):
        ing = ["chopped patty", "big tasty sauce", "red pepper", "tomato"]
        return cls(ing, "thin", 'fayrouz', 'frise', "special")

    def __str__(self):
        return f'''
        ingredients: {self.ingredients}
        pizza crust : {self.__crust}
        side: {self.side}
        drink: {self.drink}
        sauce: {self.sauce}
        price: {self.total_price()}'''
