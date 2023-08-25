from wichy.wichy import wichy


class WichyPasta(wichy):
    def __init__(self, ingredients, pasta_type, pasta_sauce, drink, side, sauce=""):
        super().__init__(ingredients, 60, drink, side, sauce)
        self.__pasta_sauce = pasta_sauce
        self.__pasta_type = pasta_type

    @classmethod
    def pasta_salad(cls):
        ing = ["corn", "green pepper", "red pepper"]
        return cls(ing, "macaroni", "veg white", 'cola', 'salad')

    @classmethod
    def bashamel(cls):
        ing = ['cheddar', "meat", "mozzarella"]
        return cls(ing, "penne", "bashamel", 'sprit', 'sambosa', "yogurt")

    @classmethod
    def chicken_ravioli(cls):
        ing = ["chicken", "cream cheese", "corn", "green pepper"]
        return cls(ing, "ravioli", "pesto", 'cola', "mozzarella sticks", "sweet chili")

    @classmethod
    def kids_meal(cls):
        ing = ['cheese']
        return cls(ing, "macaroni", "cheese", 'juice', 'strips', "ketchup")

    def __str__(self):
        return f'''
        pasta: {self.__pasta_type}
        pasta sauce" {self.__pasta_sauce}
        ingredients: {self.ingredients}
        side: {self.side}
        drink: {self.drink}
        sauce: {self.sauce}
        price: {self.total_price()}'''
