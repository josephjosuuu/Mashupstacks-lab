Str = input()
RevStr = ""
for i in range(len(Str)):
    RevStr += Str[-(i+1)]

if RevStr == Str:
    print("Palindrom")
else:
    print("Not Palindrom")