#dit is een programma wat laat zien hoe datum- en tijd functies werken in Python

from datetime import datetime

#datetime.now() geeft de huidige datum
now = datetime.now()

#er zijn andere functies
year = now.year
month = now.month
day = now.day

hour = now.hour
minute = now.minute
second = now.second

#we kunnen het ook anders weergeven
print "%s-%s-%s" % (now.year, now.month, now.day)
print "%s:%s:%s" % (now.hour, now.minute, now.second)
