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

# 3.
"""
execute try section
execute else block (if exception did not raise)
execute finally
"""

try:
    # resource descriptor
    # open
    # connect to db
    print("try")
    file = open("file.txt", "a")
    # raise FileExistsError

except Exception as exec:
    print("except")
    raise exec

else:
    print("else")

finally:
    # clean up
    print("finally")
    file.close()
