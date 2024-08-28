import math
import sys

def loves_me(n: int):
    if n < 1:
        raise ValueError("0 and negative are invalid inputs for loves_me()")
    elif n == 1:
        print("LOVES ME")
        return
    
    if n % 2 == 1:
        for _ in range(math.floor(n/2)):
            print("Loves me, Loves me not, ", end="")
        print("LOVES ME")
    else:
        for _ in range(math.floor(n/2 - 1)):
            print("Loves me, Loves me not, ", end="")
        print("Loves me, LOVES ME NOT")


if __name__ == "__main__":
    argv = sys.argv
    times = int(argv[1])
    loves_me(times)
