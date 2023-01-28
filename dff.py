# DFF
# 論理ゲートを用いた実装は今回は省略

class DFF:
    def __init__(self):
        self.D = 0
        self.Q = 0

    def set(self, D):
        self.D = D

    def clock(self):
        self.Q = self.D


class DFF4bit:
    def __init__(self):
        self.dff_list = [DFF(), DFF(), DFF(), DFF()]

    def set(self, D_4bit):
        for i in range(4):
            self.dff_list[i].set(D_4bit[i])

    def clock(self):
        for i in range(4):
            self.dff_list[i].clock()

    def get_Q(self):
        return [i.Q for i in self.dff_list]


if __name__ == "__main__":
    dff = DFF()
    print(dff.Q)
    dff.input(1)
    print(dff.Q)
    dff.clock()
    print(dff.Q)
