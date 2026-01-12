text = input("Enter a String:")
length = len(text)

print("Length of the string:", length)


sentence = input("Enter a sentence:")
print(sentence.lower())

text = input("Enter a string:")
print(text.replace(" ","_"))


text = input("Enter a string:")

first_char = text[0]
last_char = text[-1]
print("First character:", first_char)
print("Last character:", last_char)


text = input("Enter a string:")
reversed_text = text[::-1]
print("Reversed string:", reversed_text)


text = input("Enter a string:")
letter = input("Enter a letter to count:")
count = text.count(letter)
print("The letter appears", count,"times")


sentence = input("Enter a sentence:")
word = input("Enter a word to search:")
if word in sentence:
    print("The word is present in the sentence.")
else:
    print("The word is NOT present in the sentence.")


name = input("Enter your name:")
age = input("Enter your age:")
print(f"Your name is {name} and you are {age} years old.")


text = input("Enter a string:")
clean_text = text.strip()
print("String after removing extra space:", clean_text)               






favourite_movies = [
    "3 idiots",
    "sholay",
    "Lagaan",
    "Drishyam",
    "Dangal"
]
print(favourite_movies)


movies = ["3 idiots","sholay","Lagaan","Drishyam","Dangal"]
new_movie = input("Enter a new movie name:")
movies.append(new_movie)
print("Updated movie list:",movies)


movies = ["3 idiots","sholay","Lagaan","Drishyam","Dangal"]
movies.pop(0)
print("Updated movie list:",movies)


numbers = [5,2,9,1,7]
numbers.sort()
print("Sorted list:", numbers)


numbers = [1,2,3,4,5]
numbers.reverse()
print("Reversed list:",numbers)


numbers = [10,25,7,55,65]
largest = max(numbers)
print("Largest number:", largest)


list1 = [1,2,3]
list2 = [4,5,6]
merged_list = list1 + list2
print("Merged list:", merged_list)


items = [10,20,30,40,50]
last_item = items[-1]
print("Last element:", last_item)


nested_list = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
element = nested_list[1][2]
print("Accessed element:", element)


items = [1,2,2,3,5,4,4,6,7]
element = int(input("Enter the element to count"))
count = items.count(element)
print("The element appears", count, "times")