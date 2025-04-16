
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
        self.prev_value = 0

    def set_value(self):
        try:
            self.value = int(input())
        except ValueError:
            self.value = 0

        diff = self.value - self.prev_value
        print(f'{self.value} - {self.prev_value} = {diff}')
        self.prev_value = self.value

#        b10 = amount // 10
#        b1 = amount % 10
#        print(f'{b10}, {b1}')

if __name__ == '__main__':
    tens = Tens()
    print(tens)

    bsk = Basket()
    while True:
        bsk.set_value()


#    bsk = Basket()
#    bsk.add(54)
#    print(bsk)
