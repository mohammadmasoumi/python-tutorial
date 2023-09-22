# {
#     'name': 'asghar',
#     'shahr': 'asghar abad'
# }

# {
#     'name': 'asghar',
#     'city': 'Varamin DC'
# }

d = {
    'name': 'asghar',
    'shahr': 'asghar abad'
}
# rename key
d["city"] = d.pop("shahr")
print(d)

# update
d["city"] = "New Varamin DC (NV)"
print(d)




