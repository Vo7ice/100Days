#!/usr/bin/python  
# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod

class Employee(object, metaclass = ABCMeta):
    """员工"""

    __slots__ = ('_name')

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @abstractmethod
    def salary(self):
        raise NotImplementedError

class Manager(Employee):
    """经理"""

    __slots__ = ('_name')

    def salary(self):
        return 15000.0

class Programmer(Employee):
    """程序员"""

    __slots__ = ('_name', '_work_hour')

    def __init__(self, name, work_hour = 176):
        super().__init__(name)
        self._work_hour = work_hour

    @property
    def work_hour(self):
        return self._work_hour
    
    @work_hour.setter
    def work_hour(self, work_hour):
        self._work_hour = work_hour

    def salary(self):
        return self._work_hour * 150

class Saler(Employee):
    """销售"""

    __slots__ = ('_name', '_sales')

    def __init__(self, name, sales = 0):
        super().__init__(name)
        self._sales = sales

    @property
    def sales(self):
        return self._sales

    @sales.setter
    def sales(self, sales):
        self._sales = sales
    
    def salary(self):
        return 1200 + 0.05 * self._sales

def main():
    emps = [
        Manager('刘备'), Programmer('诸葛亮'),
        Manager('曹操'), Saler('荀彧'),
        Saler('吕布'), Programmer('张辽'),
        Programmer('赵云')
    ]
    for emp in emps:
        if isinstance(emp, Programmer):
            emp.work_hour = int(input('请输入%s本月工作时间: ' % emp.name))
        elif isinstance(emp, Saler):
            emp.sales = float(input('请输入%s本月销售额: ' % emp.name))
        # 同样是接收get_salary这个消息但是不同的员工表现出了不同的行为(多态)
        print('%s本月工资为: ￥%s元' %
              (emp.name, emp.salary()))

if __name__ == '__main__':
    main()