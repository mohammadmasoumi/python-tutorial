# print(f"|{input(): <20}|{input(): <20}|{input(): <20}|")

tick = chr(10003)

name_1 = input("Name: ")
age_1 = input("Age: ")
national_id_1 = input("NationalID: ")

name_2 = input("Name: ")
age_2 = input("Age: ")
national_id_2 = input("NationalID: ")

roof_count = 70

print("-" * roof_count)
print(f"|{tick} {'Name': <20}|{tick} {'Age': <20}|{tick} {'NationalID': <20}|")
print("-" * roof_count)
print(f"|{tick} {name_1: <20}|{tick} {age_1: <20}|{tick} {national_id_1: <20}|")
print("-" * roof_count)
print(f"|{tick} {name_2: <20}|{tick} {age_2: <20}|{tick} {national_id_2: <20}|")
print("-" * roof_count)