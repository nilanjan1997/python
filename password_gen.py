
import random
print("give me the no. !")
range = int(input('\nEnter the lenght of passward: '))
list1 = ['7', '9', '8','0','3','9']
list2 = ["a", "n", "p", "s"]
list3 = ['A', 'N', 'P', 'P', 'B']
list5 = ["@", "$", "%", "^", "&", "*", "!"]
mylist = list2 + list3 + list5 + list1
# #random.choices(mylist)
# #temp = random.shuffle(mylist, range)
# #res = "".join(temp)
# # print(res)
random.shuffle(mylist)
#X = mylist[:range]
res = "".join(mylist[:range])
print(res)