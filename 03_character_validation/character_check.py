def check_characters(password):
    has_letter = False
    has_digit = False
    has_special = False

    special_characters = "!@#$%^&*()-_=+[]{};:,.?/"

    for character in password:
        if character.isalpha():
            has_letter = True

        elif character.isdigit():
            has_digit = True

        elif character in special_characters:
            has_special = True

    print("\n===== CHARACTER ANALYSIS =====")

    print(f"Contains letters  : {'Yes' if has_letter else 'No'}")
    print(f"Contains digits   : {'Yes' if has_digit else 'No'}")
    print(
        f"Contains special  : "
        f"{'Yes' if has_special else 'No'}"
    )

    return has_letter, has_digit, has_special


def main():
    print("===== PASSWORD CHARACTER CHECKER =====")

    password = input("Enter your password: ")

    check_characters(password)


if __name__ == "__main__":
    main()
