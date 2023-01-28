from logic_gate import AND, OR, NOT

# SでA,Bから選択


def multiplexer(A, B, S):
    return OR(
        AND(A, NOT(S)),
        AND(B, S)
    )

# S1,S0でA,B,C,Dから選択


def multiplexer4(A, B, C, D, S1, S0):
    return multiplexer(
        multiplexer(A, B, S0),
        multiplexer(C, D, S0),
        S1
    )

# S3,S2,S1,S0でi0000~i1111から選択


def multiplexer16(
        i0000, i0001, i0010, i0011, i0100, i0101, i0110, i0111,
        i1000, i1001, i1010, i1011, i1100, i1101, i1110, i1111,
        S3, S2, S1, S0):
    return multiplexer4(
        multiplexer4(
            i0000, i0001, i0010, i0011, S1, S0
        ),
        multiplexer4(
            i0100, i0101, i0110, i0111, S1, S0
        ),
        multiplexer4(
            i1000, i1001, i1010, i1011, S1, S0
        ),
        multiplexer4(
            i1100, i1101, i1110, i1111, S1, S0
        ),
        S3, S2
    )


if __name__ == "__main__":
    print("multiplexer:",
          multiplexer(1, 0, 0), multiplexer(0, 1, 1))

    print("multiplexer4:",
          multiplexer4(1, 0, 0, 0, 0, 0), multiplexer4(0, 1, 0, 0, 0, 1),
          multiplexer4(0, 0, 1, 0, 1, 0), multiplexer4(0, 0, 0, 1, 1, 1))

    print("multiplxer16:",
          multiplexer16(
              0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
              0, 1, 0, 0)
          )
