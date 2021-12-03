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

"""
اکر برنامه در try با خطا مواجه نشود قسمت else اجرا میشود. سپس قسمت finally اجرا میشود.
اگر برنامه با خطا مواجه شود قسمت except اجرا میشود و سپس قسمت finally اجرا میشود.
"""


def get_number():
    try:
        # UnboundLocalError: local variable 'n' referenced before assignment
        n = int(input())
    except ValueError:
        n = 12
        print("Try again!")
    else:
        print("pass")
        return "else"
    finally:
        print("Nice try!")
        # if uncomment this return
        # this return will always execute
        # return "finally"


print(f"res: {get_number()}")
