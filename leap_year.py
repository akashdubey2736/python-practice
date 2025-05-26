def is_leap_year(year):
    if year%4==0:
        if year%100==0:
            if year%400==0:
                print(f"Entered year {year} is  a leap year")
            else:
                print(f"Entered year {year} is not a leap year")
        else:
            print(f"Entered year {year} is  a leap year")

    else:
        print(f"Entered year {year} is not a leap year")

year=int(input("Enter the yeat you want to check for leap year"))
is_leap_year(year)