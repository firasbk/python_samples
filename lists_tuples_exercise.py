months = ("january","february","march","april","may","june","july","august","september","october","novermber","december")
birth_date = input("enter your bday DD-MM-YYYY : ")
born_month = int( birth_date[3:5] )
print("You were born in ", months[born_month - 1])

names = ["firas", "sara", "rayyan", "bassel"]
new_name = input("enter your name to add to the list: ")
names.append(new_name)
print("The new names list ", names)
