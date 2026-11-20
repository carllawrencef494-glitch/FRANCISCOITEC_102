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