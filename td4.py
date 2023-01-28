from dff import DFF
from rom import ROM
from multiplexer import multiplexer16, multiplexer


class Computer:
    def __init__(self):
        self.switch = bin(0000)
        self.LED = bin(0000)

    def clock(self):
        pass

    def input(self, switch):
        self.switch = [int(s) for s in switch]
        print("input      :", self.switch)

    def output(self):
        print("output     :", self.LED)

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
        next_a, next_b, next_cf, next_ip, next_out = self.ALU(opecode, imm)
        for i in range(4):
            self.register_a[i].input(next_a[i])
            self.register_b[i].input(next_b[i])
            self.register_ip[i].input(next_ip[i])
            self.register_out[i].input(next_out[i])
        self.register_cf.input(next_cf)

    def ALU(self, opecode, imm):
        # 汎用レジスタAの計算
        register_a_Q = [i.Q for i in self.register_a]
        cf_add_A_imm, result_add_A_imm = self.Add(register_a_Q, imm)
        register_b_Q = [i.Q for i in self.register_b]
        next_a = [
            multiplexer16(
                result_add_A_imm[i], register_b_Q[i], self.switch[i], imm[i],
                register_a_Q[i], register_a_Q[i], register_a_Q[i], register_a_Q[i],
                register_a_Q[i], register_a_Q[i], register_a_Q[i], register_a_Q[i],
                register_a_Q[i], register_a_Q[i], register_a_Q[i], register_a_Q[i],
                opecode[0], opecode[1], opecode[2], opecode[3]) for i in range(4)]
        # 汎用レジスタBの計算
        cf_add_B_imm, result_add_B_imm = self.Add(register_b_Q, imm)
        next_b = [
            multiplexer16(register_b_Q[i], register_b_Q[i], register_b_Q[i], register_b_Q[i],
                          register_a_Q[i], result_add_B_imm[i], self.switch[i], imm[i],
                          register_b_Q[i], register_b_Q[i], register_b_Q[i], register_b_Q[i],
                          register_b_Q[i], register_b_Q[i], register_b_Q[i], register_b_Q[i],
                          opecode[0], opecode[1], opecode[2], opecode[3]
                          ) for i in range(4)
        ]
        # キャリーフラグ(CF)の計算
        next_cf = multiplexer16(
            cf_add_A_imm, 0, 0, 0, 0, cf_add_B_imm, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0,
            opecode[0], opecode[1], opecode[2], opecode[3])
        # 命令ポインタ(IP)の計算
        ip_plus1_cf, ip_plus1_result = self.Add([i.Q for i in self.register_ip], [0, 0, 0, 1])
        next_ip = [multiplexer16(
            ip_plus1_result[i], ip_plus1_result[i], ip_plus1_result[i], ip_plus1_result[i],
            ip_plus1_result[i], ip_plus1_result[i], ip_plus1_result[i], ip_plus1_result[i],
            ip_plus1_result[i], ip_plus1_result[i], ip_plus1_result[i], ip_plus1_result[i],
            ip_plus1_result[i], ip_plus1_result[i], multiplexer(imm[i], ip_plus1_result[i], self.register_cf.Q), imm[i],
            opecode[0], opecode[1], opecode[2], opecode[3]) for i in range(4)
        ]
        # アウトプットの計算
        next_out = [
            multiplexer16(
                0, 0, 0, 0, 0, 0, 0, 0,
                0, register_b_Q[i], 0, imm[i], 0, 0, 0, 0,
                opecode[0], opecode[1], opecode[2], opecode[3]
            )
            for i in range(4)
        ]

        print("CF         :", next_cf)
        print("register_A :", next_a)
        print("register_B :", next_b)
        print("IP         :", next_ip)
        return next_a, next_b, next_cf, next_ip, next_out

    # 4bit加算器
    # 論理ゲートを用いた実装は今回省略
    def Add(self, x, y):
        x_int = int("0b" + "".join([str(i) for i in x]), 0)
        y_int = int("0b" + "".join([str(i) for i in y]), 0)
        result_int = x_int + y_int
        if result_int >= 16:
            cf = 1
            result = bin(result_int - 16)
            result = [int(i) for i in format(int(result, 2), "04b")]
        else:
            cf = 0
            result = bin(result_int)
            result = [int(i) for i in format(int(result, 2), "04b")]
        return cf, result
