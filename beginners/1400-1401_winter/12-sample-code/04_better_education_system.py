"""
در خط اول ابتدا تعداد نمرات دانش آموزان را از کاربر دریافت کنید.
در n خط بعدی کاربر نمرات دانش آموزان را برای شما وارد میکند.

برای اینکه مقابسه درستی از دانش آموزان داشته باشیم، میخواهیم سیستم نمره دهی عددی رو حذف کنیم.
برای همین از شما خواسته شده است تا برنامه ای بنویسید که نمرات دانش آموزان به حروف تبدیل کند.

تغییرات بدین صورت انجام خواهد گرفت:

[17-20] -> A
[14-17) -> B
[11-14) -> C
[8-11) -> D
under 8 -> I will call you daddy!
"""

n = int(input())
student_scores = []

for _ in range(n):
    score = int(input())

    if score > 20 or score < 0:
        print("Wrong input!")
    else:
        student_scores.append(score)

new_student_scores = []
for score in student_scores:
    if 17 <= score <= 20:
        score = "A"
    elif 14 <= score < 17:
        score = "B"
    elif 11 <= score < 14:
        score = "C"
    elif 8 <= score < 11:
        score = "D"
    else:
        score = "I will call your daddy!"

    new_student_scores.append(score)

print(f"new education system scores: {new_student_scores}")