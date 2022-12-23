from datetime import datetime, timedelta


class Student:

    def __init__(self, name, birth_date):
        # 2000-12-09 12-12-12
        self.name = name
        self.birth_date = birth_date

    @property
    def age(self):
        now_dt = datetime.utcnow()
        # %H-%M-%S
        birth_dt = datetime.strptime(self.birth_date, "%Y-%m-%d")

        return (now_dt - birth_dt).days // 365

    def __str__(self):
        return f"{name}-{age}"


std1 = Student("bita", "2000-12-9")
# std2 = Student("mina", 23)

print(std1.age)

# from datetime import datetime, timedelta

# print(datetime.utcnow())
# print(datetime.utcnow().year)
# print(datetime.now())
# print(datetime.utcnow() - timedelta(days=1))
# print(datetime.utcnow() - timedelta(days=30))
# print(datetime.utcnow() + timedelta(days=30))
# datetime -> str
# print(datetime.utcnow().strftime("%Y-%m-%d %H-%M-%S"))
# str -> datetime
# print(datetime.strptime("2022-12-15 13-59-15", "%Y-%m-%d %H-%M-%S"))
