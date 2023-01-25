# // Write a function that 1) prints an array with all the names of the cuisines sorted in alphabetical order and 2) prints the sum of durations of all the cuisines

cuisines = [
{
'name' : 'Biryani',
'duration' : 300
},
{
'name' : 'Aloo Tikki',
'duration' : 80
},
{
'name' : 'Mango juice ',
'duration' : 220
}
]


sort_dict = sorted(cuisines, key=lambda x: x['name'])
print(sort_dict)



import collections

counter =  collections.Counter()

for d in cuisines:
    counter.update(d)

result_of_dur = dict(counter)

print(result_of_dur)