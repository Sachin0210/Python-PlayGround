dict    =   {02:["sachin", "dibiyapur", "7739"],01:["tanishk", "Dehradoon", "123456789"],03:["Anmol", "Aligarh", "145243425"]}
for key in sorted(dict.keys()):
    pass
print(dict)
a       =   dict.values()
for name in range(len(a)):
    print("--------------------------------")
    print("Name: {}".format(a[name][0]))
    print("Address: {}".format(a[name][1]))
    print("Phone: {}".format(a[name][2]))
    print("---------------------------------")
