import time
from td4 import TD4


def exec(computer, switch):
    while True:
        # 毎秒1クロック進める(1Hz)
        time.sleep(1)
        computer.clock()
        computer.input(switch)
        computer.output()


if __name__ == "__main__":
    print("コンピュータに対する入力:バイナリ4桁")
    switch = input()
    td4 = TD4()
    exec(td4, switch)
