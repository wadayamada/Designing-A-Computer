from logic_gate import AND, OR, NOT
from multiplexer import multiplexer, multiplexer4
from adder import full_adder

# Arithmetic Logit Unit


def ALU(A, B, Op3, Op2, Op1, Op0):

    A_selected = multiplexer(A, NOT(A), Op3)
    B_selected = multiplexer(B, NOT(B), Op2)

    AND_result = AND(A_selected, B_selected)
    OR_result = OR(A_selected, B_selected)
    ADD_result = full_adder(A_selected, B_selected, Op2)["S"]
    NOT_USE = 0

    Result = multiplexer4(AND_result, OR_result, ADD_result, NOT_USE, Op1, Op0)

    return Result


if __name__ == "__main__":
    # AND: Op=(0,0,0,0)
    print(ALU(0, 0, 0, 0, 0, 0), ALU(0, 1, 0, 0, 0, 0), ALU(1, 0, 0, 0, 0, 0), ALU(1, 1, 0, 0, 0, 0))

    # OR: Op=(0,0,0,1)
    print(ALU(0, 0, 0, 0, 0, 1), ALU(0, 1, 0, 0, 0, 1), ALU(1, 0, 0, 0, 0, 1), ALU(1, 1, 0, 0, 0, 1))

    # ADD: Op=(0,0,1,0)
    print(ALU(0, 0, 0, 0, 1, 0), ALU(0, 1, 0, 0, 1, 0), ALU(1, 0, 0, 0, 1, 0), ALU(1, 1, 0, 0, 1, 0))

    # SUBTRACT: Op=(0,1,1,0)
    print(ALU(0, 0, 0, 1, 1, 0), ALU(0, 1, 0, 1, 1, 0), ALU(1, 0, 0, 1, 1, 0), ALU(1, 1, 0, 1, 1, 0))

    # NOR: Op=(1,1,0,0)
    print(ALU(0, 0, 1, 1, 0, 0), ALU(0, 1, 1, 1, 0, 0), ALU(1, 0, 1, 1, 0, 0), ALU(1, 1, 1, 1, 0, 0))
