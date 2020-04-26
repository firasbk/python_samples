first_name = input("Enter your first name: ")
middle_name = input("Enter your middle name: ")
last_name = input("Enter your last name: ")
print("Your initials are " + first_name[0] + middle_name[0] + last_name[0])

lot_number = "037-00901-00027"
print("Country Code: " + lot_number[:3])
print("Product Code: " + lot_number[4:9])
print("Batch number: " + lot_number[10:])
print("Batch number using minus: " + lot_number[-5:])
