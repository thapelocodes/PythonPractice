try:
    Value1 = int(input("Type the first number: "))
    Value2 = int(input("Type the second number: "))
    Output = Value1 / Value2
except ValueError:
    print("You must type a whole number!")
except KeyboardInterrupt:
    print("You pressed Ctrl+C!")
except ZeroDivisionError:
    print("Attempeted to divide by zero!")
except ArithmeticError:
    print("An undefined error occurred.")
else:
    print(Output)
