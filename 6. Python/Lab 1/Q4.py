
num = int(input())
List = [num]

for i in range(1, int(num/2)+1):
    if num % i == 0:
        List.append(i)

print(sorted(List)) 

