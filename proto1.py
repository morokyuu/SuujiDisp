
class Obj:
    def __init__(self,value):
        self._value = value

    def __str__(self):
        return f'<{self._value}>'
        


class Basket:
    def __init__(self):
        self.bin1 = []
        self.bin10 = []

    def add(self,amount):
        b10 = amount // 10
        b1 = amount % 10
        print(f'{b10}, {b1}')

        self.bin10 += [Obj(10)] * b10

    @amount.param
    def amount(self):

    def __str__(self):
        st = [b for b in self.bin10]
        return f'{st}'

if __name__ == '__main__':
    bsk = Basket()
    bsk.add(54)
    print(bsk)
