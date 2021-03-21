'''
class Person:
    def __init__(self):
        self.name = 'kim'
        self.age = 30
        self.address = 'seoul'

    def print_info(self):
        print('name:{} age:{} address:{}'.format(self.name, self.age, self.address))


obj1 = Person()
obj1.print_info()
'''

class InstanceC:
    #text_list = []
    def __init__(self):
        self.text_list = []
    def add(self, text):
        self.text_list.append(text)

    def print_list(self):
        print(self.text_list)


obj2 = InstanceC()
obj2.add('first')
obj2.print_list()

obj3 = InstanceC()
obj3.add('second')
obj3.print_list()







