# Q6. Every other sub-list
# Given a list and 2 indices as input, return the sub-list enclosed within these 2 indices. It should
# contain every second element.
# E.g.
# Input f([2,3,5,7,11,13,17,19,23,29,31,37,41], 2, 9)
# Return [5, 11, 17, 23]

def findSubListWithEverySecondElement(list,index1,index2):
    subList = []
    for i in range(index1,index2,2):
        subList.append(list[i])

    return subList

print(findSubListWithEverySecondElement([2,3,5,7,11,13,17,19,23,29,31,37,41], 2, 9))    