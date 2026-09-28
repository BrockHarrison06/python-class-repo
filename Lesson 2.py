first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
current_year = int(input("Enter the current year: "))
birth_year = int(input("Enter your birth year: "))

age = current_year - birth_year

print("Hello " + first_name + " " + last_name + "!\nYou are " + str(age) + " years old this year.")

age += 1

print(f"\nIn the next year {current_year + 1}, you will be {age} years old.")

print("----------------------------")
print("Completed by, Brock Harrison")
