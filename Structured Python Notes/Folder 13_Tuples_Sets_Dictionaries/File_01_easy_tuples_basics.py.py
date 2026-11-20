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