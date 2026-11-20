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

