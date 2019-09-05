

from datetime import datetime

presentTime = datetime.now()
print(presentTime)

shortTime = presentTime.strftime('%Y-%m-%d')
print(shortTime)

#now = "2017-01-01"
#nowTime = datetime.strptime(now, '%Y-%m-%d')

now = "2017-01-01 01:02:03"
nowTime = datetime.strptime(now, '%Y-%m-%d %H:%M:%S')
print(nowTime)
