# LEVEL: INTERMEDIATE
import os

with open("students.txt", "w") as file:
    file.write("Student: Alice\nStudent: Bob\nStudent: Charlie\n")


with open("students.txt", "r") as file:
    for number, line in enumerate(file, start=1):
        print(f"{number}. {line.strip()}")

print("File closed automatically?", file.closed)     

os.remove("students.txt")
