from logic_gate import AND, OR, XOR

# 半加算器


def half_adder(A, B):
    S = XOR(A, B)
    C = AND(A, B)
    return {"C": C, "S": S}

# 全加算器


def full_adder(A, B, C_in):
    Q1 = XOR(A, B)
    Q2 = AND(A, B)
    Q3 = XOR(Q1, C_in)
    Q4 = AND(Q1, C_in)
    Q5 = OR(Q2, Q4)
    S = Q3
    C_out = Q5
    return {"C_out": C_out, "S": S}


if __name__ == "__main__":
    print("half_adder:",
          half_adder(0, 0), half_adder(0, 1), half_adder(1, 0), half_adder(1, 1))

    print("full_adder:",
          full_adder(0, 0, 0), full_adder(0, 0, 1), full_adder(0, 1, 0), full_adder(0, 1, 1),
          full_adder(1, 0, 0), full_adder(1, 0, 1), full_adder(1, 1, 0), full_adder(1, 1, 1))
