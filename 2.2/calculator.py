print("Hello! Im a calculator! Wanna calc something?")

print("Enter a number:\n")
number1 = int(input())
print("Enter an operator:\n")
operator = input()
print("Enter another number:\n")
number2 = int(input())

if operator == "+":
  print((number1) + (number2))
elif operator == "-":
  print((number1) - (number2))
elif operator == "*":
  print((number1) * (number2))
elif operator == "/":
  print((number1) / (number2))
else:
  print("Thats not a valid operator")
