from logic_gate import AND, NOT


def decoder(Y, X):
    X_not = NOT(X)
    Y_not = NOT(Y)
    Out0 = AND(X_not, Y_not)
    Out1 = AND(X, Y_not)
    Out2 = AND(X_not, Y)
    Out3 = AND(X, Y)
    return Out0, Out1, Out2, Out3


if __name__ == "__main__":
    print("decoder:", decoder(0, 0), decoder(0, 1), decoder(1, 0), decoder(1, 1))
