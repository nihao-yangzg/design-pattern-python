#coding=utf-8
###----------------------------###
### 通过type类的类生成器       ###
class Singleton(type):
    __doc__  = 'singleton class factory\n __metaclass__ = Singleton'
    def __init__(self, name, bases, dict):
       # 父类type的构造方法，参数为name, bases, dict
       super(Singleton, self).__init__(name, bases, dict)
       self.instance = None


    def __call__(self, *args, **kwargs):
        if self.instance is None:
            self.instance = super(Singleton, self).__call__(*args, **kwargs)
        return self.instance
        

class Myclass(object):
    __metaclass__ = Singleton

###----------------------------###
###       not singleton        ###
###----------------------------###

class NotSingleton(type):
    def __init__(self, name, bases, dict):
         super(NotSingleton, self).__init__(name, bases, dict)
    def __call__(self, *args, **kargs):
         return super(NotSingleton, self).__call__(*args, **kargs)


class PlainClass(object):
    __metaclass__ = NotSingleton


###----------------------------###
###      another singlton      ###
###----------------------------###

def singleton(cls):
    cls.instance = None
    def abc():
        if cls.instance is None:
            cls.instance = cls()
        return cls.instance
    return abc


@singleton
class Myclass2(object):
    def __init__(self):
        pass

if __name__ == '__main__':
    c1 = Myclass()
    c2 = Myclass()

    print c1
    print c2
    print type(c1)
    print type(type(c1))
    print type(type(type(c1)))


    c3 = PlainClass()
    c4 = PlainClass()

    print c3
    print c4

    print type(c3)
    print type(type(c3))
    print isinstance(Singleton, object)
    print isinstance(NotSingleton, object)
    print isinstance(object, type)
    print Singleton.__doc__


    c5 = Myclass2()
    c6 = Myclass2()
    print c5
    print c6
    print c5 == c6
    print c5.instance
    c7 = PlainClass()
    print c7

