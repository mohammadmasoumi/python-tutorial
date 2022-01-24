sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}

# min value
print(min(sample_dict.values()))

# who has the min value?
min_key = None
min_value = 10000

for key in sample_dict:
    value = sample_dict[key]

    if value < min_value:
        min_value = value
        min_key = key

print(f"{min_key}: {min_value}")

