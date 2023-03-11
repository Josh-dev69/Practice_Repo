from calculator import add, sub, mul, div
import sys

num_args = len(sys.argv) - 1
ops = {"+": add, "-": sub, "*": mul, "/": div}

if num_args != 3:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    sys.exit(1)
if sys.argv[2] not in list(ops.keys()):
    print("Unknown operator. Available operators: +, -, * and /")
    sys.exit(1)
    
a = int(sys.argv[1])
b = int(sys.argv[3])
    
print("{} {} {} = {}".format(a, sys.argv[2], b, ops[sys.argv[2]](a, b)))