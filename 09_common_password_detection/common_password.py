COMMON_PASSWORDS = {
    "password",
    "123456",
    "12345678",
    "123456789",
    "qwerty",
    "qwerty123",
    "abc123",
    "password123",
    "admin",
    "admin123",
    "welcome",
    "letmein",
    "iloveyou"
}


def check_common_password(password):
    password = password.lower().strip()

    if password in COMMON_PASSWORDS:
        return True

    return False


def display_result(password):
    is_common = check_common_password(password)

    print("\n===== COMMON PASSWORD CHECK =====")

    if is_common:
        print("⚠ Password is commonly used.")
        print("Recommendation: Choose a more unique password.")
    else:
        print("✓ Password was not found in the common-password list.")


def main():
    print("===== COMMON PASSWORD DETECTOR =====")

    password = input("Enter your password: ")

    display_result(password)


if __name__ == "__main__":
    main()
