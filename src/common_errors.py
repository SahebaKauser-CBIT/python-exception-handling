
# Examples of Common Python Errors

# 1. ValueError
try:
    age = int("hello")
except ValueError:
    print("ValueError handled: Invalid integer value.")

# 2. ZeroDivisionError
try:
    result = 10 / 0
except ZeroDivisionError:
    print("ZeroDivisionError handled: Cannot divide by zero.")

# 3. IndexError
try:
    numbers = [10, 20, 30]
    print(numbers[5])
except IndexError:
    print("IndexError handled: List index is out of range.")

# 4. KeyError
try:
    student = {"name": "Saheba", "age": 21}
    print(student["grade"])
except KeyError:
    print("KeyError handled: Dictionary key does not exist.")

print("All examples executed successfully.")
