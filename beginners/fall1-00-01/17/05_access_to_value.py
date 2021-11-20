d = {
    "name": "ali",
    "lastname": "karimi",
    "nationality": "Iran",
    "country": "Iran",
    # "country": "USA",
}

print(d["name"])
print(d["country"])
# print(d["city"])  # KeyError: 'city'

# dictionary.get(key, default value)
print(d.get("city"))  # does not throw exception
print(d.get("city", "Varamin"))  # if key does not exist, return default value
print(d.get("country", "Varamin"))  # if key exist, return value
print(d["nationality"])
print(d["country"])
