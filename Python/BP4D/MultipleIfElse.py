One = int(input("Type a number between 1 and 10: "))
Two = int(input("Type a number between 1 and 10: "))

if (One >= 1) and (One <= 10):
    if (Two >= 1) and (Two <= 10):
        print("You seret number is:", One * Two)
    else:
        print("Incorrect second value!")
else:
    print("Incorrect first value!")
