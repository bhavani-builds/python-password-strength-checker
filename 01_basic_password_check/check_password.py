def check_password(password):
    if password:
        print("Password entered successfully.")
    else:
        print("Password cannot be empty.")


def main():
    print("===== PASSWORD CHECKER =====")

    password = input("Enter your password: ")

    check_password(password)


if __name__ == "__main__":
    main()
