# asiignment 5

data = {
    "name": "Ali",
    "city": "NY",
    "age": 20
}

# AttributeError: 'dict' object has no attribute 'replace'
# data.replace("city", "location2")
data["location"] = data.pop("city")

print(data)