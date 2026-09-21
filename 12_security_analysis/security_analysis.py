SPECIAL_CHARACTERS = "!@#$%^&*()-_=+[]{};:,.?/<>|"

MIN_LENGTH = 8


def analyze_security(password):
    weaknesses = []
    recommendations = []

    if len(password) < MIN_LENGTH:
        weaknesses.append("Password is too short.")
        recommendations.append(
            "Use at least 8 characters."
        )

    if not any(
        character.isupper()
        for character in password
    ):
        weaknesses.append(
            "No uppercase letter found."
        )
        recommendations.append(
            "Add at least one uppercase letter."
        )

    if not any(
        character.islower()
        for character in password
    ):
        weaknesses.append(
            "No lowercase letter found."
        )
        recommendations.append(
            "Add at least one lowercase letter."
        )

    if not any(
        character.isdigit()
        for character in password
    ):
        weaknesses.append(
            "No digit found."
        )
        recommendations.append(
            "Add at least one number."
        )

    if not any(
        character in SPECIAL_CHARACTERS
        for character in password
    ):
        weaknesses.append(
            "No special character found."
        )
        recommendations.append(
            "Add at least one special character."
        )

    return weaknesses, recommendations


def display_security_analysis(
    weaknesses,
    recommendations
):
    print("\n" + "=" * 50)
    print("           SECURITY ANALYSIS")
    print("=" * 50)

    if not weaknesses:
        print("\n✓ No basic security weaknesses detected.")
    else:
        print("\nWeaknesses:")

        for number, weakness in enumerate(
            weaknesses,
            start=1
        ):
            print(f"{number}. {weakness}")

        print("\nRecommendations:")

        for number, recommendation in enumerate(
            recommendations,
            start=1
        ):
            print(f"{number}. {recommendation}")

    print("=" * 50)


def main():
    print("===== PASSWORD SECURITY ANALYZER =====")

    password = input(
        "Enter password to analyze: "
    )

    if not password:
        print("Password cannot be empty.")
        return

    weaknesses, recommendations = (
        analyze_security(password)
    )

    display_security_analysis(
        weaknesses,
        recommendations
    )


if __name__ == "__main__":
    main()
