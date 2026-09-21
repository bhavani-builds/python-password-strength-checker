def has_repeated_characters(password):
    for index in range(len(password) - 1):
        if password[index] == password[index + 1]:
            return True

    return False


def has_sequential_characters(password):
    password = password.lower()

    for index in range(len(password) - 2):
        first = ord(password[index])
        second = ord(password[index + 1])
        third = ord(password[index + 2])

        if (
            second == first + 1
            and third == second + 1
        ):
            return True

    return False


def check_repeated_pattern(password):
    if len(password) < 4:
        return False

    for size in range(1, len(password) // 2 + 1):
        pattern = password[:size]

        if len(password) % size != 0:
            continue

        repetitions = len(password) // size

        if pattern * repetitions == password:
            return True

    return False


def perform_advanced_analysis(password):
    findings = []

    if has_repeated_characters(password):
        findings.append(
            "Contains consecutive repeated characters."
        )

    if has_sequential_characters(password):
        findings.append(
            "Contains sequential characters."
        )

    if check_repeated_pattern(password):
        findings.append(
            "Contains a repeated pattern."
        )

    return findings


def display_analysis(findings):
    print("\n" + "=" * 55)
    print("          ADVANCED PASSWORD ANALYSIS")
    print("=" * 55)

    if not findings:
        print("\nNo obvious repeated or sequential patterns detected.")
    else:
        print("\nPotential weaknesses:")

        for number, finding in enumerate(
            findings,
            start=1
        ):
            print(f"{number}. {finding}")

    print("=" * 55)


def main():
    print("===== ADVANCED PASSWORD ANALYZER =====")

    password = input(
        "Enter password to analyze: "
    )

    if not password:
        print("Password cannot be empty.")
        return

    findings = perform_advanced_analysis(
        password
    )

    display_analysis(findings)


if __name__ == "__main__":
    main()
