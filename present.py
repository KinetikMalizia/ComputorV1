from function_plus import p_term
import math


def show(array, test_mode):
  degree = clean_poly(array)
  #reduit
  reducted = ""
  for term in array:
    if term.a != 0:
      reducted += f"{cust_round_reduced(term.a)} * X^{term.p} "
  reducted = reducted.strip()
  if (len(reducted) == 0):
    reducted = "0"
  if (reducted[0] == '+'):
    reducted = reducted[2:]
  reducted += " = 0"
  if (test_mode):
    print("Reduced form: " + reducted)

  #degree
  if (test_mode):
    print("Polynomial degree: " + str(degree))
  #solution
  if (degree <= 2):
    return (process_solution(array, degree))
  else:
    print("Can't solve polynomials with degree greater than 2")


def process_solution(array, degree):
  if (degree == 2):
    return solve_polynomial(array)
  if (degree == 1):
    return solve_linear(array)
  if (degree == 0):
    solve_constant(array)
    return (0)


def solve_polynomial(array):
  delta = array[1].a**2 - 4 * array[0].a * array[2].a
  if (delta < 0):
    print("No real solutions")
  if (delta == 0):
    print("Discriminant is zero, solution is: " +
          str(cust_round(bsec(array, delta)[0])))
  if (delta > 0):
    ans = bsec(array, delta)
    print("Discriminant > 0, solutions are: " + str(ans[0]) + " and " +
          str(ans[1]))
    return (ans)


def bsec(array, delta):
  solution1 = (-array[1].a - math.sqrt(delta)) / (2 * array[0].a)
  solution2 = None
  if (delta != 0):
    solution2 = (-array[1].a + math.sqrt(delta)) / (2 * array[0].a)
  return ([cust_round(solution1), cust_round(solution2)])


def solve_linear(array):
  solution = (-1 * array[1].a) / array[0].a
  print("Linear solution is: " + str(cust_round(solution)))
  return (cust_round(solution))


def solve_constant(array):
  if (array[0].a == 0):
    print("Solution is R")
  else:
    print(str(cust_round(array[0].a)),
          "= 0 -- Equation is WRONG -- no solution")


def clean_poly(array):
  while (array[0].p != 0 and array[0].a == 0):
    array.pop(0)
  return (array[0].p)


def cust_round_reduced(number):
  ret = round(number, 3)
  if ret.is_integer():
    ret = int(ret)

  ret_str = ""
  if (ret > 0):
    ret_str = "+ " + str(ret)
  if (ret < 0):
    ret_str = "- " + str(abs(ret))
  return ret_str


def cust_round(number):
  ret = round(number, 8)
  if ret.is_integer():
    ret = int(ret)

  return ret
