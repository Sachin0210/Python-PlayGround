di = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9, "zero":0}
num = input("Enter a num string:\n").split()
for i in range(len(num)):
    if(num[i] in di):
        map(int,di[num[i]])
        print(di[num[i]])
