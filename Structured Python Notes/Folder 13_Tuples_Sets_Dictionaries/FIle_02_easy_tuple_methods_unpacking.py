# LEVEL: EASY

numbers = (1, 2, 2, 3, 2, 4)
print(numbers.count(2))     
print(numbers.index(3))     
fruits = ("Apple", "Banana", "Orange")
print(fruits.index("Banana"))   
point = (10, 20)
x, y = point
print("x =", x, "| y =", y)
a, b = 5, 9
a, b = b, a
print(a, b)                 
print("Apple" in fruits)    
for fruit in fruits:
    print("-", fruit)