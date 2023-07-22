# exception handling

"""
connect to DB

cursor = conn.cursor()
cursor.execute()
"""

"""
try
    code ...
except exception
    handle
    recover

"""

try:
    # critical code
    pass

except Exception:
    pass


"""
try:
    code with probability of exception
except:
    handle exception
else:
    if doesn't throw exception
finally:
    run anyway
"""

