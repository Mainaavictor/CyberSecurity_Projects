import random
import string

def generate_password(length=12):
    if length < 6:
        return "❗ Password length too short. Use at least 6 characters."

    characters = string.ascii_letters + string.digits + string.punctuation + string.whitespace + string.ascii_uppercase + string.ascii_lowercase + string.digits

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def check_strength(password):
    strength = 0
    if any(c.islower() for c in password):
        strength += 1
    if any(c.isupper() for c in password):
        strength += 1
    if any(c.isdigit() for c in password):
        strength += 1
    if any(c in string.punctuation for c in password):
        strength += 1

    if len(password) >= 12 and strength == 4:
        return "🔒 Strong"
    elif len(password) >= 8 and strength >= 3:
        return "🟡 Medium"
    else:
        return "❗ Weak"

def main():
    print("🔐 Password Generator & Strength Checker 🔐\n")

    try:
        length = int(input("Enter desired password length (e.g., 12): "))
        password = generate_password(length)
        print(f"\nGenerated Password: {password}")
        print(f"Strength: {check_strength(password)}")
    except ValueError:
        print("❗ Please enter a valid number.")

if __name__ == "__main__":
    main()
# This code generates a random password and checks its strength.
# It uses a mix of letters, digits, and punctuation for security.
# The strength is evaluated based on character variety and length.
# The user can specify the desired length of the password.
# The program provides feedback on the generated password's strength.
