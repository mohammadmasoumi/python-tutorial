"""
در خط اول از کاربر تعداد نمرات دانش آموزان را دریافت کنید.
سپس در n خط بعدی نمرات دانش آموزان را از کاربر دریافت کنید و میانگین نمرات رو در خروجی نمایش دهید.
"""

n = int(input())
student_scores = []

for _ in range(n):
    score = int(input())

    if score > 20 or score < 0:
        print("Wrong input!")
    else:
        student_scores.append(score)

# جمع نمرات داشن آموزان
scores_sum = 0
for score in student_scores:
    scores_sum += score

# بدین صورت هم می توانید نمرات را جمع کنید
# scores_sum = sum(student_scores)

print(f"students avg is: {scores_sum / n}")
