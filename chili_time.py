import urllib2
import re
from datetime import datetime 
from datetime import date
from datetime import timedelta
import os

days = ['mon', 'tue', 'wed', 'thu', 'fri']
# Back to monday of this week
today = datetime.today()
monday = today + timedelta(-datetime.today().weekday())
tuesday = monday + timedelta(+1)
wednesday = monday + timedelta(+2)
thursday = monday + timedelta(+3)
friday = monday + timedelta(+4)
startOfWeekDate = monday.strftime('%m-%d-%Y')

github_io_home = os.environ.get('GITHUB_IO_HOME')

f = open(github_io_home + '/projects/chilitime/chilitime.ics', 'w')

f.write('BEGIN:VCALENDAR\n')
f.write('VERSION:2.0\n')
f.write('PRODID:-//www.marudot.com//iCal Event Maker\n')
f.write('X-WR-CALNAME:Chili\n')
f.write('CALSCALE:GREGORIAN\n')
f.write('BEGIN:VTIMEZONE\n')
f.write('TZID:America/Chicago\n')
f.write('TZURL:http://tzurl.org/zoneinfo-outlook/America/Chicago\n')
f.write('X-LIC-LOCATION:America/Chicago\n')
f.write('BEGIN:DAYLIGHT\n')
f.write('TZOFFSETFROM:-0600\n')
f.write('TZOFFSETTO:-0500\n')
f.write('TZNAME:CDT\n')
f.write('DTSTART:19700308T020000\n')
f.write('RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=2SU\n')
f.write('END:DAYLIGHT\n')
f.write('BEGIN:STANDARD\n')
f.write('TZOFFSETFROM:-0500\n')
f.write('TZOFFSETTO:-0600\n')
f.write('TZNAME:CST\n')
f.write('DTSTART:19701101T020000\n')
f.write('RRULE:FREQ=YEARLY;BYMONTH=11;BYDAY=1SU\n')
f.write('END:STANDARD\n')
f.write('END:VTIMEZONE\n')

for day in days:
    response = urllib2.urlopen('http://dining.guckenheimer.com/clients/unionpacific/fss/fss.nsf/weeklyMenuLaunch/5X5QCM~' + startOfWeekDate + '/$file/' + day + '.htm')
    html = response.read()

    # I can put chili sauce on anything. Doesn't count.
    m = re.search('[Cc]hili [Ss]auce', html)
    if (m is not None and m.group(0) is not None):
        continue

    # I had way too many chili macs in the Army. It is ruined on me.
    m = re.search('Chili Mac', html)
    if (m is not None and m.group(0) is not None):
        continue

    # What is this crap? No beef, no chili.
    m = re.search('Chicken Chili', html)
    if (m is not None and m.group(0) is not None):
        continue

    chili_date = monday
    if (day == 'tue'):
      chili_date = tuesday
    elif (day == 'wed'):
      chili_date = wednesday
    elif (day == 'thu'):
      chili_date = thursday
    elif (day == 'fri'):
      chili_date = friday
        

  
    m = re.search('Chili', html)
    if (m is not None and m.group(0) is not None):
        print ('CHILI ' + day.upper() + '!')

        # add event to ical
        f.write('BEGIN:VEVENT\n')
        formatted_date = str(chili_date.strftime('%Y%m%d'))
        f.write('DTSTAMP:' + formatted_date + 'T184832Z\n')
        f.write('UID:' + formatted_date + 'T184832Z-217285625@bdetweiler.github.io\n')
        f.write('DTSTART;VALUE=DATE:' + formatted_date + '\n')
        f.write('DTEND;VALUE=DATE:' + formatted_date + '\n')
        f.write('SUMMARY:Chili today!\n')
        f.write('END:VEVENT\n')

f.write('END:VCALENDAR\n')
f.close() # you can omit in most cases as the destructor will call it

