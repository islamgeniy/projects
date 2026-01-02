import math

# function to add two numbers
def addNumbers(a, b):
    return a+b

# function to subtract two numbers
def subtractNumbers(a, b):
    return a-b

# function to multiply two numbers
def multiplyNumbers(a, b):
    return a*b

# function to divide two numbers
def divideNumbers(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a/b

def main():
    print("Basic Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        choice = input("Enter choice (1/2/3/4): ")

        if choice in ['1', '2', '3', '4']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(f"{num1} + {num2} = {addNumbers(num1, num2)}")

            elif choice == '2':
                print(f"{num1} - {num2} = {subtractNumbers(num1, num2)}")

            elif choice == '3':
                print(f"{num1} * {num2} = {multiplyNumbers(num1, num2)}")

            elif choice == '4':
                print(f"{num1} / {num2} = {divideNumbers(num1, num2)}")
        else:
            print("Invalid Input")

        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            break
    
if __name__ == "__main__":
    main()