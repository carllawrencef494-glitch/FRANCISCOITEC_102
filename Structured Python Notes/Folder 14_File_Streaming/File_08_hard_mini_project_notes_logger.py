# LEVEL: HARD
import os

FILENAME = "journal.txt"

def add_entry(text):
    with open(FILENAME, "a") as f:
        f.write(text + "\n")

def view_entries():
    try:
        with open(FILENAME) as f:
            for number, line in enumerate(f, start=1):
                print(f"{number}. {line.strip()}")
    except FileNotFoundError:
        print("No entries yet.")

def search(keyword):
    with open(FILENAME) as f:
        return [line.strip() for line in f if keyword.lower() in line.lower()]

def statistics():
    lines = words = 0
    with open(FILENAME) as f:
        for line in f:
            lines += 1
            words += len(line.split())
    return lines, words

view_entries()              
add_entry("Studied Python file handling")
add_entry("Finished the list comprehension notes")
add_entry("Practice Python for the final project")

print("--- All entries ---")
view_entries()
print("--- Search 'python' ---")
print(search("python"))
lines, words = statistics()
print(f"--- {lines} entries, {words} words ---")

os.remove(FILENAME)