class Product:
    def __init__(self, name, product_id, price, rating, stock):
        self.name = name
        self.product_id = product_id
        self.price = price
        self.rating = rating
        self.stock = stock

    def add_stock(self, quantity):
        self.stock += quantity

    def remove_stock(self, quantity):
        if quantity <= self.stock:
            self.stock -= quantity
        else:
            print("Недостаточно")

    def update_rating(self, new_rating):
        self.rating = new_rating

    def update_price(self, new_price):
        self.price = new_price


class Category:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_item(self, product):
        self.products.append(product)

    def remove_item(self, product):
        if product in self.products:
            self.products.remove(product)
        else:
            print("Не найдено в категории")

    def get_item(self, product_id):
        for product in self.products:
            if product.product_id == product_id:
                return product
        print("Не найдено в категории")
        return None


class Basket:
    def __init__(self):
        self.items = []

    def add_item(self, product):
        self.items.append(product)

    def remove_item(self, product):
        if product in self.items:
            self.items.remove(product)
        else:
            print("Не найдено в корзине")

    def get_item(self, product_id):
        for product in self.items:
            if product.product_id == product_id:
                return product
        print("Не найдено в корзине")
        return None

    def make_purchase(self):
        if len(self.items) > 0:
            print("Купленные плюшки:")
            for product in self.items:
                print(product.name)
            self.items = []
        else:
            print("Нужно больше золота")


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.basket = Basket()


# Создание объектов класса Категория
category1 = Category("Электроника")
category2 = Category("Одежда")

# Создание объектов класса Пользователь
user1 = User("user1", "password1")
user2 = User("user2", "password2")

# Создание товара
product1 = Product("4ядра_4гига_игровая видеокарта", 1, 1000, 4.5, 10)
category1.add_item(product1)

user1.basket.add_item(product1)
user1.basket.make_purchase()