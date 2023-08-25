class wichy:
    __orderId = 0
    __codes = [{'code': "sorry", 'amount': '15'},
               {'code': "welcome", 'amount': '10'},
               {'code': "joo", 'amount': '100'}
               ]

    def __init__(self, ingredients, base_price, drink="none", side="none", sauce="none"):
        self.drink = drink
        self.side = side
        self.sauce = sauce
        self.ingredients = ingredients
        self.__ingPrice = int(len(self.ingredients) * 10)
        wichy.__orderId = wichy.__orderId + 1
        self.__totalPrice = int(base_price) + self.__ingPrice
        self.__lucky()

    def __lucky(self):
        if wichy.__orderId % 10 == 0:
            print(f'''CONGRATULATION YOU ARE OUR LUCKY CUSTOMER
                    you get extra 30% discount on this item''')
            self.__totalPrice = wichy.__promotion(self.__totalPrice, 30)

    def total_price(self):
        # print(f'''price: {self.__totalPrice} LE''')
        return self.__totalPrice

    @staticmethod
    def add_code(code, amount):
        wichy.__codes.append({"code": code, "amount": amount})

    @staticmethod
    def __promotion(total, amount):
        x = int(total) * (1 - (int(amount) / 100))
        return x

    @staticmethod
    def promo_code(code, total):
        # found = False
        for i in wichy.__codes:
            if code == i['code']:
                total = wichy.__promotion(total, i['amount'])
                print(f'''code added successfully 
                your new total is : {total}''')
                # found = True
                return [total, True]
        # if not found:
        print("code is not found")
        return [total, False]
