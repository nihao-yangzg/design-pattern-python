#coding=utf-8
# writen in 2017-03-18

###---------------------------###
###        装饰器模式          ###
###---------------------------###
class AbstractHouseComponent(object):
    def __init__(self):
        raise SyntaxError('cannot instanced')

    def getCost(self):
        raise SyntaxError('has not overrided')

    def getCategory(self):
        raise SyntaxError('has not overrided')

class House(AbstractHouseComponent):
    def __init__(self):
        self.cost = 1200000
        self.contents = []

    def getCost(self):
        return self.cost

    def getCategory(self):
        return self.contents


class InnerDecorator(AbstractHouseComponent):
    def __init__(self, house):
        self.cost = 120000
        self.name = 'inner'
        self.house = house

    def getCost(self):
        return self.cost + self.house.getCost()

    def getCategory(self):
        category = self.house.getCategory()
        category.append(self.name)
        return category
    # 自定义方法，对被装饰对象的功能扩展
    def display(self):
        print('inner')

class OuterDecorator(AbstractHouseComponent):
    def __init__(self, house):
        self.cost = 340000
        self.name = 'outer'
        self.house = house

    def getCost(self):
        return self.cost + self.house.getCost()

    def getCategory(self):
        category = self.house.getCategory()
        category.append(self.name)
        return category

    # 自定义方法
    def show(self):
        print 'haha'

class GaugeDecorator(AbstractHouseComponent):
    def __init__(self, house):
        self.cost = 40000
        self.name = 'gauge'
        self.house = house

    def getCost(self):
        return self.cost + self.house.getCost()

    def getCategory(self):
        category = self.house.getCategory()
        category.append(self.name)
        return category

if __name__ == '__main__':
    house = House()

    house = InnerDecorator(house)
    house.display()
    house = OuterDecorator(house)
    house = InnerDecorator(house)
    house = GaugeDecorator(house)
    print house.getCategory()
    print house.getCost()
