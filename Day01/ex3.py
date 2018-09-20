import math
from math import sqrt

def main():
    a = float(input('请输入a:'))
    b = float(input('请输入b:'))
    c = float(input('请输入c:'))
    if isTriangle(a, b, c):
        line = a + b + c
        print('周长:%f' % line)
        p = line / 2
        area = sqrt(p * (p - a)*(p -b) * (p - c))
        print('面积:%f' % (area))
    else:
        print('%.2f, %.2f, %.2f不能构成三角形' % (a, b, c))
    

def isTriangle(a, b, c):
    return a + b > c and a + c > b and b + c > a
    

if __name__ == '__main__':
    main()