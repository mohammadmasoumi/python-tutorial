# |19||3|5|30456|| 
barcode = input()

year_of_produce = int(barcode[:4].replace("|", ""))

num_of_pipes = barcode.count("|", -3, 16)

gaurantee_section = int(barcode[-7:].replace("|", "")[:4])

quarantee_type_num = gaurantee_section // 100
quarantee_month = gaurantee_section % 100

if quarantee_type_num % 3 == 0 and quarantee_type_num % 5 == 0:
    quarantee_month += 3
elif quarantee_type_num % 3 == 0:
    quarantee_month += 1

remaining_month = quarantee_month - ((23 - year_of_produce) * 12)

if num_of_pipes == 3:
    replacement_type = "replacement without payment"
elif  num_of_pipes == 2:
    replacement_type = "replacement with payment"
elif  num_of_pipes == 1:
    replacement_type = "no replacement"

if remaining_month > 0:
    print(f"Guarantee {remaining_month} month(s). {replacement_type}")
else:
    print(f"No guarantee. {replacement_type}")