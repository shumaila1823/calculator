
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

def power(x, y):
    return x ** y

def modulus(x, y):
    return x % y

def logarithm(x, base):
    """Return log of x with specified base."""
    if x <= 0 or base <= 0:
        return "Error! Logarithm undefined for zero or negative numbers."
    return math.log(x, base)

def sine(x):
    return math.sin(math.radians(x))

def factorial(x):
    """Return the factorial of a number."""
    if x < 0:
        return "Error! Factorial is not defined for negative numbers."
    return math.factorial(x) return math.cos(math.radians(x))

def tangent(x):
    return math.tan(math.radians(x))

def calculator():
    history = []


# Main calculator function
def calculator(): 
    print("🔢 Welcome to Advance Calculator")
    print("-------------------------------")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Modulus")
    print("7. Logarithm")
    print("8. Sine")
    print("9. Cosine")
    print("10. Tangent")
    print("Q. Quit")
    
    while True:
        choice = input("Enter choice (1/2/3/4/5/6/7/8/9/10 or Q to quit): ")
        
        if choice.lower() == 'Q':
            print("Exiting calculator. Goodbye!")
            break
      

        if choice not in ['1', '2', '3', '4','5','6','7','8','9','10']:
            print("Invalid input. Please choose 1-10 or 'Q' to quit.")
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
        elif choice == '7':
            try:
                base = int(input("Enter base for logarithm (e.g., 10 or e=2.718...): "))
                result = logarithm(num1, base)
                print(f"✅ Result: log base {base} of {num1} = {result}")
            except ValueError:
                print("❌ Invalid base value.")
        elif choice in ['8', '9', '10']:
            try:
                angle = float(input("Enter angle in degrees: "))
            except ValueError:
                print("Invalid input. Please enter a numeric angle.")
                continue

            if choice == '8':
                result = sine(angle)
                op = f"sin({angle})"
            elif choice == '9':
                result = cosine(angle)
                op = f"cos({angle})"
            elif choice == '10':
                result = tangent(angle)
                op = f"tan({angle})"

            print(f"Result: {result}")
            history.append(f"{op} = {result}")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    calculator()
