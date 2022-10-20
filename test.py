class A():
    def __init__(self):
        self.a = 0
    
    def calc(self, num):
        self.a = 4*num
        print(self.a)
    
class B(A):
    def __init__(self):
        super().__init__()
    
    def calc(self, num):
        self.a = 2*num
        print(self.a)
    
res = B()
res.calc(15)