numbers = (10,20,30,40,50)
print(numbers)


numbers = (10,20,30,40,50)
third_element = numbers[2]
print("Third element:", third_element)


numbers = (10,20,30)
a,b,c = numbers
print("a=",a)
print("b=",b)
print("c=",c)


fruits = {"apple", "banana", "mango", "orange", "grapes"}
print(fruits)


fruits = {"apple", "banana", "mango", "orange", "grapes"}
new_fruit = input("Enter a new fruit to add:")
fruits.add(new_fruit)
print("updated set of fruits:", fruits)


fruits = {"apple", "banana", "mango", "orange", "grapes"}
fruit_to_remove = input("Enter the fruit to remove:")
fruits.discard(fruit_to_remove)
print("Updated set of fruits:", fruits)


set1 = {"apple", "banana", "mango"}
set2 = {"orange", "grapes", "banana"}
union_set = set1.union(set2)
print("union of sets:", union_set)


list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
intersection = [item for item in list1 if item in list2]
print("intersaction of the list:", intersection)


set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
if set1.issubset(set2):
    print("set1 is a subset of set2")
else:
    print("set1 is not subset of set2")


numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers)
print("List after removing duplicates:", unique_numbers)




students = {
    "Krish": 85,
    "Meet": 92,
    "Aryan": 78,
    "Yash": 90,
    "Nisarg": 88
}
print(students)


students = {
    "Krish": 85,
    "Meet": 92,
    "Aryan": 78
}
students["David"] = 90
print("Updated dictionary:", students)


students = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 90
}
del students["Charlie"]
print("Updated dictionary:", students)


dict1 = {"Alice": 85, "Bob": 92}
dict2 = {"Charlie": 78, "David": 90}
dict1.update(dict2)
print("Merged dictionary:", dict1)


students = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78
}
key_to_check = input("Enter the key to check:")
if key_to_check in students:
    print(f"the key '{key_to_check}' exists in the dictionary.")
else:
    print(f"the key '{key_to_check}' does NOT exists in the dictionary.")


text = input("Enter a string:")
words = text.split()
word_freq={}
for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1
print("Word frequency:", word_freq)


students = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 90
}
max_key = max(students,key=students.get)
print("Key with maximum value:", max_key)
print("Maximum value:", students[max_key])


students = {
    "Krish": 85,
    "Meet": 92,
    "Aryan": 78
}
reversed_dict = {value: key for key, value in students.items()}
print("Reversed dictionary:", reversed_dict)


students = {
    "Krish": 85,
    "Meet": 92,
    "Aryan": 78
}
key_to_update = input("Enter the key to update:")
new_value = int(input("Enter the new value:"))
if key_to_update in students:
    students[key_to_update] = new_value
    print("updated dictionary:", students)
else:
    print(f"the key '{key_to_update}' does not exist.")


tuple_list = [("Krish",83), ("Meet",92),("Yash",42)]
student_dict = dict(tuple_list)

print("Dictionary:", student_dict)
