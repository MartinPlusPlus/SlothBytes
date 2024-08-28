import math
import sys

def loves_me(n: int):
    if n < 1:
        raise ValueError("0 and negative are invalid inputs for loves_me()")
    elif n == 1:
        return "LOVES ME"
    
    s = ""
    if n % 2 == 1:
        for _ in range(math.floor(n/2)):
            s += "Loves me, Loves me not, "
        s += "LOVES ME"
    else:
        for _ in range(math.floor(n/2 - 1)):
            s += "Loves me, Loves me not, "
        s += "Loves me, LOVES ME NOT"

    return s


if __name__ == "__main__":
    argv = sys.argv
    times = int(argv[1])
    print(loves_me(times))
