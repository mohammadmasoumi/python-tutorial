# replace key

d = {
    'name': 'asghar',
    'shahr': 'varamin'
}

oldkey = 'shahr'
newkey = 'city'
# asghar -> manchester
# shahr -> city

# d.update(city=d.pop(oldkey))
# d.update({newkey: d.pop(oldkey, oldkey)})
update_dict = {newkey: d.pop(oldkey, oldkey)}
d.update(update_dict)

print(d)
