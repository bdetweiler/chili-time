import urllib2
import re
from datetime import datetime 
from datetime import date
from datetime import timedelta

days = ['mon', 'tue', 'wed', 'thu', 'fri']
# Back to monday of this week
newDate = datetime.today() + timedelta(-datetime.today().weekday())
mondayDateFormat = newDate.strftime('%m-%d-%Y')
for day in days:
    response = urllib2.urlopen('http://dining.guckenheimer.com/clients/unionpacific/fss/fss.nsf/weeklyMenuLaunch/5X5QCM~' + mondayDateFormat + '/$file/' + day + '.htm')
    html = response.read()

    m = re.search('Chili', html)
    if (m is not None and m.group(0) is not None):
        print ('CHILI ' + day.upper() + '!')
