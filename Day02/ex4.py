#!/usr/bin/python  
# -*- coding: utf-8 -*-

def main():
    index = int(input('请输入正整数:'))
    if index > 0:
        data = getDataFromIndex(index)
        print('data:', data)
    else:
        print('输入的%d不合法' % index)
    
    a = 0
    b = 1
    for _ in range(20):
        (a, b) = (b, a + b)
        print(a, end=' ')

def getDataFromIndex(n):
    if n == 1 or n == 2:
        return 1
    else:
        return getDataFromIndex(n - 1) + getDataFromIndex(n - 2)

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a

if __name__ == '__main__':
    main() 