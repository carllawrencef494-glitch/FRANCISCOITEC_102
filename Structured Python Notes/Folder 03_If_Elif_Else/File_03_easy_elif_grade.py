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