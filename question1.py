# Q1. Get your basics right - Implement selection sort algorithm in python. The function accepts a
# list in the input and returns a sorted list.
# E.g.
# Input f1([5,416,54,21,6135,15,741]) should
# Return [5, 15, 21, 54, 416, 741, 6135]

import math

def selectionSort(unsortedList):
    for i in range(0,len(unsortedList)):
        min = math.inf
        minIndex = i
        for j in range(i+1,len(unsortedList)):
            if min > unsortedList[j]:
                min = unsortedList[j]
                minIndex = j
        # print("min",min)
        # print("minIndex",minIndex)
        # print(unsortedList)
        if unsortedList[i] > min:
             temp = unsortedList[i]
             unsortedList[i] = min
             unsortedList[minIndex] = temp
    
    return unsortedList


print(selectionSort([0,-5,250,7895,-89745]))
