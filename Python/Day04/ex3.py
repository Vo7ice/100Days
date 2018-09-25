#!/usr/bin/python  
# -*- coding: utf-8 -*-

class Person(object):

    __slots__ = ('_age', '_name')

    def __init__(self, age, name):
        self._age = age
        self._name = name
    
    @property
    def age(self):
        return self._age

    @property
    def name(self):
        return self._name
    
    @age.setter
    def age(self, age):
        self._age = age

    @name.setter
    def name(self, name):
        self._name = name

    def play(self):
        print('%s正在愉快的玩耍.' % self._name)
    
    def watch_av(self):
        if self._age > 18:
            print('%s正在看爱情动作片.' % self._name)
        else:
            print('%s正在看熊出没.' % self._name)

class Student(Person):

    def __init__(self, age, name, grade):
        super.__init__(age, name)
        self._grade = grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        self._grade = grade

    def study(self, course):
        print('%s的%s正在学习%s' % (self._grade, self._name, course))

class Teacher(Person):

    def __init__(self, age, name, title):
        super.__init__(age, name)
        self._title = title
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        self._title = title
    
    def teach(self, course):
        print('%s%s正在讲%s.' % (self._title, self._name, course))

def main():
    pass

if __name__ == '__main__':
    main()