#!/usr/bin/python  
# -*- coding: utf-8 -*-

def main():
    a = [4,6,1,10,3,7,5]
    print('sorted:', sort(a))

def sort(original):
    sorted_list = sorted(original, reverse=True)
    return sorted_list[0], sorted_list[1]

if __name__ == '__main__':
    main() 