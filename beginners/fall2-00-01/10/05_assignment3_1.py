"""
سوال سوم:


حسن که دانش آموزان تنبل ولی باهوش است، از شما خواسته است تا برنامه ای بنویسید که به او در حل مسائل ریاضی کند. حسن از شما خواسته که برنامه بنویسید که جمع همه اعداد بین دو عدد داده شده رو بدست بیارد.

نمونه ورودی:
2 10
نمونه خروجی:
54

راهنمایی: از فرمول جمع اعداد بین دو عدد استفاده کنید
"""



"""
a, b

[FORMULA] numbers between: b - a + 1

1, 10 => 10 numbers
2, 10 => 9 numbers


[FORMULA] 

(b + a) * (b - a + 1)
____________________
        2

"""

# use formula
a, b = input().split()

a, b = int(a), int(b)


print((b - a + 1) * (a + b) / 2)


