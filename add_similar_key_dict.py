dict_sub = {'math':100,'Eng':100,'Chem':98}
dict_sub1 = {'math':100,'Eng':100}
d3 = {}
for key in dict_sub1:
    if key in dict_sub:
        dict_sub1[key] += dict_sub[key]
    else:
        continue

d3.update(dict_sub1)
print(d3)

for key,value in dict_sub.items():
    if key not in d3:
        d3[key] = value

# print(d3)

from collections import Counter

res_dict = Counter(dict_sub) + Counter(dict_sub1)
print(dict(res_dict))


# dict_sub = {'math':100,'Eng':100,'Chem':98}
# dict_sub1 = {'math':100,'Eng':100}

# for key,val in dict_sub.items():
#     if key in dict_sub1:
#         dict_sub1[key] += dict_sub[key]
#     dict_sub1[key] = dict_sub1[val]
# print("mydict",dict_sub1)

dict_sub2 = {'math':100,'Eng':100,'Chem':98}
dict_sub3 = {'math':100,'Eng':100}
d3 = {}