sdata = {1,4,3,5,2,4,1}
print(sdata)
sdata2 = set([2,1,3,2,1])
print(sdata2)

print()

ddata = {}
print(type(ddata))
ddata['name'] = 'kim'
print(ddata)
ddata['address'] = 'incheon'
print(ddata)

sdata = set()
print(type(sdata))

print()
print(ddata['name'])
print(ddata.get('name'))
print()
#print(ddata['height'])
print(ddata.get('height', 170))
