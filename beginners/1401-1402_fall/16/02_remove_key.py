dict1 = {"k1": "v1", "k2": "v2"}

value = dict1.pop("k1")
default_value = dict1.pop("k10", "DEFAULT_VALUE")

# KeyError: 'k20'
del dict1["k20"]

# --------------------------------------------
dict2 = {
    "k1": {
        "k2": {
            "k3": {
                "k4": [{"k5": ({"k6": "FINDME"})}]
            }
        }
    },
    "k6": "Hello"
}
print(dict2["k6"])

# {'k2': {'k3': {'k4': [{'k5': {'k6': 'FINDME'}}]}}}
print(dict2["k1"])
# {'k3': {'k4': [{'k5': {'k6': 'FINDME'}}]}}
print(dict2["k1"]["k2"])
# {'k4': [{'k5': {'k6': 'FINDME'}}]}
print(dict2["k1"]["k2"]["k3"])
# [{'k5': {'k6': 'FINDME'}}]
print(dict2["k1"]["k2"]["k3"]["k4"])
# {'k5': {'k6': 'FINDME'}}
print(dict2["k1"]["k2"]["k3"]["k4"][0])
# {'k6': 'FINDME'}
print(dict2["k1"]["k2"]["k3"]["k4"][0]["k5"])
# FINDME
print(dict2["k1"]["k2"]["k3"]["k4"][0]["k5"]["k6"])

print(dict2.get("k1", {}).get("k2", {})["k3"]["k4"][0]["k5"]["k6"])

