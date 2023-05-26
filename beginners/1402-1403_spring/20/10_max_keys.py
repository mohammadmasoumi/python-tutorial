d = {
    'k1': 100,
    'k2': 20,
    'k3': 200,
    'k4': 200
}

max_value = max(d.values())
print([k for k, v in d.items() if v == max_value])
