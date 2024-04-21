a = int(input())

b = 0
if a % 2 == 0:
    b = a / 2

if b % 2 == 1:
    print(int((b + 1) / 2))