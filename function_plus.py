import re
from dataclasses import dataclass

@dataclass
class p_term:
  a: float
  p: int
  
def parse(args): 
  return_array = []

  highest_exp = find_highest_exponent(args)
  return_array = prepare_array(highest_exp)
  fill_array(return_array, args, highest_exp)
  return return_array

def extract_coefficient(string):
  match = re.match(r'([+-]?)\s*(\d+(\.\d+)?)', string)
  if match:
      sign = match.group(1)
      coefficient = match.group(2)
      return f"{sign}{coefficient}"
  return None

def fill_array(return_array, expression, h_exp):
  neg = 1
  terms = split_terms(expression)
  for term in terms:
    if term[0] ==  '=':
      neg = -1
      if (term[1] != None):
        term = term.replace("= ", "")
    if '^' in term:
      a_part, exponent_part = term.split('^')
      a_part = extract_coefficient(a_part)
      exponent = int(exponent_part)
      a = 0
      if (a_part):
        a = float(a_part)
      return_array[h_exp - exponent].a += a * neg

def prepare_array(highest_exp):
  return_array = []
  for i in range(highest_exp, -1, -1):
    return_array.append(p_term(0, i))
  return return_array
  
def split_terms(expression):
  return re.findall(r'(?:[+\-=]\s?|^)[^+\-=]+', expression)

def find_highest_exponent(expression):
  terms = split_terms(expression)
  exponents = []
  for term in terms:
      if '^' in term:
          _, exponent_part = term.split('^')
          exponent = int(exponent_part)
          exponents.append(exponent)
  if exponents:
      return max(exponents)
  else:
      return 0  # If no exponent is found, return 0 as the highest exponent