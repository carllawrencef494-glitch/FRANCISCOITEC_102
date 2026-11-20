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