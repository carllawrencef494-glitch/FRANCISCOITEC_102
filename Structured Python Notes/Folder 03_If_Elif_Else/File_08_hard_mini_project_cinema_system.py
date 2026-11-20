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