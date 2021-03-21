def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def multi(a, b):
    return a * b

af = add
print(af(10, 20))

funclist = [add, sub, multi]

print(funclist[2](10,20))
print(funclist[1](10,20))

def calculator(fname, d1, d2):
    print(fname(d1, d2))

calculator(sub, 20, 50)
calculator(add, 20, 50)

def fre(n):
    if n == 'a':
        return add
    elif n =='s':
        return sub
    else:
        return multi

cal = fre('s')
print(cal(40,50))


