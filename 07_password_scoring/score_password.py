SPECIAL_CHARACTERS = "!@#$%^&*()-_=+[]{};:,.?/<>|"
MIN_LENGTH = 8


def calculate_score(password):
    score = 0

    if len(password) >= MIN_LENGTH:
        score += 1

    if any(character.isupper() for character in password):
        score += 1

    if any(character.islower() for character in password):
        score += 1

    if any(character.isdigit() for character in password):
        score += 1

    if any(
        character in SPECIAL_CHARACTERS
        for character in password
    ):
        score += 1

    return score


def display_score(password, score):
    print("\n===== PASSWORD SCORE =====")

    print(f"Password length : {len(password)}")
    print(f"Score           : {score}/5")

    print("\nScore details:")

    if len(password) >= MIN_LENGTH:
        print("✓ Minimum length")
    else:
        print("✗ Minimum length")

    if any(character.isupper() for character in password):
        print("✓ Uppercase letter")
    else:
        print("✗ Uppercase letter")

    if any(character.islower() for character in password):
        print("✓ Lowercase letter")
    else:
        print("✗ Lowercase letter")

    if any(character.isdigit() for character in password):
        print("✓ Digit")
    else:
        print("✗ Digit")

    if any(
        character in SPECIAL_CHARACTERS
        for character in password
    ):
        print("✓ Special character")
    else:
        print("✗ Special character")


def main():
    print("===== PASSWORD SCORING SYSTEM =====")

    password = input("Enter your password: ")

    score = calculate_score(password)

    display_score(password, score)


if __name__ == "__main__":
    main()
