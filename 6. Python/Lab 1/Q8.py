import random

lst = range(1,11)

num = random.choice(lst)

while True:
    print("Guess the number: ")
    Gsnum = int(input())

    if Gsnum == num:
        print("Exactly right")
        break
    elif Gsnum > num:
        print("too high")
    else:
        print("too low")
