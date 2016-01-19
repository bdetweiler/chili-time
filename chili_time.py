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

    m = re.search('Chili', html)
    if (m is not None and m.group(0) is not None):
        print ('CHILI ' + day.upper() + '!')
        # BEGIN:VCALENDAR
        # VERSION:2.0
        # PRODID:-//www.marudot.com//iCal Event Maker
        # X-WR-CALNAME:Chili
        # CALSCALE:GREGORIAN
        # BEGIN:VTIMEZONE
        # TZID:America/Chicago
        # TZURL:http://tzurl.org/zoneinfo-outlook/America/Chicago
        # X-LIC-LOCATION:America/Chicago
        # BEGIN:DAYLIGHT
        # TZOFFSETFROM:-0600
        # TZOFFSETTO:-0500
        # TZNAME:CDT
        # DTSTART:19700308T020000
        # RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=2SU
        # END:DAYLIGHT
        # BEGIN:STANDARD
        # TZOFFSETFROM:-0500
        # TZOFFSETTO:-0600
        # TZNAME:CST
        # DTSTART:19701101T020000
        # RRULE:FREQ=YEARLY;BYMONTH=11;BYDAY=1SU
        # END:STANDARD
        # END:VTIMEZONE
        # BEGIN:VEVENT
        # DTSTAMP:20160106T184832Z
        # UID:20160106T184832Z-217285625@marudot.com
        # DTSTART;VALUE=DATE:20160106
        # DTEND;VALUE=DATE:20160106
        # SUMMARY:Chili
        # END:VEVENT
        # END:VCALENDAR

