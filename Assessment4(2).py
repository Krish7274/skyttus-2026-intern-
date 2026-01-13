age = int(input("Enter Your Age:"))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")


marks = float(input("Enter Your Marks:"))
if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
else:
    grade = "C"
print("Your Grade is:", grade)


light = input("Enter traffic light color (Red/Yellow/Green): ").strip().lower()
if light == "red":
    print("Stop")
elif light == "yellow":
    print("wait")
elif light == "green":
    print("Go")
else:
    print("Invalid color! Please Enter Red, Yellow, or Green.")


balance = float(input("Enter your account Balance:"))
withdraw_amount = float(input("Enter the amount to withdraw:"))
if withdraw_amount <= balance:
    balance -= withdraw_amount
    print("Withdrawal Successful!!")
    print("Remaining Balance!!:", balance)
else:
    print("Insufficient balance Transaction Failed.")


num = float(input("Enter a Number:"))
if num > 0:
    print("The Number is Positive:")
elif num < 0:
    print("The Number is Negative:")
else:
    print("The Number is Zero:")


num = float(input("Enter a Number:"))
lower = float(input("Enter The Lower Bound Of the Range:"))
upper = float(input("Enter The Upper Bound Of the Range:"))
if lower <= num <= upper:
    print(f"{num} lies within the rage {lower} to {upper}.")
else:
    print(f"{num} does not lie within the range {lower} to {upper}.")


correct_username = "Patel Krish"
correct_password = "Manavin"
username = input("Enter your username:")
password = input("Enter Your Password:")
if username == correct_username and password == correct_password:
 print("Login Successful!!")
else:
 print("Invalid username  or password.")


units = float(input("Enter The number of units consumed:"))
if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = (100 * 5) + (units - 100) * 7
else:
    bill = (100*5) + (100*7) + (units - 200) * 10
print(f"Electricity bill for {units} units is: {bill}")


num1 = float(input("Enter first number:"))
num2 = float(input("Enter Second number:"))
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
choice = input("Enter choice (1/2/3/4):")
if choice =="1":
    result = num1 + num2
    print(f"Result: {num1} + {num2} = {result}")
elif choice == "2":
    result = num1 - num2
    print(f"Result: {num1} - {num2} = {result}")
elif choice == "3":
    result = num1 * num2
    print(f"Result: {num1} * {num2} = {result}")
elif choice == "4":
    if num2 != 0:
        result = num1 / num2
        print(f"Result: {num1} / {num2} = {result}")
    else:
        print("Error: Division by zero!")
else:
    print("Invalid choice!")


a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))
if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("The triangle is Equilateral.")
    elif a == b or b == c or a == c:
        print("The triangle is Isosceles.")
    else:
        print("The triangle is Scalene.")
else:
    print("The given sides do not form a triangle.")