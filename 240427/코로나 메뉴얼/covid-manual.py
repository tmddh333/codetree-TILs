count = 0
for i in range(3):
    status, degree = input().split()
    if status == 'Y' and int(degree) >= 37:
        count+=1
    else:
        continue

if count >= 2:
    print('E')
else:
    print('N')