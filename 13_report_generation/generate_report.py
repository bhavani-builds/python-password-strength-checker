from datetime import datetime


SPECIAL_CHARACTERS = "!@#$%^&*()-_=+[]{};:,.?/<>|"

MIN_LENGTH = 8


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
        )
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


def generate_report(
    password,
    result,
    score,
    output_file="password_report.txt"
):
    strength = get_strength(score)

    with open(
        output_file,
        "w",
        encoding="utf-8"
    ) as file:

        file.write("=" * 50 + "\n")
        file.write(
            "       PASSWORD SECURITY REPORT\n"
        )
        file.write("=" * 50 + "\n\n")

        file.write(
            f"Report Generated: "
            f"{datetime.now()}\n\n"
        )

        file.write("PASSWORD ANALYSIS\n")
        file.write("-" * 50 + "\n")

        file.write(
            f"Password Length   : "
            f"{result['length']}\n"
        )

        file.write(
            f"Uppercase         : "
            f"{'Yes' if result['uppercase'] else 'No'}\n"
        )

        file.write(
            f"Lowercase         : "
            f"{'Yes' if result['lowercase'] else 'No'}\n"
        )

        file.write(
            f"Digit             : "
            f"{'Yes' if result['digit'] else 'No'}\n"
        )

        file.write(
            f"Special Character : "
            f"{'Yes' if result['special'] else 'No'}\n"
        )

        file.write("\n")
        file.write("SECURITY SCORE\n")
        file.write("-" * 50 + "\n")

        file.write(
            f"Score    : {score}/5\n"
        )

        file.write(
            f"Strength : {strength}\n"
        )

        file.write("\n")
        file.write("=" * 50 + "\n")
        file.write("End of Report\n")
        file.write("=" * 50 + "\n")

    return output_file


def main():
    print("===== PASSWORD REPORT GENERATOR =====")

    password = input(
        "Enter password to analyze: "
    )

    if not password:
        print("Password cannot be empty.")
        return

    result = analyze_password(password)

    score = calculate_score(result)

    output_file = generate_report(
        password,
        result,
        score
    )

    print(
        f"\nReport generated successfully: "
        f"{output_file}"
    )


if __name__ == "__main__":
    main()
