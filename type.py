#coding=utf-8
if __name__ == '__main__':
    c1 = type('Myclass', (object,), {'fsf': 'fdfs'})

    c2 = c1()
    c3 = c1()

    print type(c1)
    print isinstance(c1, object)
    print c2
    print c3
    print c2.fsf
