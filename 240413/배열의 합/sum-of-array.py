lst = [
    list(map(int, input().split()))
    for _ in range(4)
]

for lst2 in lst:
    sum = 0
    for i in lst2:
        sum+=i
    print(sum)