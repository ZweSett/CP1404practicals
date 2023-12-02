MENU = "(G)et a valid score (must be 0-100 inclusive)\n(P)rint result\n(S)how stars\n(Q)uit"
print(MENU)
choice = input(">>> ").upper()


def main(choice):
    while choice != "Q":
        if choice == "G":
            score = get_user_score()
        elif choice == "P":
            result = determine_result(score)

            if result is not None:
                print(f"Your result: {result}")
        elif choice == "S":
            print("*" * score)
        elif choice == "Q":
            print("Farewell.")
        else:
            print("Invalid Choice.")
        print(MENU)
        choice = input(">>> ").upper()


def get_user_score():
    try:
        score = int(input("Enter your score: "))
        if score < 0 or score > 100:
            print("Invalid Score")
            return None
        return score
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return None


def determine_result(score):
    if score is None:
        return None  # Invalid score
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main(choice)
