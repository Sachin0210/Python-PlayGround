def Upper_Lower_count(a):
    upper= []
    lower = []
    for i in range(len(a)):
        if(a[i].isupper()):
            upper.append(a[i])
        else:
            lower.append(a[i])
    return("Upper Case In String are :\n{} \nLower Case in string are \n{}".format(len(upper),len(lower)))

a = input("Enter a string :\n")
print(Upper_Lower_count(a))
