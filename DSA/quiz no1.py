# Initial library dictionary

library = {
"Python Basics": {"author": "John", "copies": 5},
"AI Guide": {"author": "Sara", "copies": 3}
}

# 1. Add a new book

library["Data Science 101"] = {"author": "Ali", "copies": 7}

# 2. Update copies of "AI Guide"

library["AI Guide"]["copies"] = 5

# 3. Remove books with less than 5 copies

for book, info in list(library.items()):
if info["copies"] < 5:
del library[book]

# 4. Print remaining books

print("Books available in the library:")
for book, info in library.items():
print(f"{book} by {info['author']} - {info['copies']} copies")
