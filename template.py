#coding=utf-8
###2017-03-22
###-------------------------------------------###
###                 模板模式                  ###
### 将相同的处理过程抽象到一个通用方法中，将独###
### 特的方法由子类单独实现                    ###
###-------------------------------------------###
class Washing(object):
    def __init__(self):
        raise RuntimeError('cannot initialized Washing class')

    def washing(self):
        self.prepare_water()
        quantity = self.get_quantity()
        self.add_chemical(quantity)
        self.open_mechine()
        self.end()

    def prepare_water(self):
        raise RuntimeError('has not overrided')
        
    def add_chemical(self, quantity):
        raise RuntimeError('hsa not overrided')
    def open_mechine(self):
        raise RuntimeError('hsa not overrided')

    def end(self):
        raise RuntimeError('hsa not overrided')
    def get_quantity():
        raise RuntimeError('hsa not overrided')

class Washingwiring(Washing):
    def __init__(self, wiring, chemical):
        self.wiring = wiring
        self.chemical = chemical 

    def prepare_water(self):
        print 'water is prepared'

    def add_chemical(self, quantity):
        self.quantity = quantity

    def open_mechine(self):
        print 'washing {}, weigh: {} kg...'.format(self.wiring.name, self.wiring.weigh/1000.00)

    def end(self):
        print 'drying...'
    def get_quantity(self):
        return self.get_weigh() * 0.08
    def get_weigh(self):
        return self.wiring.weigh


class WashingTableware(Washing):
    def __init__(self, tableware, chemical):
        self.tableware = tableware
        self.chemical = chemical
    def prepare_water(self):
        print 'water is prepared'

    def add_chemical(self, chemical):
        self.chemical = chemical

    def open_mechine(self):
        print 'washing {}, weigh: {}kg...'.format(self.tableware.name, self.tableware.weigh/100.00)

    def end(self):
        print 'drying...'
    def get_quantity(self):
        return self.get_weigh() * 0.02
    def get_weigh(self):
        return self.tableware.weigh
    

class Target(object):
    def __init__(self, name, weigh):
        self.name = name
        self.weigh = weigh   


if __name__ == '__main__':
    wiring = Target('sweet', 5000)
    wiring_wash = Washingwiring(wiring, 'abc')
    wiring_wash.washing()

    tableware = Target('pan', 400)
    tableware_wash = WashingTableware(tableware, 'bcd')
    tableware_wash.washing()
