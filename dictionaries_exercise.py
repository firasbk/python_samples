person = {"name":"Firas", "gender":"male", "age":34, "address":"budapest", "phone":"+365415152"}
guess = input("Please enter what you want to know about the person: ").lower()
info = person.get(guess, "your request is not available, please try other")
print("Result: ", info)
