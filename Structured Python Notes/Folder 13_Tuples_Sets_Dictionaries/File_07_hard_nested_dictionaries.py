# LEVEL: HARD
students = {
    "Ana":   {"age": 19, "grades": [92, 88, 95]},
    "Ben":   {"age": 20, "grades": [70, 65, 78]},
    "Cathy": {"age": 19, "grades": [85, 90, 82]},
}

for name, info in students.items():
    average = sum(info["grades"]) / len(info["grades"])
    status = "Passed" if average >= 75 else "Failed"
    print(f"{name:6} age {info['age']} avg {average:.1f} {status}")

students["Dan"] = {"age": 21, "grades": [88, 91, 79]}      
students["Ben"]["grades"].append(80)                          

best = max(students, key=lambda n: sum(students[n]["grades"]) / len(students[n]["grades"]))
print("Top student:", best)

products = [
    {"name": "Mouse", "price": 350, "stock": 10},
    {"name": "Keyboard", "price": 900, "stock": 0},
    {"name": "Monitor", "price": 5400, "stock": 4},
]
in_stock = [p["name"] for p in products if p["stock"] > 0]
print("In stock:", in_stock)

