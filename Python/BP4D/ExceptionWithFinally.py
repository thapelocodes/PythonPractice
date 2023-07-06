import sys
try:
    ##raise ValueError
    print("Raising an exception.")
except ValueError:
    print("ValueError Exception!")
    sys.exit()
finally:
    print("Takine care of last minute details.")

print("This code will never execute.")
