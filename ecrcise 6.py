import datetime

week_days = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
now = datetime.datetime.now()
day = week_days[now.weekday()] # Note the change to now.weekday()

if day == 'Tuesday':
    print ('yes it is tuesday')
else :
     print ('no')