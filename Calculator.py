print("Select an operation to perform")
print("1. ADD")
print("2. SUBTRACT")
print("3. MULTIPLY")
print("4. DIVIDE")

operation = input()

if operation == "1":
    num1 = float(input("Enter First Number: "))
    num2 = float(input("Enter Second Number: "))
    result = num1+num2
    print("Sum =", result)

elif operation == "2":
      num1 = float(input("Enter First Number: "))
      num2 = float(input("Enter Second Number: "))
      result = num1-num2
      print("Subtraction =", result)

elif operation == "3":
      num1 = float(input("Enter First Number: "))
      num2 = float(input("Enter Second Number: "))
      result = num1*num2
      print("Product =", result)

elif operation == "4":
      num1 = float(input("Enter First Number: "))
      num2 = float(input("Enter Second Number: "))
      result = num1/num2
      print("Quotient = ", result)

else:
    print("Invalid Entry")