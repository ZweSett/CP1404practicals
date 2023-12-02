"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
    A ValueError will occur if the user enters a value that cannot be converted to an integer, such as a non-numeric input.

2. When will a ZeroDivisionError occur?
    A ZeroDivisionError will occur if the user enters a denominator of zero.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
    Yes, the code has been modified to check if the denominator is zero before performing the division. If the denominator is zero, a ZeroDivisionError is raised with an appropriate message.
By making this change, the code avoids the possibility of a ZeroDivisionError by explicitly checking for a zero denominator.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    # Check if the denominator is zero before performing the division
    if denominator == 0:
        raise ZeroDivisionError("Cannot divide by zero!")

    fraction = numerator / denominator
    print(fraction)

except ValueError:
    print("Numerator and denominator must be valid numbers!")

except ZeroDivisionError as error:
    print(error)

print("Finished.")
