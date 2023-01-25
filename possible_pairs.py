arr = [1,2,4,5,6,3,8,1]
target = 9

def possible_pairs(arr1,target1):
    for i in range(len(arr1)):
        for j in range(i+1,len(arr1)):
            if arr1[i] + arr1[j] == target1:
              
                print([arr1[i],arr1[j]])

sol = possible_pairs(arr,target)


def findPairs(lst, K): 
    res = []
    while lst:
        num = lst.pop()
        diff = K - num
        if diff in lst:
            res.append((diff, num))
          
    res.reverse()
    return res
      
# Driver code
lst = [1, 5, 3, 7, 9]
K = 12
print(findPairs(lst, K))