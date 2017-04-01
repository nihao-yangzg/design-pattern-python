#coding=utf-8
###----------------------------------------------------###
###                      策略模式                       ###
###----------------------------------------------------###

import math

class HomeMoving(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def set_transport(self, trans):
        self.transport = trans

    def get_transport(self):
        return self.transport

    def get_cost(self):
        return self.transport.calculate_cost(self.start, self.end)

###==========================###
###      decorator           ###
###==========================###    
def override(function):
    def abcd(self, *args):
        return function(self, *args)
    return abcd

###==========================###
###     strategy base class  ###
###==========================###
class Transport(object):
    def __init__(self):
        # must inherited
        raise SyntaxError('Transport can not be instanced')

    def calculate_distance(self, start, end):
        distance = math.sqrt((start.x - end.x) ** 2 + (start.y - end.y) ** 2)
        return distance

    def calculate_cost(self, distance):
        raise SyntaxError('Transport has not been inherited')

class Texi(Transport):
    def __init__(self, name):
        #super(Texi, self).__init__()
        self.name = 'texi'
    @override
    def calculate_cost(self, start, end):
        distance = self.calculate_distance(start,end)
        return distance * 1.5

class Didi(Transport):
    def __init__(self, name):
        #super(Didi, self).__init__()
        self.name = name
    @override
    def calculate_cost(self, start, end):
        distance = self.calculate_distance(start, end)
        return distance * 1.4


class Location(object):
    def __init__(self, x, y):
        self.x = x;
        self.y = y;



if __name__ == '__main__':
    start = Location(1, 10)
    end = Location(40,8)
    homemove = HomeMoving(start, end)
    didi = Didi('didi')
    homemove.set_transport(didi)
    print 'transport : %s' % homemove.get_transport().name
    print 'cost: %f' % homemove.get_cost()

    texi = Texi('texi')
    homemove.set_transport(texi)
    print 'transport : %s' % homemove.get_transport().name
    print 'cost: %f' % homemove.get_cost()







