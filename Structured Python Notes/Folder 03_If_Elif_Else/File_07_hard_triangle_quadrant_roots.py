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