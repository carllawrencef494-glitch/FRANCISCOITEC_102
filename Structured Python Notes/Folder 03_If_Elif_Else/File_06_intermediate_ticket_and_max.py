# LEVEL: INTERMEDIATE
age = 12
if age < 5:
    price = 0
elif age <= 12:
    price = 80
elif age < 60:
    price = 150
else:
    price = 100
print(f"Age {age} ticket price: P{price}")

a, b, c = 14, 29, 21
if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c
print("Largest of three:", largest)      # 29

letter = "e"
if letter.lower() in "aeiou":
    print(letter, "is a vowel")
else:
    print(letter, "is a consonant")