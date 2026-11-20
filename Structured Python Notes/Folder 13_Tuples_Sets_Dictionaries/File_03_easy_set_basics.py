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
