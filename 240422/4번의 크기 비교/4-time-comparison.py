a = int(input())
lst = list(map(int, input().split()))

for i in lst:
    print(1) if a > i else print(0)