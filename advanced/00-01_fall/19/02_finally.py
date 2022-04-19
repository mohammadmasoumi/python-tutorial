"""
try:
    pass

except:
    pass

else:  # optional
    pass

finally:  # optional
    # clean up
    pass
"""

#           file name file mode
# w r +wb +w a(append)

# a => append at the end
# w => override

# run finally anyway

# 1.
"""
1. raise exception in try
2. execute except block
3. if exception raises in except block(catch the exception)
4. execute finally block
5. re-raise exception
"""

# 2.
"""
1. raise exception in try
2. execute except block
3. if exception does not raise in except block(catch the exception)
4. execute finally block
"""

try:
    # resource descriptor
    # open
    # connect to db
    print("try")
    file = open("file.txt", "a")
    raise FileExistsError

except Exception as exec:
    print("except")
    raise exec

else:
    print("else")

finally:
    print("finally")
    file.close()
