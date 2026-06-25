name=input("what is your name:")
birth_year=int(input("what is your date of birth:"))
current_year=int(input("what is current year:"))
age=current_year-birth_year
print(f"hello {name} your are {age} years old")
if(age>=18):
    print("you are an adult")
elif(age>=13):
    print("you are a teenager")
else:
    print("you are a child")