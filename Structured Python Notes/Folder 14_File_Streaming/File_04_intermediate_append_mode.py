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
