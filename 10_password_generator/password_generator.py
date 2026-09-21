import secrets
import string


def generate_password(length=12):
    characters = (
        string.ascii_uppercase
        + string.ascii_lowercase
        + string.digits
        + "!@#$%^&*"
    )

    password = ""

    for _ in range(length):
        password += secrets.choice(characters)

    return password


def main():
    print("===== PASSWORD GENERATOR =====")

    try:
        length = int(
            input("Enter password length: ")
        )
    except ValueError:
        print("Please enter a valid number.")
        return

    if length < 8:
        print("Password length must be at least 8.")
        return

    password = generate_password(length)

    print("\nGenerated Password:")
    print(password)


if __name__ == "__main__":
    main()
