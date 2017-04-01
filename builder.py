#encoding=utf-8
'''
                  builder 模式 
    有效应对类成员过多时构造方法内容太长问题
    因为python中存在默认参数，效果没有java中明显
    当出现许多可选参数时，java需重载多个构造函数以应对
'''
class Person(object):
    def __init__(self):
        raise SyntaxError('Person cannot instance')

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setAge(self, age):
        self.age = age

    def getAge(self):
        return self.age

    def setHometown(self, hometown):
        self.hometown = hometown

    def getHometown(self):
        return self.hometown

    def setGender(self, gender):
        self.gender = gender

    def getGender(self):
        return self.gender

    def setIdnum(self, idnum):
        self.idnum = idnum

    def getIdnum(self):
        return self.idnum

    def setJob(self, job):
        self.job = job

    def getJob(self):
        return self.job

    def __str__(self):
        return 'name = {0}, age = {1}, gender = {2}, idnum = {3}, job = {4}'.format(self.getName(),\
               self.getAge(), self.getGender(), self.getIdnum(), self.getJob())

    class PersonBuilder(object):
        def __init__(self):
            pass

        def name(self, name):
            self.name = name
            return self

        def age(self, age):
            self.age = age
            return self

        def hometown(self, hometown):
            self.hometown = hometown
            return self

        def gender(self, gender):
            self.gender = gender
            return self
        def idnum(self, idnum):
            self.idnum = idnum
            return self

        def job(self, job):
            self.job = job
            return self

        def build(self):
            person = object.__new__(Person, None, None)
            person.setName(self.name)
            person.setAge(self.age)
            person.setHometown(self.hometown)
            person.setGender(self.gender)
            person.setIdnum(self.idnum)
            person.setJob(self.job)
            return person


if __name__ == '__main__':
    builder = Person.PersonBuilder()
    person = builder.name('zhangsan')\
                    .age(14)\
                    .gender('female')\
                    .job('student')\
                    .hometown('sichuan')\
                    .idnum('423563834629')\
                    .build()
    print(person)
    print person.getName()
