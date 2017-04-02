#coding=utf-8

###----------------------------------------------------###
###                  适配器模式                        ###
### A、B依照各自的规范编写类型，当B需要使用            ###
### A的方法时，通过适配器模式将A类的方法调用引入到     ###
### Adabtor的方法中。。。                              ###
###----------------------------------------------------###
class Abstract_A(object):
    def __init__(self):
        raise SyntaxError('can not initialize')

    def join(self, ss):
        raise SyntaxError('has not override')


class A(Abstract_A):
    def __init__(self):
        pass

    # A方法
    def join(self, ss):
        return reduce(lambda a,b: str(a) + ',' + str(b), ss)


class Abstract_B(object):
    def __init__(self):
        raise SyntaxError('can not initialize')

    def show(self):
        raise SyntaxError('can not initialize')

class A_Adabtor(Abstract_A):

    def __init__(self):
        self.__a = A()

    def join(self, ss):
        return self.__a.join(ss)

class B(Abstract_B):
    def __init__(self, ss):
        self.__adabtor_a = A_Adabtor()
        self.ss = ss
    def show(self):
        return self.__adabtor_a.join(self.ss)

if __name__ == '__main__':
    adabtor = A_Adabtor()
    b = B([1,2,3,4])
    print b.show()
         
