from multiplexer import multiplexer4, multiplexer16, multiplexer16_8bit

# addr=4bit, data=8bitのROM


class ROM:
    def __init__(self):
        # addr0~15
        self.data = [
            # 8bitのデータ*16
            # キッチンタイマーのコード
            [0, 1, 1, 0, 0, 0, 0, 0],  # 0: IN B
            [1, 0, 0, 1, 0, 0, 0, 0],  # 1: OUT B
            [0, 0, 1, 1, 1, 1, 0, 1],  # 2: MOV A 13
            [0, 0, 0, 0, 0, 0, 0, 1],  # 3: ADD A 1
            [1, 1, 1, 0, 0, 0, 1, 1],  # 4: JNC 3
            [0, 1, 0, 1, 0, 0, 0, 1],  # 5: ADD B 1
            [1, 1, 1, 0, 0, 0, 0, 1],  # 6: JNC 1
            [1, 0, 1, 1, 0, 0, 0, 0],  # 7: OUT 0
            [1, 0, 1, 1, 1, 1, 1, 1],  # 8: OUT 15
            [1, 1, 1, 1, 0, 1, 1, 1],  # 9: JMP 7
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
        ]

    def get_data(self, addr):
        return multiplexer16_8bit(
            self.data[0], self.data[1], self.data[2], self.data[3],
            self.data[4], self.data[5], self.data[6], self.data[7],
            self.data[8], self.data[9], self.data[10], self.data[11],
            self.data[12], self.data[13], self.data[14], self.data[15],
            addr
        )


if __name__ == "__main__":
    rom = ROM()
    # addr=0
    print(rom.get_data([0, 0, 0, 0]))
    # addr=4
    print(rom.get_data([0, 1, 0, 0]))
    # addr=8
    print(rom.get_data([1, 0, 0, 0]))
    # addr=12
    print(rom.get_data([1, 1, 0, 0]))
