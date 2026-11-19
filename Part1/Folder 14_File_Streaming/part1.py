# LEVEL: EASY
import os

file = open("message.txt", "w")
file.write("Hello\n")
file.write("Welcome to Python.\n")
file.close()                    

file = open("message.txt", "r")
content = file.read()
file.close()

print(content)
print("Characters:", len(content))

os.remove("message.txt")        


# LEVEL: EASY
import os

with open("poem.txt", "w") as f:
    f.write("Line one\nLine two\nLine three\n")

file = open("poem.txt", "r")
print(file.readline())          
print(file.readline())          
print(file.readline().strip())  
print(repr(file.readline()))   
file.close()

os.remove("poem.txt")


# LEVEL: EASY
import os

with open("fruits.txt", "w") as f:
    f.write("Apple\nBanana\nOrange\nMango\n")

file = open("fruits.txt", "r")
lines = file.readlines()
file.close()

print(lines)                    
print("Number of lines:", len(lines))
for line in lines:
    print("-", line.strip())

os.remove("fruits.txt")


# LEVEL: INTERMEDIATE
import os

with open("notes.txt", "w") as f:
    f.write("First note\n")

with open("notes.txt", "a") as f:       
    f.write("Second note\n")
    f.write("Third note\n")

with open("notes.txt", "r") as f:
    print(f.read())

with open("notes.txt", "w") as f:       
    f.write("Only this remains\n")

with open("notes.txt") as f:            
    print(f.read())

os.remove("notes.txt")


# LEVEL: INTERMEDIATE
import os

with open("students.txt", "w") as file:
    file.write("Student: Alice\nStudent: Bob\nStudent: Charlie\n")


with open("students.txt", "r") as file:
    for number, line in enumerate(file, start=1):
        print(f"{number}. {line.strip()}")

print("File closed automatically?", file.closed)     

os.remove("students.txt")


# LEVEL: INTERMEDIATE
import os

n = 5
with open("numbers.txt", "w") as f:
    for i in range(1, n + 1):
        f.write(f"{i * 10}\n")

line_count = 0
total = 0
with open("numbers.txt") as f:
    for line in f:
        line_count += 1
        total += int(line)

print("Lines:", line_count)             
print("Sum:", total)                    
print("Average:", total / line_count)   

with open("numbers.txt") as f:
    print([int(line) for line in f])  

os.remove("numbers.txt")


# LEVEL: HARD
import os

with open("source.txt", "w") as f:
    f.write("python is fun\nfiles are useful\nstreaming saves memory\n")

with open("source.txt") as src, open("copy.txt", "w") as dst:
    for number, line in enumerate(src, start=1):
        dst.write(f"{number}: {line.upper()}")

with open("copy.txt") as f:
    print(f.read())

with open("source.txt") as f:
    lines = [line.strip() for line in f]
print("Total words:", sum(len(line.split()) for line in lines))
print("Longest line:", max(lines, key=len))


try:
    with open("does_not_exist.txt") as f:
        print(f.read())
except FileNotFoundError:
    print("Error: the file was not found.")

os.remove("source.txt")
os.remove("copy.txt")


# LEVEL: HARD
import os

FILENAME = "journal.txt"

def add_entry(text):
    with open(FILENAME, "a") as f:
        f.write(text + "\n")

def view_entries():
    try:
        with open(FILENAME) as f:
            for number, line in enumerate(f, start=1):
                print(f"{number}. {line.strip()}")
    except FileNotFoundError:
        print("No entries yet.")

def search(keyword):
    with open(FILENAME) as f:
        return [line.strip() for line in f if keyword.lower() in line.lower()]

def statistics():
    lines = words = 0
    with open(FILENAME) as f:
        for line in f:
            lines += 1
            words += len(line.split())
    return lines, words

view_entries()              
add_entry("Studied Python file handling")
add_entry("Finished the list comprehension notes")
add_entry("Practice Python for the final project")

print("--- All entries ---")
view_entries()
print("--- Search 'python' ---")
print(search("python"))
lines, words = statistics()
print(f"--- {lines} entries, {words} words ---")

os.remove(FILENAME)