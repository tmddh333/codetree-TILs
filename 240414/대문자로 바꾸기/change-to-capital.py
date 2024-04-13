lst = [
    list((input().upper()).split())
    for _ in range(5)
]

for i in lst:
    print(' '.join(i))