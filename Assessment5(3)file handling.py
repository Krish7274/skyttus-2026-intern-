#1-Write a program to read a file and display its contents.
file = open("sample.txt", "w")
file.write("Hello")
file.close()
file = open("sample.txt", "r")
conent = file.read()
print(conent)
file.close()

#2-Write a program to count the number of lines in a file.
file = open("sample.txt","r")
lines = file.readlines()
print("Number of lines:",len(lines))
file.close()

#3-Write a program to count how many times each word appears in a file.
file = open("sample.txt","r")
words = file.read().split()
file.close()
words_count = {}
for word in words:
    words_count[word] = words_count.get(word, 0) + 1
    
    print(words_count)


# 4-Write a program to write 5 user-entered sentences to a file.
file = open("sentences.txt", "w")
for i in range (1,6):
    sentence = input(f"enter sentence {i}:")
    file.write(sentence + "\n")
file.close()
print()

# 5- Write a program to append a list of strings to an existing file..
strings = [
    "Apple",
    "Banana",
    "Mango",
    "Orange"
    ]
file_path = "example.txt"
with open(file_path,"a") as file:
    for line in strings:
        file.write(line + "\n")

# 6 - Write a program to read a file and print only lines containing a specific word..
word = "python"
with open("word.txt","r") as file:
    for line in file:
        if word in line:
            print(line.strip())

# 7 - Write a program to replace a specific word in file and save changes..
old_word = "python"
new_word = "Java"
file_path = "word.txt"
with open(file_path,"r") as file:
    content = file.read()
content = content.replace(old_word, new_word)
with open(file_path, "w") as file:
    file.write(content)

# 8 - Write a program to merge the contents of two text files into a third file..
file1 = "file1.txt"
file2 = "file2.txt"
file3 = "merged.txt"
with open(file1, "r") as f1, open(file2,"r") as f2, open(file3, "w") as f3:
    f3.write(f1.read())
    f3.write("\n")
    f3.write(f2.read())

# 9 - Write a program to read a CSV file and Display its content in a formatted way..
import csv
file_name = "data.csv"
with open(file_name, "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print("{:<15} {:<15} {:<15}".format(*row))

# 10 - Write a Program to backup a file by copying its contents into another file..
source_file = "original.txt"
backup_file = "backup.txt"
with open(source_file, "r") as src:
    content =  src.read()
with open(backup_file, "w") as backup:
    backup.write(content)