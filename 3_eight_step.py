
n = 3

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

asc = [1, 2, 3, 4, 5, 6, 7, 8]
desc = [8, 7, 6, 5, 4, 3, 2, 1]

for i in range(n):
    if array[i] == asc:
        print ('ascending')
    elif array[i] == desc:
        print ('descending')
    else:
        print ('mixed')
        
