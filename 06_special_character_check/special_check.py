SPECIAL_CHARACTERS = "!@#$%^&*()-_=+[]{};:,.?/<>|"


def check_special_characters(password):
    special_found = []

    for character in password:
        if character in SPECIAL_CHARACTERS:
            special_found.append(character)

    print("\n===== SPECIAL CHARACTER ANALYSIS =====")

    if special_found:
        print("Contains special character : Yes")
        print(
            "Special characters found   : "
            + " ".join(special_found)
        )
    else:
        print("Contains special character : No")

    return special_found


def main():
    print("===== SPECIAL CHARACTER CHECKER =====")

    password = input("Enter your password: ")

    check_special_characters(password)


if __name__ == "__main__":
    main()
