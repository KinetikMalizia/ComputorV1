import math
import sys
from function_plus import parse
from present import show

def main():
  if (len(sys.argv) < 2):
    print("WRONG FORMAT!")
    return
  else:
    equations = sys.argv[1:]

  for eq in equations:
    print("----------------")
    print("Equation: " + eq)
    parsed = parse(eq)
    show(parsed, 1)
    print("----------------")


main()