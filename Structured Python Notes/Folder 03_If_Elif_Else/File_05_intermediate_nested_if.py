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