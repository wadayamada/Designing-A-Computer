import time
from td4 import TD4


def exec(computer):
    clock_counter = 0
    while True:
        # 毎秒1クロック進める(1Hz)
        time.sleep(1)
        print("--- clock_counter:", clock_counter, "---")
        print("input      :", computer.switch)
        print("output     :", computer.LED)
        computer.clock()
        clock_counter += 1


if __name__ == "__main__":
    # switchから4bit入力
    print("コンピュータに対する入力:バイナリ4桁")
    switch = input()
    td4 = TD4(switch)
    exec(td4)
