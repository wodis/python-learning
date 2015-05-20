# encoding: utf-8
__author__ = 'wudi'


class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def sayHi(self):
        print "my name is %s . I'm %d years old. " % (self.name, self.age),
        if self.gender == 1:
            print "男"
        elif self.gender == 2:
            print "女"
        else:
            print "外星人"


class Child(Person):
    def __init__(self, name, age, gender, school):
        Person.__init__(self, name, age, gender)
        self.school = school

    def sayHi(self):
        Person.sayHi(self)
        print "School : %s" % self.school


class Robot:
    def __init__(self, battery=200):
        self.battery = battery

    def display(self):
        print "Battery : %d" % self.battery


class RobotChild(Child, Robot):
    def __init__(self, name, age, gender, school, battery):
        Child.__init__(self, name, age, gender, school)
        Robot.__init__(self, battery)


if __name__ == '__main__':
    wudi = RobotChild("wudi", 26, 2, "北大", 1000)
    wudi.sayHi()
    wudi.display()