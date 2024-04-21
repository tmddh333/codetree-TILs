lst = input().split()

[(print('even') if int(i) % 2 == 0 else print('odd')) for i in lst]