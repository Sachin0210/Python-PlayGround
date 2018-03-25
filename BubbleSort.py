def BubbleSort(a):
    n = len(a)
    for i in range(n-1):
        for j in range(0, n-1-i):
            if (a[j] > a[j+1]):
                a[j], a[j+1] = a[j+1], a[j]
    return(a)

a = [23,43,545,1,25,18,54,6,5,100]
print(BubbleSort(a))
