import datetime

def getFirst(day1,day2):
    if(day2>=day1):
        return day2-day1
    return 7+day2-day1

def GetDates(date1, date2, dayOf):
    date1 = datetime.datetime.strptime(date1,"%d.%m.%y")
    date2 = datetime.datetime.strptime(date2,"%d.%m.%y")
    dist = getFirst(date1.weekday(),dayOf)
    start = date1.toordinal()
    finish = date2.toordinal()
    res  = []
    for x in range(start+dist,finish,7):
        res.append(datetime.date.fromordinal(x).strftime('%d.%m.%Y'))
    return res