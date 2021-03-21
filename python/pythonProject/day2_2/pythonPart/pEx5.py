a = 'Hello'
print(a[2])
print(a[2:])

b = a + ' world'
print(b)
c = a * 3
print(c)

d = '  good thing   '
print(d.strip())
print(d.rstrip())
print(d.lstrip())
print()

e = 'age:%d name:%s'%(20,'kim')
print(e)

f = 'age:{} name:{}'.format(20,'kim')
print(f)

g = 'total:{:.2f}'.format(2323132142.8443722)
print(g)
g = 'total:{:,.2f}'.format(2323132142.8443722)
print(g)
