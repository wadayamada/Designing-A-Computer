def AND(A, B):
    return A and B


def OR(A, B):
    return A or B


def NOT(A):
    return int(not A)


def XOR(A, B):
    return A ^ B


if __name__ == "__main__":
    print("AND:", AND(0, 0), AND(0, 1), AND(1, 0), AND(1, 1))  # 0001
    print("OR:", OR(0, 0), OR(0, 1), OR(1, 0), OR(1, 1))  # 0111
    print("NOT:", NOT(0), NOT(1))  # 10
    print("XOR:", XOR(0, 0), XOR(0, 1), XOR(1, 0), XOR(1, 1))  # 0110
