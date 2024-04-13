lst1 = [
    list(map(int, input().split()))
    for _ in range(2)
]

lst2 = []
for i in range(len(lst1)):
    lst2.append(str(round(sum(lst1[i]) / len(lst1[i]), 1)))
print(' '.join(lst2))

lst3 = [str(round((x + y) / 2, 1)) for x, y in zip(lst1[0], lst1[1])]
print(' '.join(lst3))

print(str(round((sum(lst1[0]) + sum(lst1[1])) / 8, 1)))