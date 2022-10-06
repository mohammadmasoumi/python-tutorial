n = int(input())

# is_not_aval = False
# for item in range(2, n):
#     if n % item == 0:
#         is_not_aval = True
#         print("aval nist")
#         break
#
# if not is_not_aval:
#     print("avan ast")

# for else
for item in range(2, n):
    if n % item == 0:
        print("aval nist")
        break
else:
    print("avan ast")