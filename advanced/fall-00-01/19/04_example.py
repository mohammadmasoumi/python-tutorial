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

while True:

    try:
        n = int(input())
    except ValueError:
        print("Try again!")
    else:
        print("pass")
        break
    finally:
        print("Nice try!")
