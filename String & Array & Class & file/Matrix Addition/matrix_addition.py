# -*- coding: utf-8 -*-

#1. matrix
#1 3 5
#2 4 1
#1 5 7
#
#2. matrix
#3 3 4
#2 4 1
#3 5 4
#
#
#
# expected result
#4 6 9
#4 8 2
#4 10 11

x = [[1,3,5],[2,4,1],[1,5,7]]

y = [[3,3,4],[2,4,1],[3,5,4]]

result = [[0,0,0],[0,0,0],[0,0,0]]

result[0][0] = x[0][0]+y[0][0]
result[0][1] = x[0][0]+y[0][0]
result[0][2] = x[0][0]+y[0][0]
result[1][0] = x[0][0]+y[0][0]
result[1][1] = x[0][0]+y[0][0]
result[1][2] = x[0][0]+y[0][0]
result[2][0] = x[0][0]+y[0][0]
result[2][1] = x[0][0]+y[0][0]
result[2][2] = x[0][0]+y[0][0]

for i in range(len(x)):
    for j in range(len(y)):
        result[i][j] = x[i][j]+y[i][j]
        
for list1 in result:
    for num in list1:
        print(str(num), end="\t")
    print()

