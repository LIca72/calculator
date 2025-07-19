# calculator.py

try:
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    operation = input("Choose operation (+, -, *, /, ^): ")

    result = None

    if operation == '+':
        result = a + b
    elif operation == '-':
        result = a - b
    elif operation == '*':
        result = a * b
    elif operation == '/':
        result = a / b
    elif operation == '^':
        result = a ** b
    else:
        print("⚠️ Unknown operation.")

except ZeroDivisionError:
    print("🚫 You can't divide by zero.")
except ValueError:
    print("❗ Please enter valid numbers.")
else:
    if result is not None:
        print(f"✅ Result: {result}")
finally:
    print("🔚 Program finished.")
