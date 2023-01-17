# DFF
# 論理ゲートを用いた実装は今回は省略

class DFF:
    def __init__(self):
        self.D = 0
        self.Q = 0

    def input(self, D):
        self.D = D

    def clock(self):
        self.Q = self.D


if __name__ == "__main__":
    dff = DFF()
    print(dff.Q)
    dff.input(1)
    print(dff.Q)
    dff.clock()
    print(dff.Q)
