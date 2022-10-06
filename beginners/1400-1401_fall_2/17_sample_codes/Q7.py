student_data = {}

def is_less_than_ten(score):
    return scores < 10

min_all_scores = 21
max_all_scores = -1
students_less_than_ten = []

for _ in range(int(input())):

    first_name = input()
    last_name = input()
    scores = list(map(int, input().split()))
    age = int(input())

    # student key
    student_key = f"{first_name} {last_name}"

    # min and max
    min_score = min(scores)
    max_score = max(scores)

    if min_score < min_all_scores:
        min_all_scores = min_score
    
    if max_score > max_all_scores:
        max_all_scores = max_score
    
    # has less then 10 grade
    less_than_10 = any(map(is_less_than_ten, scores))
    students_less_than_ten.append(student_key) if less_than_10 else None

    info = {
        "first_name": first_name,
        "last_name": last_name, 
        "scores": scores,
        "avg": sum(scores) / len(scores), 
        "min_score": min_score,
        "max_score": max_score,
        "less_than_10": less_than_10,
        "age": age,
    }

    student_data[student_key] = info

print(f"max all scores: {max_all_scores}")
print(f"min all scores: {min_all_scores}")

for item in students_less_than_ten:
    print(item)


