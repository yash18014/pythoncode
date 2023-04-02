year = 2006

if (year % 400 == 0) and (year % 100 == 0):
    print("{0} is a leap year".format(year))

    if(year % 4 ==0) and (year % 100 != 0):
        print("{0} is a leap year".format(year))

    else:
        print("{0} is a not leap year".format(year))
