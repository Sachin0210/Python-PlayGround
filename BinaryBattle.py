def BinaryCon(n):
    return bin(n)

di = {}
num = int(input("Enter how many num you want to input: \n"))

for _ in range(num):
    a  = int(input("Enter numbers : \n"))
    di[a] = BinaryCon(a)
print(di)

sorted(di.keys())
max_num,di_key = 0,0
for k,i in di.items():
    n   =   str(i).count('1')
    if(max_num < n):
        max_num = n
        di_key  = k
print("Maximum Number of 1 is: {}".format(max_num))
print("Key {}".format(di_key))
