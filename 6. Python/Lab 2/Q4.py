# program to count repeated characters in a string.

String = input("Enter a string: ")

print("The repeated characters in the string are:")
for i in String:
    if String.count(i) > 1:
        print(i, String.count(i))