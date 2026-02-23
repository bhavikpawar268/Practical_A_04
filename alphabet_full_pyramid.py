# Full Pyramid using Alphabets

letters = ["A", "B", "C", "D", "E"]

for i in range(len(letters), 0, -1):
    print(" " * (len(letters) - i), end="")
    for j in range(i):
        print(letters[j], end=" ")
    print()