# Q10. Of date and days
# Write a func that takes 2 args:
# date - string representing a date in the form of 'yy-mm-dd'
# n - integer
# Returns the string representation of date n days before 'date'
# E.g. f('16-12-10', 11) should return '16-11-29'

from datetime import date,timedelta

def findDate(iDate,numOfDays):
    date1 = iDate.split("-")
    init_date = date(int("20"+date1[0]),int(date1[1]),int(date1[2]))
    ref_date = date(2000,1,1)
    daysFromRef = (init_date-ref_date).days
    reqDate = str(ref_date + timedelta(days=daysFromRef-numOfDays))
    return reqDate[2:len(reqDate)+1]

print(findDate("16-12-10",11))