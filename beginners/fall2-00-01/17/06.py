# assignment 6

data = {
    "asghar": 20, 
    "akbar": 19,
    "hassan": 10
}

# min(values)
print(min(data.values()))
print(min(data.keys()))

min_value = 10000
min_key = ""

for key, value in data.items():
    if value < min_value:
        min_value = value
        min_key = key
        
print(min_key, min_value)