def check_digits(password):
    has_digit = False

    for character in password:
        if character.isdigit():
            has_digit = True
            break

    print("\n===== DIGIT ANALYSIS =====")

    if has_digit:
        print("Contains digit : Yes")
    else:
        print("Contains digit : No")

    return has_digit


def main():
    print("===== PASSWORD DIGIT CHECKER =====")

    password = input("Enter your password: ")

    check_digits(password)


if __name__ == "__main__":
    main()
