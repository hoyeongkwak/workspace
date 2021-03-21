class AA:
    def __init__(self):
        print('AA init func call')
        self.message = 'hi hello'

class BB(AA):
    def __init__(self):
        super().__init__()
        print('BB init func call')
        print(self.message)


obj1 = BB()
