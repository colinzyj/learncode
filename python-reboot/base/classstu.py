#encoding:utf-8

class Animal(object):
    #类的属性
    incr = 0

    
    def __init__(self,name,age):
        print "Animal init"
        self.name = name
        ## 私有属性 __ 开头
        self.__name = name
        self.age = age
        Animal.incr += 1

    def run(self):
        print 'run', self.name, self.__name,self.age
        
    ## 私有方法 __ 开头
    def __run(self):
        print 'run', self.name, self.__name

    def eat(self):
        print 'eat'
        return self.incr

    def cry(self):
        print 'cry'

    # 类的方法
    @classmethod
    def getIncr(cls):
        return cls.incr

    # 静态函数
    @staticmethod
    def print_args(*args,**kwargs):
        print args,kwargs

class Plant(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

# 继承
class Dog(Animal):
    def __init__(self,name,age,variety):
        print "Dog init"
        super(Dog,self).__init__(name,age)
        self.__variety = variety
        
    def run(self):
        print 'run', self.name,self.age
        # 调用不到父类的私有属性
        print 'run', self.__name,self.age


if __name__ == '__main__':
    dog = Animal('dog',2)
    cat = Animal('cat',3)
    mimi = Animal('cat',1)
    Animal.print_args(1,2,3,a=1,b=2)
    flower = Plant('flower',2)
    print '============='
    print dog.eat()
    print id(Animal.incr),Animal.incr,Animal.getIncr()
    print id(dog.incr),dog.incr,dog.getIncr()
    print id(cat.incr),cat.incr,cat.getIncr()
    #修改类的属性，所有实例都修改
    Animal.incr=10
    print '============='
    print dog.eat()
    print id(Animal.incr),Animal.incr,Animal.getIncr()
    print id(dog.incr),dog.incr,dog.getIncr()
    print id(cat.incr),cat.incr,cat.getIncr()
    # 修改实例的属性，只修改本实例的值
    dog.incr = 5
    print '============='
    print dog.eat()
    print id(Animal.incr),Animal.incr,Animal.getIncr()
    print id(dog.incr),dog.incr,dog.getIncr()
    print id(cat.incr),cat.incr,cat.getIncr()
    #修改类的属性，已被实例修改的值不改变,getIncr获取的是类的属性值
    Animal.incr=20
    print '============='
    print dog.eat()
    print id(Animal.incr),Animal.incr,Animal.getIncr()
    print id(dog.incr),dog.incr,dog.getIncr()
    print id(cat.incr),cat.incr,cat.getIncr()

    
    #dog.run()

    '''
    print mimi.name
    print cat.age
    print type(dog)
    print isinstance(dog,Animal)
    print isinstance(flower,Animal)
    '''
