class Book:
    def __init__(self, title, pages, price):
        self.title = title
        self.pages = pages
        self.__price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value >= 0:
            self.__price = value
        else:
            raise ValueError("Price is negative")


kniha = Book("Harry Potter", 400, 10)
print(kniha.price)
kniha.price = 20
print(kniha.price)
kniha.price = -10
print(kniha.price)
