def lam_cube(a,b,c):
    return lambda a,b,c :lam_cube(a*b*c)
    

abc = [lambda a,b,c:a*b*c]
print(abc)
    