
"""
Hashing
Hash function
x --hash function --> hash
f=2x-1
"""
import hashlib
password = "2134"
print(hashlib.md5(password.encode('utf-8')).hexdigest())

# save password in db
# username password
# asghar   81dc9bdb52d04dc20036dbd8313ed055


