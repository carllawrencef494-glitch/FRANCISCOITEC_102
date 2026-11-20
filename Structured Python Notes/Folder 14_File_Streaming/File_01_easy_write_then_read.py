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