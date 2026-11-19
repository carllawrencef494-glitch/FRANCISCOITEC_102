# LEVEL: EASY
age = 20
if age >= 18:
    print("You are an adult.")

number = -5
if number < 0:
    print("The number is negative.")

temperature = 35
if temperature > 30:
    print("It is hot today!")

print("Program finished.")


# LEVEL: EASY
age = 16
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

number = 7
if number % 2 == 0:
    print(number, "is even")
else:
    print(number, "is odd")

password = "python123"
if password == "python123":
    print("Access granted")
else:
    print("Access denied")


# LEVEL: EASY
score = 87

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score: {score} -> Grade: {grade}") 
number = 0
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")


# LEVEL: INTERMEDIATE
number = 15
if number > 0:
    print("Positive")
if number % 3 == 0:
    print("Divisible by 3")
if number % 5 == 0:
    print("Divisible by 5")
age = 25
has_license = True
if age >= 18 and has_license:
    print("You can drive.")

day = "Sunday"
if day == "Saturday" or day == "Sunday":
    print("Weekend!")

is_raining = False
if not is_raining:
    print("No umbrella needed.")


# LEVEL: INTERMEDIATE
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed.")
    else:
        print("Valid ID required.")
else:
    print("You must be at least 18 years old.")
username = "admin"
password = "1234"

if username == "admin":
    if password == "1234":
        print("Login successful")
    else:
        print("Wrong password")
else:
    print("User not found")


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


# LEVEL: HARD
a, b, c = 3, 4, 5
if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        kind = "equilateral"
    elif a == b or b == c or a == c:
        kind = "isosceles"
    else:
        kind = "scalene"
    print(f"Valid triangle ({kind})")
else:
    print("Not a valid triangle")


x, y = -3, 4
if x > 0 and y > 0:
    print("Quadrant I")
elif x < 0 and y > 0:
    print("Quadrant II")
elif x < 0 and y < 0:
    print("Quadrant III")
elif x > 0 and y < 0:
    print("Quadrant IV")
else:
    print("On an axis")

a, b, c = 1, -4, 4
discriminant = b ** 2 - 4 * a * c
if discriminant > 0:
    print("Two real roots")
elif discriminant == 0:
    print("One real root")
else:
    print("No real roots")


# LEVEL: HARD
def ticket_price(age, day, is_student, is_member):
    if age < 3:
        return 0
    elif age <= 12:
        price = 120
    elif age < 60:
        price = 220
    else:
        price = 150

    # weekday vs weekend
    if day in ("Saturday", "Sunday"):
        price += 30
    elif day == "Wednesday":
        price -= 40        

    if is_member and is_student:
        price *= 0.70
    elif is_member:
        price *= 0.85
    elif is_student:
        price *= 0.80

    return round(price, 2)

customers = [
    ("Ana", 2, "Friday", False, False),
    ("Ben", 10, "Sunday", False, False),
    ("Cathy", 20, "Wednesday", True, False),
    ("Dan", 35, "Saturday", False, True),
    ("Ella", 65, "Monday", False, True),
    ("Fred", 19, "Friday", True, True),
]

total = 0
for name, age, day, student, member in customers:
    p = ticket_price(age, day, student, member)
    total += p
    print(f"{name:6} age {age:>2} {day:10} -> P{p:>7.2f}")
print(f"Total sales: P{total:,.2f}")