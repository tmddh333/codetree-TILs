a, b, c = map(int, input().split())

if a > b and a < c:
    print(a)
elif b > c and c > a:
    print(c)
else:
    print(b)