from phone import Phone


class Apple(Phone):
    def __init__(self, name, price, voltage, screen_size, country):
        super().__init__(name, price, voltage, screen_size)
        self.country = country
