"""
در خط اول ابتدا تعداد نمرات دانش آ«وزان را از کاربر دریافت کنید.
در n خط بعدی کاربر نمرات دانش آموزان را برای شما وارد میکند.

نمرات را در یک لیست ذخیره سازی کنید و سپس بیشترین نمره را در خروجی چاپ کنید.
"""

n = int(input())
student_scores = []

for _ in range(n):
    score = int(input())

    if score > 20 or score < 0:
        print("Wrong input!")
    else:
        student_scores.append(score)

# ابتدا بیشترین نمره را ۰ در نظر میگیریم.
max_score = 0

# روی تمام نمرات می چرخیم و اگر نمره ای از ماکسیسمم فعلی بیشتر بود.
# آن نمره را به عنوان ماکسیمم فعلی مد نظر قرار میدهیم.
for score in student_scores:
    if score > max_score:
        max_score = score

print(f"max of student's scores is: {max_score}")
