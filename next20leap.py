def isLeap(year):
    return((year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0))

a = int(input("Enter a year:\n"))
leap = []
if(isLeap(a)):
    b = a
    while (len(leap) != 20):
        b = b + 4 
        if(isLeap(b)):
            leap.append(b)
        else:
            print("Entered year is not a leap year.")
print(leap)
