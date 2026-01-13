#1
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
     if n % 1 == 0:
       return False
    return True
num = int(input("Enter a number:"))
if is_prime(num):
    print("Prime number")
else:
    print("Not a prime number")

#2
def reverse_string(s):
    reversed_str = ""
    for ch in s:
        reversed_str = ch + reversed_str
    return reversed_str
text = input("Enter a string:")
print(reverse_string(text))

#3
def factorial(n):
    result = 1 
    for i in range(1, n + 1):
        result *= i
    return result
num = int(input("Enter a number:"))
print("Factorial:", factorial(num))

#4
def simple_interest(principle, rate, time):
    return (principle * rate * time) / 100
p = float(input("Enter Principle amount:"))
r = float(input("Enter rate of interest:"))
t = float(input("Enter Time in years:"))
si = simple_interest(p, r, t)
print("Simple Interest:", si)

#5
def is_palindrome(word):
    return word == word[::-1]
text = input("Enter a word:")
if is_palindrome(text):
    print("Palindrome")
else:
    print("Not a Palindrome")

#6
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in s:
        if ch in vowels:
            count += 1
    return count
text = input("Enter a string:")
print("Number of vowels:", count_vowels(text))

#7
def merge_lists(list1, list2):
    return list1 + list2
list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged = merge_lists(list1, list2)
print("Merged list:", merged)

#8
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
num1 = int(input("Enter First Number:"))
num2 = int(input("Enter Second Number:"))
print("GCD:", gcd(num1, num2))

#9
def rectangle_area(length, width):
    return length * width
l = float(input("Enter Length of the rectangle:"))
w = float(input("ENter width of the rectangle:"))
print("Area of the rectangle:", rectangle_area(l, w))

#10
def is_armstrong(number):
    num_str = str(number)
    num_digits = len(num_str)
    total = sum(int(digit) ** num_digits for digit in num_str)
    return total == number
num = int(input("Enter a number:"))
if is_armstrong(num):
    print(num, "is an Armstrong number")
else:
    print(num, " is not an Armstrong number")