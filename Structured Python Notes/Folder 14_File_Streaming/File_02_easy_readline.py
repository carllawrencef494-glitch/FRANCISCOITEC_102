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