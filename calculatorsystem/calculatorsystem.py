
# ==========================================
# Simple Calculator using Python Functions
# Forked and Enhanced by Sania Irshad
# Original Project by: shumaila1823
# ==========================================

# Arithmetic operation functions

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

# Main calculator function
def calculator():
    print("🔢 Welcome to Simple Calculator")
    print("-------------------------------")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    print("5. Power")
    print("6. Modulus")
    print("Q. Quit")
    
    while True:
        choice = input("Enter choice (1/2/3/4/5/6 or Q to quit): ")
        
        if choice.lower() == 'Q':
            print("Exiting calculator. Goodbye!")
            break

        if choice not in ['1', '2', '3', '4','5','6']:
            print("Invalid input. Please choose 1-6 or 'Q' to quit.")
            continue

        try:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
        except ValueError:
            print("❌ Please enter valid numeric values.")
            continue

        if choice == '1':
            result = add(num1, num2)
            print(f"✅ Result: {num1} + {num2} = {result}")
        elif choice == '2':
            result = subtract(num1, num2)
            print(f"✅ Result: {num1} - {num2} = {result}")
        elif choice == '3':
            result = multiply(num1, num2)
            print(f"✅ Result: {num1} * {num2} = {result}")
        elif choice == '4':
            print(f"Result: {divide(num1, num2)}")
        elif choice == '5':
                result = power(num1, num2)
                op = '^'
        elif choice == '6':
                result = modulus(num1, num2)
                op = '%'
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    calculator()
