# Dict comprehension

d = {
    'k1': 'v11',
    'k2': 'v22',
    'k3': 'v31',
    'k4': 'v42',
}

# 'k1' :'v1v1'
print({k: v*2 for k, v in d.items()})

print({k: char + "".join(num)
      for k, (char, *num) in d.items() if int("".join(num)) % 2 == 0})

print({k: char + "".join(num)
      for k, (char, *num) in d.items() if int(num[-1]) % 2 == 0})

_, *num = 'v11'
# _: v
# *num: '11'
# num: ['1', '1']
# a, *b, c = 1, 2, 3, 4

print({k: num for k, (_, *num) in d.items()})
print({k: "".join(num) for k, (_, *num) in d.items()})
# 'k1': ['1', '1'],
print({k: v[1:] for k, v in d.items()})
print({k: v for k, v in d.items() if int(v[-1]) % 2 == 0})