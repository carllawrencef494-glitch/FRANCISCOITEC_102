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
