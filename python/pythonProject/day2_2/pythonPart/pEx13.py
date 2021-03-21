'''
for i in range(4):
    print(i)
print()
iterator = range(3).__iter__()
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
'''

class CustomRange1:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.end:
            rvalue = self.current
            self.current += 1
            return rvalue
        else:
            raise StopIteration


for i in CustomRange1(1, 5):
    print(i)



