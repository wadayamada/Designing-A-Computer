from dff import DFF
from rom import ROM


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
    def __init__(self):
        super().__init__()
        # 汎用レジスタ
        self.register_a = [DFF(), DFF(), DFF(), DFF()]
        self.register_b = [DFF(), DFF(), DFF(), DFF()]
        # フラグレジスタ
        self.register_cf = DFF()
        # 命令ポインタ
        self.register_ip = [DFF(), DFF(), DFF(), DFF()]
        # IOレジスタ
        self.register_out = [DFF(), DFF(), DFF(), DFF()]
        # ROM
        self.rom = ROM()

    def clock(self):
        # 新しい値をregisterに読み込む
        for i in range(4):
            self.register_a[i].clock()
            self.register_b[i].clock()
            self.register_ip[i].clock()
            self.register_out[i].clock()
        self.register_cf.clock()
        # 出力
        self.LED = [dff.Q for dff in self.register_out]
        # ROMからデータを取り出す
        data = self.rom.get_data([dff.Q for dff in self.register_ip])
        opecode = data[0:4]
        imm = data[4:8]
        # ALUで計算
        next_a, next_b, next_cf, next_ip, next_out = self.ALU(opecode, imm, self.switch)
        for i in range(4):
            self.register_a[i].input(next_a[i])
            self.register_b[i].input(next_b[i])
            self.register_ip[i].input(next_ip[i])
            self.register_out[i].input(next_out[i])
        self.register_cf.input(next_cf)

    def ALU(self, opecode, imm, switch):
        next_a = [0, 0, 0, 0]
        next_b = [0, 0, 0, 0]
        next_cf = 0
        next_ip = [0, 0, 0, 0]
        next_out = [0, 0, 0, 0]
        return next_a, next_b, next_cf, next_ip, next_out
