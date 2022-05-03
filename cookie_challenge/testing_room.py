from firstcookie import FirstCookie
from datetime import date, datetime, timedelta

TIME_IN_SECONDS = 10
TIME_IN_MINUTES = 0

firstcookie = FirstCookie()

now = datetime.now() + timedelta(minutes=TIME_IN_MINUTES, seconds=TIME_IN_SECONDS)
print(now)

while datetime.now() < now :
    firstcookie.clickerloop(10)
    
firstcookie.close()
print(datetime.now())