def missingno(list1):
    return [ x for x in range(list1[0], list1[-1]+1) if x not in list1 ]
    '''result = []
    for i in range(list1[0],list1[-1] + 1):
        if i not in list1:
            result.append(i)
    return result'''

print(missingno([1,2,3,5,7,10]))