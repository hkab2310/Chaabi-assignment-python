# Q3. Column Sorting, yay!
# Given a list of dicts, write a program to sort the list according to a key given in input.
# E.g.
# Input f([
# {"fruit": "orange", "color": "orange"},
# {"fruit": "apple", "color": "red"},
# {"fruit": "banana", "color": "yellow"},
# {"fruit": "blueberry", "color": "blue"}
# ], "fruit")
# Should Output
# [
# {"fruit": "apple", "color": "red"},
# {"fruit": "banana", "color": "yellow"},
# {"fruit": "blueberry", "color": "blue"},
# {"fruit": "orange", "color": "orange"}
# ]
# AND
# Input f([
# {"fruit": "orange", "color": "orange"},
# {"fruit": "apple", "color": "red"},
# {"fruit": "banana", "color": "yellow"},
# {"fruit": "blueberry", "color": "blue"}
# ], "color")
# Should Output
# [
# {"fruit": "blueberry", "color": "blue"},
# {"fruit": "orange", "color": "orange"},
# {"fruit": "apple", "color": "red"},
# {"fruit": "banana", "color": "yellow"}
# ]

def sortListByKey(unsortedList,key):
    sortedList = sorted(unsortedList, key=lambda x: x[key])
    return sortedList

unsortedList = [{"fruit": "orange", "color": "orange"},
                {"fruit": "apple", "color": "red"},
                {"fruit": "banana", "color": "yellow"},
                {"fruit": "blueberry", "color": "blue"}]

print(sortListByKey(unsortedList,"fruit"))
