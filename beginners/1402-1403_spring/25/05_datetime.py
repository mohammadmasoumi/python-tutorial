from datetime import datetime, timedelta

print(datetime.utcnow())
print(datetime.now())
print(datetime.now() - timedelta(days=1))
print(datetime.now() + timedelta(days=1))
print(datetime.now() + timedelta(days=1, hours=1))

print(datetime.strftime(datetime.now(), "%Y-%m-%d:%H-%M-%S"))  # datetime -> string
print(
    datetime.strptime("2023-06-15:13-53-46", "%Y-%m-%d:%H-%M-%S")
)  # string -> datetime

print(type(datetime.now()))
