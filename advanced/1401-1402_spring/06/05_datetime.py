
from datetime import datetime, timedelta

# current datetime
print(datetime.now()) # local time
print(datetime.utcnow()) # utc time

# timedelta inputs
# days=0, seconds=0, microseconds=0,milliseconds=0, minutes=0, hours=0, weeks=0
print(datetime.now() - timedelta(days=1))
print(datetime.now() - timedelta(hours=1))
print(datetime.now() - timedelta(weeks=1))

# diff
twenty_six_years_ago = datetime.utcnow() - timedelta(days=26 * 365)
# year, month=None, day=None, hour=0, minute=0, second=0, microsecond=0 
twenty_six_years_ago2 = datetime(year=1996, month=3, day=2)
yesterday = datetime.utcnow() - timedelta(days=1)
now = datetime.utcnow()

print(now - yesterday)
print((now - yesterday).days)
print((now - twenty_six_years_ago).days // 365)
print((now - twenty_six_years_ago2).days // 365)
