#!/usr/bin/python  
# -*- coding: utf-8 -*-
from math import sqrt

class Point(object):

    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def __str__(self):
        return ('x = %.2f, y = %.2f' % (self._x, self._y))

    def path_to(self, other):
        return sqrt((self._x - other._x) ** 2 + (self._y - other._y) ** 2)
    
    def move_to(self, x=0, y=0):
        self._x = x
        self._y = y
    
    def move_by(self, dx=0, dy=0):
        self._x += dx
        self._y += dy


def main():
    p1 = Point(3, 4)
    print('p1:', p1)
    p2 = Point(0, 0)
    print('p2:', p2)
    p2.move_by(1, 1)
    print('after move p2:', p2)
    path = p1.path_to(p2)
    print('p1, p2 distance = %.2f' % path)


if __name__ == '__main__':
    main()