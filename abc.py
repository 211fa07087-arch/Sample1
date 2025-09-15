class car1:
    def __init__(self,c1,c2,c3):
        self.c1=c1
        self.c2=c2
        self.__c3=c3
    def get_price(self):
        return self.__c3
    def set_price(self,c3):
        if c3>0:
            self.__c3=c3
        else:
            print("invalid")
    def show(self):
        print("car:",self.c1,self.c2,self.__c3)
c11=car1("hi","he",4)
print("Price:", c11.get_price())
c11.set_price(90000)
c11.show()
