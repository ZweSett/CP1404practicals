MIN_LENGTH = 2
MAX_LENGTH = 6
SPECIAL_CHARS_REQUIRED = True
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print(f"Your password must be between {MIN_LENGTH} and {MAX_LENGTH} characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print(f"\tand 1 or more special characters: {SPECIAL_CHARACTERS}")

    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")

    print(f"Your {len(password)}-character password is valid: {password}")


def is_valid_password(password):
    """Determine if the provided password is valid."""
    # TODO: Check if the length is within the specified range
    if not MIN_LENGTH <= len(password) <= MAX_LENGTH:
        return False

    # TODO: Count lowercase characters
    count_lower = sum(1 for char in password if char.islower())

    # TODO: Count uppercase characters
    count_upper = sum(1 for char in password if char.isupper())

    # TODO: Count digits
    count_digit = sum(1 for char in password if char.isdigit())

    # TODO: Check if any of the 'normal' counts are zero
    if count_lower == 0 or count_upper == 0 or count_digit == 0:
        return False

    # TODO: If special characters are required, check the count of those
    if SPECIAL_CHARS_REQUIRED:
        count_special = sum(1 for char in password if char in SPECIAL_CHARACTERS)
        if count_special == 0:
            return False

    # If we get here (without returning False), then the password must be valid
    return True


main()