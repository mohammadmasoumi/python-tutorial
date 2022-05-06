"""
در خط اول ابتدا تعداد نمرات دانش آموزان را از کاربر دریافت کنید.
در n خط بعدی کاربر نمرات دانش آموزان را برای شما وارد میکند.

از شما خواسته شده است تا دومین بیشترین نمره را در بین نمرات پیدا کنید.

به عنوان نمونه:
4
19
20
20
18

در نمونه ورودی بالا عدد ۱۹ دومین بزرگترین عدد می‌باشد.
___________________________________________________________
نمونه ورودی و خروجی
4
20
20
19
18
max_score: 20,  before_max_score: 19

"""

n = int(input())
student_scores = []

for _ in range(n):
    score = int(input())

    if score > 20 or score < 0:
        print("Wrong input!")
    else:
        student_scores.append(score)

max_score, before_max_score = 0, 0
for score in student_scores:
    if score > max_score:
        before_max_score = max_score
        max_score = score
        # max_score, before_max_score = score, max_score

    if before_max_score < score < max_score:
        before_max_score = score

print(f"max_score: {max_score},  before_max_score: {before_max_score}")
