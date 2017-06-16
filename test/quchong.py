user_list=[]
with open('user_list') as file:
    for line in file:
        if len((line[:8].strip())) ==8:
            user_list.append(int(line[:8]))
user_list2=list(set(user_list))
f=open("user_list_quchong","w+")
for user in user_list2:
    f.write(str(user)+"\n")
f.close()

