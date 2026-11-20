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
