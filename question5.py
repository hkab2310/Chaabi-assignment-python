# Q5. Common, Not Common
# Given 2 lists in input. Write a program to return the elements, which are common to both
# lists(set intersection) and those which are not common(set symmetric difference) between the
# lists.
# Input:
# Mainstream = ["One Punch Man","Attack On Titan","One Piece","Sword
# Art Online","Bleach","Dragon Ball Z","One Piece"]
# must_watch = ["Full Metal Alchemist","Code Geass","Death
# Note","Stein's Gate","The Devil is a Part Timer!","One Piece","Attack
# On Titan"]
# f(mainstream, must_watch) should return:
# ["One Piece", "Attack On Titan"], ["Dragon Ball Z", "Death Note",
# "One Punch Man", "Stein's Gate", "The Devil is a Part Timer!", "Sword
# Art Online","Full Metal Alchemist","'Bleach", "Code Geass"]

def findCommonAndRest(list1,list2):
    common = []
    rest = []
    for i in range(0,len(list1)):
        if list2.count(list1[i])>0:
            if common.count(list1[i])==0:
                common.append(list1[i])
        else :
            rest.append(list1[i])

    for i in range(0,len(list2)):
        if common.count(list2[i])==0:
            rest.append(list2[i])

    return common,rest

mainstream = ["One Punch Man","Attack On Titan","One Piece","SwordArt Online","Bleach","Dragon Ball Z","One Piece"]
must_watch = ["Full Metal Alchemist","Code Geass","Death Note","Stein's Gate","The Devil is a Part Timer!","One Piece","Attack On Titan"]


print(findCommonAndRest(mainstream,must_watch))        