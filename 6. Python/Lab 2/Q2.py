# program to count the number of characters (character frequency) in a string.

String = input("Enter a string: ")

Char = input("Enter a character: ")

Count = 0
for i in String.lower():
    if i == Char.lower():
        Count += 1

print("The character", Char, "appears", Count)