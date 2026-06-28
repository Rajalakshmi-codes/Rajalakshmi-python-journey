name = input("NAME: ")
age = int(input("AGE: "))
email = input("EMAIL: ")
password = input("PASSWORD: ")
phone_number = input("PHONE_NUMBER: ")

print(name)
print(age)
print(email)
print(phone_number)

if age >= 18:
    print("You are eligible")
else:
    print("Not eligible")

if "@" in email:
    print("Valid Email")
else:
    print("Invalid Email")

if len(password) >= 8:
    print("Strong Password")
else:
    print("Weak Password")

if len(phone_number) == 10:
    print("Valid Phone Number")
else:
    print("Invalid Phone Number")

password = "*" * len(password)
print(password)
