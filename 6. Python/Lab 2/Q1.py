from itertools import permutations

strng = permutations(("a","e","i","o","u"))

for i in strng:
    print("".join(i))