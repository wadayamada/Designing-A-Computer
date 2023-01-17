from multiplexer import multiplexer4

# addr=4bit, data=8bitのROM


class ROM:
    def __init__(self):
        # addr0~15
        self.data = [
            # 8bitのデータ
            [1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
        ]

    def get_data(self, addr):
        data = []
        for i in range(8):
            data.append(
                multiplexer4(
                    multiplexer4(
                        self.data[0][i], self.data[1][i], self.data[2][i], self.data[3][i], addr[2], addr[3]
                    ),
                    multiplexer4(
                        self.data[4][i], self.data[5][i], self.data[6][i], self.data[7][i], addr[2], addr[3]
                    ),
                    multiplexer4(
                        self.data[8][i], self.data[9][i], self.data[10][i], self.data[11][i], addr[2], addr[3]
                    ),
                    multiplexer4(
                        self.data[12][i], self.data[13][i], self.data[14][i], self.data[15][i], addr[2], addr[3]
                    ),
                    addr[0], addr[1]
                )
            )
        return data


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
