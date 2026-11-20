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
