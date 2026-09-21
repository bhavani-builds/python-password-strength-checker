MIN_LENGTH = 8


def check_password_length(password):
    length = len(password)

    print(f"\nPassword length: {length}")

    if length == 0:
        print("Password cannot be empty.")
        return False

    if length < MIN_LENGTH:
        print(
            f"Password is too short. "
            f"Minimum length is {MIN_LENGTH} characters."
        )
        return False

    print("Password length is acceptable.")
    return True


def main():
    print("===== PASSWORD LENGTH CHECKER =====")

    password = input("Enter your password: ")

    check_password_length(password)


if __name__ == "__main__":
    main()
