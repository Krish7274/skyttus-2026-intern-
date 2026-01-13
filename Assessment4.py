for i in range(1,11):
    print(i)


num = int(input("Enter a Number:"))
for i in range(1,11):
    print(f"{num}*{i} = {num*i}")


num = int(input("Enter a Number:"))
factorial = 1
for i in range(1,num+1):
    factorial *= i
    print("Factorial of", num, "is",factorial)


n = int(input("Enter The Value of N:"))
a, b = 0, 1
print("Fibonacci sequence:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b


num = int(input("Enter a Number:"))
if num <= 1:
    print(num,"is not a prime number")
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print(num, "is not a prime number")
            break
        else:
            print(num, "is a prime number")


num = int(input("Enter a number:"))
rev = 0
while num > 0:
    digit = num  % 10
    rev = rev * 10 + digit
    num //=10
print("Reversed number:", rev)
    

num = int(input("Enter a number:"))
count = 0 
if num == 0:
    count = 1
else:
    while num != 0:
        count += 1
        num //= 10
print("Number of digits:", count)


total = 0
for i in range(1,101):
    if i % 2 == 0:
        total += i
print("Sum of a even numbers between 1 and 100:", total)


rows = int(input("Enter the number of rows:"))
for i in range(1, rows + 1):
    print(" " * (rows - i), end="")
    print("*" * (2 * i - 1))


num = int(input("Enter a Number:"))
divisors = []
for i in range(1, num + 1):
    if num % i == 0:
        divisors.append(i)
print("Divisors of", num, "are:",divisors)