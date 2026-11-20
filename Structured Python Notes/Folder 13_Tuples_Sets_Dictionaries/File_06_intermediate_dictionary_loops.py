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