from replit import clear

def add(n1, n2):
  return n1 + n2

def sub(n1, n2):
  return n1 - n2 

def div(n1, n2):
  return n1 / n2

def mult(n1, n2):
  return n1 * n2  

calc = {
  "+": add,
  "-": sub,
  "/": div,
  "*": mult
}  

def calcu():

  num1 = float(input("What's the first number? "))
  for i in calc:
    print(i)
  
  
  cont = True
  
  while cont:
    symbol = (input("Pick an operation: "))
    num2 = float(input("What's the next number? "))
    calc_func = calc[symbol]
    res = calc_func(num1, num2)
    print(f"{num1} {symbol} {num2} = {res}")
    if input("Should continue? ") == "y":
      num1 = res
      symbol = ""
    else:
      clear()
      calcu()

calcu()
