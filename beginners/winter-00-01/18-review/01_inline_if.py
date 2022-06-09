# inline-if

true_condition = True

if true_condition:
    value = 1
else:
    value = 0

"""
variable = true_value if condition else false_value   

usage:
    lambda function
    map
    filter

if condition:
    variable = true_value
else:
    variable = false_value
"""
# value = value_if_condition_is_true if condition else value_if_condition_is_false
value = 1 if true_condition else 0
value = 12 if true_condition else None

print(value)



