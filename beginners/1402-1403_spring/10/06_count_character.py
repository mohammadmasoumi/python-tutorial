string = "HelloHell12oHeElLOWOLRD12AS12LKHKJDAGHSDXNMBC"

#             LOWER                 UPPER
# 0                     25 26                   51
#  <---------26---------> <---------26--------->
count_characters = [0] * 52

for char in string:

    if ord("A") <= ord(char) <= ord("Z"):
        idx = ord(char) - ord("A") + 26
        count_characters[idx] += 1

    elif  ord("a") <= ord(char) <= ord("z"):
        idx = ord(char) - ord("a")
        count_characters[idx] += 1

for idx, count in enumerate(count_characters):

    if idx < 26:
        char = chr(idx + ord("a"))
    else:
        char = chr(idx + ord("A") - 26)
    
    print(f"{char}: {count}")