b, a = map(int, input().split())

if b % 2 == 1:
    for i in range(b, a-1, -2):
        print(i, end=" ")
else:
    for i in range(b, a-1, -2):
        print(i, end=" ")