"""
سوال ششم:


کارنامه حسن

حسن که پسر زرنگی است از شما خواسته است تا برنامه محاسبه معدل دانشگاه رو تغییر دهید. حسن از شما خواسته است که اگر  اسم دانشجو با حسن شروع شد، معدل نمراتی که بالای ۱۵ (خود ۱۵ شامل نمیشود) هستند را حساب کنید. ( در صورتی که نمره بالای ۱۵ نداشت معدل را ۲۰ محاسبه کنید.

در خط اول ورودی نام و نام خانوادگی دانشجو را از متصدی دریافت کنید.
در خط دوم ( در یک خط) تمام نمرات دانشجو را از متصدی دریافت کنید.

Hassan Hassani

12 13 14 15
 

نمونه خروجی:
20


نمونه ورودی ۲:


AmirHassan Hassani

15 15 12 18
نمونه خروجی ۲:
15

"""
student_name = input()
student_scores = input().split()


if student_name.startswith("Hassan"):
    sum = 0
    numbers_upper_than_15 = 0

    for score in student_scores:
        score = int(score)

        if score > 15:
            sum += score
            numbers_upper_than_15 += 1

    if numbers_upper_than_15 == 0:
        avg = 20
    else:
        avg = sum / numbers_upper_than_15

else:
    sum = 0

    for score in student_scores:
        sum += int(score)

    avg = sum / len(student_scores)

print(avg)