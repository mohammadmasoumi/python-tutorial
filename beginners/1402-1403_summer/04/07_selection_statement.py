# Selection statement

# if

"""
# 1.
if (CONDITIONS) {

}

if CONDITIONS:
print("Hello")

if CONDITIONS:
    print("Hello")

indentation

# 2.
if (CONDITIONS) {

} else {

}

if CONDITIONS:
    pass
else:
    pass


# 3.
if (CONDITIONS) {

} else if (CONDITIONS) {
    
} else if (CONDITIONS) {

} else {
    
}

if CONDITIONS:
    pass
elif CONDITIONS:
    pass
else:
    pass

# 4. 
if (CONDITIONS) {

}
if (CONDITIONS) {

}

"""
is_active = True

if is_active:
    print("Body")

if is_active:
  print("Body")
else:
        print("Body")
        print("Bye")
        if True:
          print("Body")
            # IndentationError: unexpected indent
            # print("Bye")

if is_active:
        print("Body")
#   print("Body")

if True:
    print("Hello")
    if True:
        if True: 
            print("Good job!")
        else:
            pass
    else:
        pass
else:
    pass

print("Hello")