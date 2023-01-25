'''
for i in range(1,101):
    if i > 1:
        for j in range(2,i):
            if (i % j) == 0:
                break
        else:
            print(i) '''


def prime_num(num):
    for i in range(2,num):
        if num % i == 0:
            print(num, "is prime number")
            break
        
            
    else:
        return [str(num) + " is not prime number " ]

prime_num(19)