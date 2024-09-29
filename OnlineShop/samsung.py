from phone import Phone


class Samsung(Phone):
    def __init__(self, name, price, voltage, screen_size, foldable):
        super().__init__(name, price, voltage, screen_size)
        self.foldable = foldable
