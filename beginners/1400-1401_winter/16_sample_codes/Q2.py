"""
تمرین دوم

فیلترینگ 

با استفاده از دستور map و filter سعی کنید اعدادی که هم بر ۳ و هم بر ۵ بخش پذیر هستند را فیلتر کنید. ( ورودی همانند تمرین قبلی می‌باشد)

نمونه ورودی:
15 5 30 4 60

نمونه خروجی:
15 30 60
"""

def division_by_15(item):
    return not (item % 15)

print(list(filter(division_by_15, map(int, input().split()))))