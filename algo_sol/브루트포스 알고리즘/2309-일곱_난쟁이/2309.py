list_num = []

for i in range(9):
    list_num.append(int(input()))

list_num.sort()

for i in range(1<<len(list_num)):
    num_list = []
    for idx in range(len(list_num)):
        if i & (1<<idx):
            num_list.append(list_num[idx])
    if sum(num_list) == 100 and len(num_list) == 7:
        break

num_list.sort()
for i in range(len(num_list)):
    print(num_list[i])