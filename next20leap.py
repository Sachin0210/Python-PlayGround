def isLeap(year):
    return((year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0))

year = int(input("Enter a year:\n"))
leap = []
if(isLeap(year)):
    next = year
    while (len(leap) != 20):
        next = next + 4 
        if(isLeap(next)):
            leap.append(next)
        else:
            print("Entered year is not a leap year.")
print(leap)
