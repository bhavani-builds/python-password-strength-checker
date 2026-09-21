def check_letter_case(password):
    has_uppercase = False
    has_lowercase = False

    for character in password:
        if character.isupper():
            has_uppercase = True

        elif character.islower():
            has_lowercase = True

    print("\n===== LETTER CASE ANALYSIS =====")

    print(
        f"Uppercase letters : "
        f"{'Yes' if has_uppercase else 'No'}"
    )

    print(
        f"Lowercase letters : "
        f"{'Yes' if has_lowercase else 'No'}"
    )

    return has_uppercase, has_lowercase


def main():
    print("===== PASSWORD CASE CHECKER =====")

    password = input("Enter your password: ")

    check_letter_case(password)


if __name__ == "__main__":
    main()
