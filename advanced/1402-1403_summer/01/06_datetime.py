from datetime import datetime, timedelta


print(datetime.strptime("1997-03-02", "%Y-%m-%d"))
print(datetime.strftime(datetime.utcnow(), "%Y-%m-%d %H:%M:%S"))

print(datetime.utcnow() - timedelta(days=1))
print(datetime.now() - timedelta(days=1))
print(datetime.now() + timedelta(days=1, hours=12))
