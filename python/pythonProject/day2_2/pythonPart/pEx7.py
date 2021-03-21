def print_info(name, address='seoul', age=20):
    print('name:{} addres:{} age:{}'.format(name, address, age))

print_info('kim', 'suwon', 30)
print_info('lee','daegu')
print_info(address='busan', name='choi')

print()

def add(*data):
    result = 0
    for d in data:
        result += d
    return result

print(add(10,20,30))
print(add(10,20,30,40,50))

print()

def settingF(**sdata):
    for k in sdata.keys():
        print('{}:{}'.format(k, sdata[k]))

settingF(color='red', linewidth=5, data=[10,20,30])

