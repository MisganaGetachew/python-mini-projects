# leap year calculator
while True:
    year = int(input("insert a year to calculate if its a leap year: "))

    if year % 4 == 0:
        if year % 100 != 0:
            print(f'{year} is a leap year')
        elif year % 100 == 0 and year % 400 == 0:
            print(f'{year} is a leap year')
        else:
            print("its not a leap year")
    else:
        print("its not a leap year")
