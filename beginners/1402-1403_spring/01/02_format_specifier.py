# default values
# sep => space
# end => \n

# ["Hello", "world"] => "Hello&world" => "Hello&world**" 
print("Hello", "world", sep="&", end="**")
# ["Hello", "world"] => "Hello world" => "Hello world"
print("Hello", "world", end="")
# "The\tEnd\n" => "The\tEnd\n\n"
# ["The\tEnd\n", "Start\n"] => "The\tEnd\n Start\n"
print("The\tEnd\n", "Start\n", end="\n")
print("ByeBye")

"""
             P          P           
Hello&world**Hello worldThe    End
P

"""
