number = int(input("Enter a number: "))

temp = number
digits = len(str(number))
sum = 0

while temp > 0:
    digit = temp % 10
    sum += digit ** digits
    temp //= 10

if sum == number:
    print("Armstrong Number")
else:
    print("Not Armstrong")