'''
data1 = [i for i in range(10)]
print(data1)

data2 = [i for i in range(10) if i % 2 == 0]
print(data2)

data3 = [i if i % 2 == 0 else 10 for i in range(10)]
print(data3)

#data4 = [i for i in range(10) if i % 2 == 0 else 10]


sentence = 'it is good day'
words = sentence.split()
data4 = [[w.lower(), w.upper(), len(w)]for w in words]
print(data4)

data5 = ['kim', 'lee', 'choi']
for i, d in enumerate(data5):
    print(i, d)

data6 = {i:j for i, j in enumerate('have a good day'.split())}
print(data6)

a1 = [10, 40, 70]
a2 = [20, 70 ,90]
a3 = [110,220,330]

data7 = [x+y+z for x,y,z in zip(a1,a2, a3)]
print(data7)
print([sum(x) for x in zip(a1,a2,a3)])


def add(a, b):
    return a + b

add2 = lambda a, b: a+b
print(add(10,20))
'''

data = [1,2,3,4]

def f1(x):
    return x**2

result = list(map(f1, data))
print(result)

result2 = list(map(lambda x:x**2, data))
print(result2)

data3 = [(10,40),(5,30),(60,35)]
data3.sort(key=lambda x:x[1])
print(data3)

