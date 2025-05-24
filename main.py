# Ask the user to enter a number.
number = int(input("Enter a number: "))

# Check if the number is Even or Odd.
if number % 2 == 0:
    print(str(number) + " is an Even Number.")
else:
    print(str(number) + " is an Odd Number.")