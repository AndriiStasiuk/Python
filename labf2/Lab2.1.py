with open("text.txt") as file:
    array = [row.strip() for row in file]
print(array)