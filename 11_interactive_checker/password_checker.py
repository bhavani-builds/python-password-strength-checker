SPECIAL_CHARACTERS = "!@#$%^&*()-_=+[]{};:,.?/<>|"

MIN_LENGTH = 8

COMMON_PASSWORDS = {
    "password",
    "123456",
    "12345678",
    "123456789",
    "qwerty",
    "qwerty123",
    "abc123",
    "password123",
    "admin",
    "admin123",
    "welcome",
    "letmein",
    "iloveyou"
}


def analyze_password(password):
    result = {
        "length": len(password),
        "uppercase": any(
            character.isupper()
            for character in password
        ),
        "lowercase": any(
            character.islower()
            for character in password
        ),
        "digit": any(
            character.isdigit()
            for character in password
        ),
        "special": any(
            character in SPECIAL_CHARACTERS
            for character in password
        ),
        "common": password.lower().strip()
        in COMMON_PASSWORDS
    }

    return result


def calculate_score(result):
    score = 0

    if result["length"] >= MIN_LENGTH:
        score += 1

    if result["uppercase"]:
        score += 1

    if result["lowercase"]:
        score += 1

    if result["digit"]:
        score += 1

    if result["special"]:
        score += 1

    return score


def get_strength(score):
    if score <= 1:
        return "Very Weak"

    if score == 2:
        return "Weak"

    if score == 3:
        return "Medium"

    if score == 4:
        return "Strong"

    return "Very Strong"


def display_analysis(result, score):
    strength = get_strength(score)

    print("\n" + "=" * 45)
    print("         PASSWORD ANALYSIS")
    print("=" * 45)

    print(
        f"Length              : "
        f"{result['length']}"
    )

    print(
        f"Uppercase           : "
        f"{'Yes' if result['uppercase'] else 'No'}"
    )

    print(
        f"Lowercase           : "
        f"{'Yes' if result['lowercase'] else 'No'}"
    )

    print(
        f"Digit               : "
        f"{'Yes' if result['digit'] else 'No'}"
    )

    print(
        f"Special Character   : "
        f"{'Yes' if result['special'] else 'No'}"
    )

    print(
        f"Common Password     : "
        f"{'Yes' if result['common'] else 'No'}"
    )

    print("-" * 45)

    print(f"Score               : {score}/5")
    print(f"Strength            : {strength}")

    print("=" * 45)


def main():
    print("=" * 45)
    print("      PYTHON PASSWORD STRENGTH CHECKER")
    print("=" * 45)

    password = input(
        "\nEnter password to analyze: "
    )

    if not password:
        print("Password cannot be empty.")
        return

    result = analyze_password(password)

    score = calculate_score(result)

    display_analysis(
        result,
        score
    )


if __name__ == "__main__":
    main()
