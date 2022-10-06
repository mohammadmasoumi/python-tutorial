d = {
    'name': 'ali',
    'last_name': 'alavi'
}

# update
key = 'name'

d.update(name='hassan')
d['name'] = 'hassan'
d[key] = 'hassan'

# add
# 'father_name': 'abbas'
# print(d)
# اگر کلید باید مقدار آن را آپدیت میکند. در صورتی که کلید نباشد اضافه میکند.
key2 = 'father_name'

d['father_name'] = 'abbas'
d[key2] = 'abbas'
d.update(father_name='abbas')

print(d)
