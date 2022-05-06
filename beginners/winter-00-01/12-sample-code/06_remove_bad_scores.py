"""
در خط اول ابتدا تعداد نمرات دانش آموزان را از کاربر دریافت کنید.
در n خط بعدی کاربر نمرات دانش آموزان را برای شما وارد میکند.

برای حفظ آبروی مدرسه از شما خواسته شده است تا برنامه ای بنویسید که نمرات کمتر از ۱۰ را از لیست نمرات حذف نماید.
"""

n = int(input())
student_scores = []

for _ in range(n):
    score = int(input())

    if score > 20 or score < 0:
        print("Wrong input!")
    else:
        student_scores.append(score)

# چون همزمان نمیتوانیم روی یک لیست بچرخیم و نمرات رو از اون حذف کنیم.
# مجبور هستیم یک کپی از لیست مون تهیه کنیم و در لیست جدید نمرات را حذف کنیم
good_scores = student_scores.copy()
for score in student_scores:
    if score < 10:
        good_scores.remove(score)

# راه دیگر
# به جای حذف کردن نمرات از یک لیست شما میتوانید نمرات بالای ۱۰ را به یک لیست دیگر اضافه کنید.
good_scores = []
for score in student_scores:
    if score >= 10:
        good_scores.append(score)

print(f"good_scores: {good_scores}")
