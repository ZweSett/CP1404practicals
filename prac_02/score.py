import random


def main():
    user_score = get_user_score()
    result = determine_result(user_score)

    if result is not None:
        print(f"Your result: {result}")

    # Generate a random score between 0 and 100
    random_score = random.randint(0, 100)
    print(f"Random score: {random_score}")

    # Use the determine_result function for the random score
    random_result = determine_result(random_score)

    if random_result is not None:
        print(f"Result for random score: {random_result}")


def get_user_score():
    try:
        score = float(input("Enter your score: "))
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


main()
