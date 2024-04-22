a, b, c = map(int, input().split())
d = min(a, b, c)

r1 = 1 if a == d else 0
r2 = 1 if (a == b and b == c) else 0

print(r1, r2, end=" ")