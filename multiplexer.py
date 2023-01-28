from logic_gate import AND, OR, NOT

# SでA,Bから選択


def multiplexer(A, B, S):
    return OR(
        AND(A, NOT(S)),
        AND(B, S)
    )

# S1,S0でA,B,C,Dから選択


def multiplexer4(A, B, C, D, S):
    return multiplexer(
        multiplexer(A, B, S[1]),
        multiplexer(C, D, S[1]),
        S[0]
    )

# S3,S2,S1,S0でi0000~i1111から選択


def multiplexer16(
        i0000, i0001, i0010, i0011, i0100, i0101, i0110, i0111,
        i1000, i1001, i1010, i1011, i1100, i1101, i1110, i1111,
        S):
    return multiplexer4(
        multiplexer4(
            i0000, i0001, i0010, i0011, S[2:4]
        ),
        multiplexer4(
            i0100, i0101, i0110, i0111, S[2:4]
        ),
        multiplexer4(
            i1000, i1001, i1010, i1011, S[2:4]
        ),
        multiplexer4(
            i1100, i1101, i1110, i1111, S[2:4]
        ),
        S[0:2]
    )


def multiplexer_4bit(A, B, S):
    return [multiplexer(A[i], B[i], S) for i in range(4)]


def multiplexer16_4bit(
        i0000, i0001, i0010, i0011, i0100, i0101, i0110, i0111,
        i1000, i1001, i1010, i1011, i1100, i1101, i1110, i1111,
        S):
    return [multiplexer16(
        i0000[i], i0001[i], i0010[i], i0011[i],
        i0100[i], i0101[i], i0110[i], i0111[i],
        i1000[i], i1001[i], i1010[i], i1011[i],
        i1100[i], i1101[i], i1110[i], i1111[i],
        S
    ) for i in range(4)]


def multiplexer16_8bit(
        i0000, i0001, i0010, i0011, i0100, i0101, i0110, i0111,
        i1000, i1001, i1010, i1011, i1100, i1101, i1110, i1111,
        S):
    return [multiplexer16(
        i0000[i], i0001[i], i0010[i], i0011[i],
        i0100[i], i0101[i], i0110[i], i0111[i],
        i1000[i], i1001[i], i1010[i], i1011[i],
        i1100[i], i1101[i], i1110[i], i1111[i],
        S
    ) for i in range(8)]


if __name__ == "__main__":
    print("multiplexer:",
          multiplexer(1, 0, 0), multiplexer(0, 1, 1))

    print("multiplexer4:",
          multiplexer4(1, 0, 0, 0, [0, 0]), multiplexer4(0, 1, 0, 0, [0, 1]),
          multiplexer4(0, 0, 1, 0, [1, 0]), multiplexer4(0, 0, 0, 1, [1, 1]))

    print("multiplxer16:",
          multiplexer16(
              0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
              [0, 1, 0, 0])
          )
