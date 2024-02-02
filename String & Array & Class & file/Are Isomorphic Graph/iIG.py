# -*- coding: utf-8 -*-

def bubbleSort(arr):
	n = len(arr)
	for i in range(n-1):
		for j in range(0, n-i-1):
			if arr[j] > arr[j + 1] :
				arr[j], arr[j + 1] = arr[j + 1], arr[j]


# create matrix for 1. graph

n = int(input("1. graph kaç elemanlı : "))

matrix = []

for i in range(n):
    temp = []
    for j in range(n):
        x = int(input("Is there a connection between"+chr(65+i)+" and "+chr(65+j)+"; yes (1), no (0) = "))
        temp.append(x)
    matrix.append(temp)

# create matrix for 2. graph

n = int(input("\n2. graph kaç elemanlı : "))

matrix2 = []

for i in range(n):
    temp = []
    for j in range(n):
        x = int(input("Is there a connection between"+chr(65+i)+" and "+chr(65+j)+"; yes (1), no (0) = "))
        temp.append(x)
    matrix2.append(temp)

# create ranklist for 1. graph

rankList = []

for i in range(n):
    rank=0
    for j in range(n):
        if(1==matrix[i][j]):
            rank+=1
            if(i==j):
                rank+=1
    rankList.append(rank)

# create ranklist for 2. graph

rankList2 = []

for i in range(n):
    rank=0
    for j in range(n):
        if(1==matrix2[i][j]):
            rank+=1
            if(i==j):
                rank+=1
    rankList2.append(rank)


# Control

cond=True
bubbleSort(rankList)
bubbleSort(rankList2)
    
if(len(rankList)==len(rankList2)):
    for i in range(len(rankList)):
        if(rankList[i]!=rankList2[i]):
            cond=False
else:
    cond=False


if(cond):
    print("\nIsomorphic")
else:
    print("\nNOT Isomorphic")


