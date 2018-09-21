#!/usr/bin/python  
# -*- coding: utf-8 -*-
from random import randint

def main():
    code = generate_code()
    print('code:',code)

def generate_code(index=4):
    all = []
    code = []
    all.extend(list_case(start='a'))
    all.extend(list_case(start='A'))
    all.extend(list_case(start='0',length=10))
    print('all:',all)
    for _ in range(index):
        ran = randint(0, len(all) -1)
        print('ran:',ran)
        code += all[ran]
    return code
    
def list_case(start, length=26):
    temp = []
    for i in range(ord(start), ord(start) + length):
        temp.append(chr(i))
    return temp

if __name__ == '__main__':
    main()