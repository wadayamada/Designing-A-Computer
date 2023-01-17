class Computer:
    def __init__(self):
        self.switch = bin(0000)
        self.LED = bin(0000)

    def clock(self):
        pass

    def input(self, switch):
        self.switch = switch

    def output(self):
        print(self.LED)

# とりあえず動作する4bitのコンピューター


class TD4(Computer):
    pass
