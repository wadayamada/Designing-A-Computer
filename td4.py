from dff import DFF, DFF4bit
from rom import ROM
from multiplexer import multiplexer16, multiplexer, multiplexer16_4bit, multiplexer_4bit


# とりあえず動作する4bitのコンピューター


class TD4():
    def __init__(self, switch):
        # 入力スイッチ
        self.switch = [int(s) for s in switch]
        # 出力LED
        self.LED = [0, 0, 0, 0]
        # 汎用レジスタ
        self.register_a = DFF4bit()
        self.register_b = DFF4bit()
        # キャリーフラグ(CF)
        self.register_cf = DFF()
        # 命令ポインタ(IP)
        self.register_ip = DFF4bit()
        # IOレジスタ
        self.register_out = DFF4bit()
        # ROM
        self.rom = ROM()

    def clock(self):
        # 新しい値をregisterに読み込む
        self.register_a.clock()
        self.register_b.clock()
        self.register_ip.clock()
        self.register_out.clock()
        self.register_cf.clock()
        # 出力
        self.LED = self.register_out.get_Q()
        # ROMからデータを取り出す
        data = self.rom.get_data(self.register_ip.get_Q())
        opecode = data[0:4]
        imm = data[4:8]
        # ALUで計算
        next_a, next_b, next_cf, next_ip, next_out = self.ALU(opecode, imm)
        self.register_a.set(next_a)
        self.register_b.set(next_b)
        self.register_ip.set(next_ip)
        self.register_out.set(next_out)
        self.register_cf.set(next_cf)

    def ALU(self, opecode, imm):
        # 汎用レジスタAの計算
        register_a_Q = self.register_a.get_Q()
        cf_add_A_imm, result_add_A_imm = self.Add(register_a_Q, imm)
        register_b_Q = self.register_b.get_Q()
        next_a = multiplexer16_4bit(
            result_add_A_imm, register_b_Q, self.switch, imm,
            register_a_Q, register_a_Q, register_a_Q, register_a_Q,
            register_a_Q, register_a_Q, register_a_Q, register_a_Q,
            register_a_Q, register_a_Q, register_a_Q, register_a_Q,
            opecode
        )
        # 汎用レジスタBの計算
        cf_add_B_imm, result_add_B_imm = self.Add(register_b_Q, imm)
        next_b = multiplexer16_4bit(
            register_b_Q, register_b_Q, register_b_Q, register_b_Q,
            register_a_Q, result_add_B_imm, self.switch, imm,
            register_b_Q, register_b_Q, register_b_Q, register_b_Q,
            register_b_Q, register_b_Q, register_b_Q, register_b_Q,
            opecode
        )
        # キャリーフラグ(CF)の計算
        next_cf = multiplexer16(
            cf_add_A_imm, 0, 0, 0,
            0, cf_add_B_imm, 0, 0,
            0, 0, 0, 0,
            0, 0, 0, 0,
            opecode
        )
        # 命令ポインタ(IP)の計算
        ip_plus1_cf, ip_plus1_result = self.Add(self.register_ip.get_Q(), [0, 0, 0, 1])
        next_ip = multiplexer16_4bit(
            ip_plus1_result, ip_plus1_result, ip_plus1_result, ip_plus1_result,
            ip_plus1_result, ip_plus1_result, ip_plus1_result, ip_plus1_result,
            ip_plus1_result, ip_plus1_result, ip_plus1_result, ip_plus1_result,
            ip_plus1_result, ip_plus1_result, multiplexer_4bit(imm, ip_plus1_result, self.register_cf.Q), imm,
            opecode
        )
        # アウトプットの計算
        next_out = multiplexer16_4bit(
            [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],
            [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],
            [0, 0, 0, 0], register_b_Q, [0, 0, 0, 0], imm,
            [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],
            opecode
        )
        # print
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
