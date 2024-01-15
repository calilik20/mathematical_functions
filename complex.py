a_0000 = int(input("Enter a 3 digit integer number:"))
if (a_0000 <= 99):
    print("Please enter a 3 digit number")

if a_0000 > 1:

    for i in range(2, a_0000):
        if (a_0000 % i) == 0:
            print(a_0000, " is not a prime number. ")
            break
    else:
        print(a_0000, "is a prime number.")

else:
    print(a_0000, " is a prime number.")