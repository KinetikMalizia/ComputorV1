import math
import sys
from function_plus import *
from present import *


class bcolors:
  HEADER = '\033[95m'
  OKBLUE = '\033[94m'
  OKCYAN = '\033[96m'
  OKGREEN = '\033[92m'
  WARNING = '\033[93m'
  FAIL = '\033[91m'
  ENDC = '\033[0m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'


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
