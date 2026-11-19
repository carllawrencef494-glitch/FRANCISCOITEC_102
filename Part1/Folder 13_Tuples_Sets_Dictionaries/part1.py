# LEVEL: EASY
colors = ("red", "green", "blue")
print(colors)               
print(colors[0])            
print(colors[-1])           
print(colors[0:2])          
print(len(colors))          

mixed = ("Ana", 19, True)   
print(mixed)

single = ("hello",)         
print(type(single))

try:
    colors[0] = "yellow"
except TypeError as error:
    print("Error:", error)


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


# LEVEL: EASY
numbers = {1, 2, 3, 3, 2, 1}
print(numbers)              
votes = ["Ana", "Ben", "Ana", "Cathy", "Ben", "Ana"]
unique_voters = set(votes)
print(unique_voters)
print("Unique candidates:", len(unique_voters))  

fruits = {"apple", "banana"}
fruits.add("mango")
fruits.add("apple")         
print(sorted(fruits))       
fruits.remove("banana")
fruits.discard("grapes")   
print(sorted(fruits))

print("mango" in fruits) 


# LEVEL: INTERMEDIATE
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1 | set2)          
print(set1 & set2)          
print(set1 - set2)          
print(set1 ^ set2)          


python_class = {"Ana", "Ben", "Cathy", "Dan"}
web_class = {"Cathy", "Dan", "Ella"}

print("Both classes:", sorted(python_class & web_class))
print("Python only:", sorted(python_class - web_class))
print("All students:", sorted(python_class | web_class))
print("Is subset?", {"Ana", "Ben"}.issubset(python_class))     


# LEVEL: INTERMEDIATE
student = {
    "name": "Alice",
    "age": 20
}

print(student["name"])              
print(student.get("course"))        
print(student.get("course", "N/A")) 

student["age"] = 21                 
student["course"] = "Computer Science"  
print(student)

del student["age"]                  
print(student)

print("name" in student)            
print(len(student)) 


# LEVEL: INTERMEDIATE
prices = {"coffee": 120, "tea": 80, "juice": 95}

print(list(prices.keys()))      
print(list(prices.values()))    

for item, price in prices.items():
    print(f"{item.title():8} P{price}")

print("Total:", sum(prices.values()))
print("Most expensive:", max(prices, key=prices.get))


word = "banana"
counts = {}
for letter in word:
    counts[letter] = counts.get(letter, 0) + 1
print(counts)       


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


# LEVEL: HARD
text = "the quick brown fox jumps over the lazy dog the fox"
frequency = {}
for word in text.split():
    frequency[word] = frequency.get(word, 0) + 1

ranked = sorted(frequency.items(), key=lambda pair: pair[1], reverse=True)
print("Top 3 words:", ranked[:3])

inventory = {
    "apple":  {"price": 15, "qty": 50},
    "banana": {"price": 10, "qty": 80},
    "mango":  {"price": 40, "qty": 20},
}

def sell(item, amount):
    if item not in inventory:
        return f"{item} not found"
    if inventory[item]["qty"] < amount:
        return f"Not enough {item}"
    inventory[item]["qty"] -= amount
    return f"Sold {amount} {item} = P{amount * inventory[item]['price']}"

print(sell("apple", 10))
print(sell("mango", 25))
print(sell("grapes", 1))
print("Remaining:", {name: data["qty"] for name, data in inventory.items()})

visitors = ["ana", "ben", "ana", "cathy", "ben", "dan"]
print("Unique visitors:", len(set(visitors)))

locations = [("Manila", 14.60, 120.98), ("Cebu", 10.31, 123.89)]
for city, lat, lon in locations:
    print(f"{city}: {lat}, {lon}")