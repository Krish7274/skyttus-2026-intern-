num1 = float(input("Enter numerator:"))
num2 = float(input("Enter Dominator:"))
try:
    reesult = num1 / num2
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero")


while True:
    try:
        num = int(input("Enter an integer:"))
        print("You entered:", num)
        break
    except ValueError:
        print("Invalid input! Please Enter a valid Integer.")


filename = input("Enter the file name  to open:")
try:
    with open(filename, "r") as file:
        content = file.read()
        print("File content:")
        print(content)
except FileNotFoundError:
    print("Error: The File does not exist.")


try:
    num1 = int(input("Enter numerator:"))
    num2 = int(input("Enter denominator:"))
    result = num1 / num2 
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Invalid input! Please Enter an integer.")
except Exception as e:
    print("An unexpected error occured:", e)


try:
    file = open("sample.txt", "r")
    content = file.read()
    print("File content:")
    print(content)
except FileNotFoundError:
    print("Error: File not found.")
finally:
    print("Closing the file if it was opened...")
    try:
        file.close()
        print("File closed successfully.")
    except NameError:
        print("File was never opened, so nothing to close.")


class InvalidAgeError(Exception):
    pass

age = int(input("Enter your age: "))

try:
    if age < 18:
        raise InvalidAgeError("Age must be 18 or above.")
    print("Access granted. Age is valid.")
except InvalidAgeError as e:
    print("Custom Exception:", e)


numbers = [10, 20, 30, 40, 50]

try:
    index = int(input("Enter an index: "))
    print("Value at index", index, "is", numbers[index])
except IndexError:
    print("Error: Index out of range.")
except ValueError:
    print("Error: Please enter a valid integer index.")


try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    result = num1 / num2
    print("Result of division:", result)

except ValueError:
    print("Error: Invalid input! Please enter numeric values.")

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except Exception as e:
    print("Unexpected error occurred:", e)

else:
    print("Operation completed successfully.")

finally:
    print("Program execution finished.")


import logging

logging.basicConfig(
    filename="error.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 / num2
    print("Result:", result)

except ZeroDivisionError as e:
    logging.error("Division by zero error", exc_info=True)

except ValueError as e:
    logging.error("Invalid input error", exc_info=True)

except Exception as e:
    logging.error("Unexpected error occurred", exc_info=True)


import re

class InvalidEmailError(Exception):
    pass

email = input("Enter your email address: ")

try:
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$"
    
    if not re.match(pattern, email):
        raise InvalidEmailError("Invalid email format.")
    
    print("Email address is valid.")

except InvalidEmailError as e:
    print("Error:", e)


