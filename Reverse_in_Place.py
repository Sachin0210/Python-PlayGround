num_list = [1,2,3,4,5,6]
len_list = len(num_list) - 1
i = 0
while(len_list >= i):
    num_list[i],num_list[len_list] = num_list[len_list],num_list[i]
    len_list -= 1
    i += 1
print(num_list)
