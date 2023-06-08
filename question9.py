# Q9.
# Write a func that takes 3 args:
# from_date - string representing a date in the form of 'yy-mm-dd'
# to_date - string representing a date in the form of 'yy-mm-dd'
# difference - int
# Returns True if from_date and to_date are less than difference days away from each other, else
# returns False.

from datetime import date

def findNumberOfDays(fDate,sDate,diff):
    date1 = fDate.split("-")
    date2 = sDate.split("-")
    difference = diff

    from_date = date(int("20"+date1[0]),int(date1[1]),int(date1[2]))
    to_date = date(int("20"+date2[0]),int(date2[1]),int(date2[2]))
    date_diff = to_date - from_date

    if date_diff.days < difference:
        return True
    else :
        return False

print(findNumberOfDays("23-05-29","23-06-02",5))

