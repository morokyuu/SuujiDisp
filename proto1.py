
class Tile:
    def __init__(self,value):
        self._value = value

    def __str__(self):
        return f'<{self._value}>'
        
class Tens(Tile):
    def __init__(self):
        super().__init__(10)

class Ones(Tile):
    def __init__(self):
        super().__init__(1)


class Basket:
    def __init__(self):
        self.value = 0
        self.tens_bin = []
        self.ones_bin = []
    
    @classmethod
    def from_value(cls, value):
        instance = cls()
        instance.put(value)
        return instance

    def put(self,value):
        b10 = value // 10
        b1 = value % 10
        self.tens_bin = [Tens()] * b10
        self.ones_bin = [Ones()] * b1

    def __str__(self):
        return f'{Tens()} : {len(self.tens_bin)}\n{Ones()} : {len(self.ones_bin)}'

    def __add__(self):
        return self.b10


class UI:
    def __init__(self):
        self.value = 0
        pass
    
    def input(self):
        try:
            self.value = int(input())
        except ValueError:
            self.value = 0
        return self.value


if __name__ == '__main__':
    
    ui = UI()
    bsk = Basket()
    
    bsk2 = Basket.from_value(14)
    print(bsk2)

    while True:
        v = ui.input()
        bsk.put(v)
        print(bsk)


