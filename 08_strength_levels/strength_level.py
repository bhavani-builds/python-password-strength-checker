def get_strength_level(score):
    if score <= 1:
        return "Very Weak"

    elif score == 2:
        return "Weak"

    elif score == 3:
        return "Medium"

    elif score == 4:
        return "Strong"

    else:
        return "Very Strong"


def display_strength(score):
    strength = get_strength_level(score)

    print("\n===== PASSWORD STRENGTH =====")
    print(f"Score    : {score}/5")
    print(f"Strength : {strength}")


def main():
    print("===== PASSWORD STRENGTH LEVEL =====")

    score = int(
        input("Enter password score (0-5): ")
    )

    if score < 0 or score > 5:
        print("Invalid score. Enter a value from 0 to 5.")
        return

    display_strength(score)


if __name__ == "__main__":
    main()
