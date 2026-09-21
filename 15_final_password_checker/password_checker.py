import secrets
import string


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
    return {
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


def detect_patterns(password):
    findings = []

    for index in range(len(password) - 1):
        if password[index] == password[index + 1]:
            findings.append(
                "Contains consecutive repeated characters."
            )
            break

    password_lower = password.lower()

    for index in range(len(password_lower) - 2):
        first = ord(password_lower[index])
        second = ord(password_lower[index + 1])
        third = ord(password_lower[index + 2])

        if (
            second == first + 1
            and third == second + 1
        ):
            findings.append(
                "Contains sequential characters."
            )
            break

    return findings


def generate_password(length=12):
    characters = (
        string.ascii_uppercase
        + string.ascii_lowercase
        + string.digits
        + SPECIAL_CHARACTERS
    )

    return "".join(
        secrets.choice(characters)
        for _ in range(length)
    )


def display_analysis(
    result,
    score,
    findings
):
    strength = get_strength(score)

    print("\n" + "=" * 55)
    print("           PASSWORD SECURITY ANALYZER")
    print("=" * 55)

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

    print("-" * 55)

    print(f"Score               : {score}/5")
    print(f"Strength            : {strength}")

    print("\nAdvanced Analysis")

    if findings:
        for number, finding in enumerate(
            findings,
            start=1
        ):
            print(f"{number}. {finding}")
    else:
        print("No obvious repeated or sequential patterns detected.")

    if result["common"]:
        print(
            "\nWarning: This password is in the "
            "common-password list."
        )

    print("=" * 55)


def main():
    while True:
        print("\n" + "=" * 55)
        print("        PYTHON PASSWORD SECURITY TOOL")
        print("=" * 55)

        print("1. Analyze Password")
        print("2. Generate Password")
        print("3. Exit")

        choice = input(
            "\nEnter your choice: "
        ).strip()

        if choice == "1":
            password = input(
                "\nEnter password to analyze: "
            )

            if not password:
                print("Password cannot be empty.")
                continue

            result = analyze_password(password)

            score = calculate_score(result)

            findings = detect_patterns(password)

            display_analysis(
                result,
                score,
                findings
            )

        elif choice == "2":
            try:
                length = int(
                    input(
                        "\nEnter password length: "
                    )
                )
            except ValueError:
                print("Please enter a valid number.")
                continue

            if length < 8:
                print(
                    "Password length must be "
                    "at least 8."
                )
                continue

            password = generate_password(length)

            print("\nGenerated Password:")
            print(password)

        elif choice == "3":
            print(
                "\nThank you for using "
                "Python Password Security Tool!"
            )
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
