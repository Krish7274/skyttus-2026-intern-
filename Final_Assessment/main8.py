# Write a program to calculate the difference between two dates. 

from datetime import date

y1 = int(input("Enter year of first date: "))
m1 = int(input("Enter month of first date: "))
d1 = int(input("Enter day of first date: "))

y2 = int(input("Enter year of second date: "))
m2 = int(input("Enter month of second date: "))
d2 = int(input("Enter day of second date: "))

date1 = date(y1, m1, d1)
date2 = date(y2, m2, d2)

diff = date2 - date1

print("Difference in days:", diff.days)
