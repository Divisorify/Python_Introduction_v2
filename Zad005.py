import string

list = [0,1,2,3]
list2 = []
for x in list:
    list2.append(x*2+1)

print(list2)

list3 = [3,8,9,5]
list4 = []
for x in list3:
    if(x%3 == 0):
        list4.append(False)
    else:
        list4.append(True)
print(list4)

list5 = ['mapple','acacia','oak']
print([x[0].upper() for x in list5])
# x[0] for x in list5:

list5 = ['mapple','acacia','oak']
print(f'{[x.len(list5[0]) for x in list5]}{len(list5[0])}')
# list5 = ['mapple','acacia','oak']
# print([x +","+ len(list5[0]) for x in list5]+ len(list5[0]))

# for x in list5:
#     print(len(list5[x]))
# for x in list5:
#     list5.append([x],[len(list5[x])])
#
# print(list5)

