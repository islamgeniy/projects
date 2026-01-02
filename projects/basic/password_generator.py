import random

# function to generate a random password
def generate_password(length=12):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")
    try:
        length = int(input("Enter desired password length (default is 12): "))
        if length <= 0:
            print("Length should be a positive integer. Using default length of 12.")
            length = 12
    except ValueError:
        print("Invalid input. Using default length of 12.")
        length = 12

    password = generate_password(length)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()