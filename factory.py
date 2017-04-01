#coding=utf-8
'''
工厂模式                    
原始类的创建过程比较复杂，如需要通过查询数据库等操作才
能获取相应的类成员变量，若将此过程放入构造方法中，构造
方法显得相当臃肿。通过工厂方法可以避免此问题
'''

class Book(object):
    def __init__(self, name, publish_company, book_id, publish_date=None, price=0.0):
        self.name = name
        self.publish_date = publish_date
        self.price = price
        self.publish_company = publish_company
        self.book_id = book_id


class BookFactory(object):
    '''
    Book对象的创建需要一系列的成员，然而可以通过book_id
    查询到其他成员的所有值，因而将查询过程放入工厂类中更为合适
    ''' 
     def __init__(self):
         pass

     def newInstance(self, book_id):
         name, pub_date, price, company, id = self.get_book_info(book_id)
         return Book(name=name, publish_date=pub_date, book_id=id, publish_company=company, price=price)

     def get_book_info(self, book_id):
         return ('python 设计模式', '2014-06-23', 35.2, '机械工业出版社', book_id)


if __name__ == '__main__':
    book_factory = BookFactory()

    book = book_factory.newInstance('2345')
    print book.name, book.publish_date, book.price, book.publish_company, book.book_id


