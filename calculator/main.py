# My calculator
from art import logo
from replit import clear
import time

#Add
def add(n1, n2):
  return n1 + n2
#Substract
def substract (n1, n2):
  return n1 - n2
#Multiply
def multiply (n1,n2):
  return n1 * n2
#Divide
def divide(n1,n2):
  return n1 / n2 

operations = {
  "+":add, 
  "-":substract, 
  "*":multiply, 
  "/":divide
  }

def calculator():
  clear()
  print(logo)
  calc_running = True
  num1 = float(input("Whats the first number?: "))


  while calc_running:
    for symbol in operations:
      print(symbol)
    operation_symbol =input("Pick an operation from the line above: ")
    if operations.get(operation_symbol) is None:
      print("False Operator")
      time.sleep(2)
      calc_running = False
      clear()
      calculator()
    num2 = float(input("Whats the next number?: "))
    answer = operations[operation_symbol](num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    go_on = input(f"Type y to continue with {answer}, r for restart,x for exit\n")
    if go_on == "y":
      clear()
      num1 = answer
      print(f"{num1}")
    elif go_on == "r":
      calc_running = False
      clear()
      calculator()
    else:
      clear()
      calc_running = False
calculator()
