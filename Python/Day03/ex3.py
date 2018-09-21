#!/usr/bin/python  
# -*- coding: utf-8 -*-

def main():
    print('sdcard.txt = ', get_suffix('sdcard.txt'))
    print('sdcard. = ', get_suffix('sdcard.'))
    print('sdcard = ', get_suffix('sdcard'))


def get_suffix(file_name, has_dot=False):
    pos = file_name.find('.')
    if pos > 0 and pos < len(file_name) - 1:
        index = pos if has_dot else pos + 1
        return file_name[index:]
    else:
        return ''

if __name__ == '__main__':
    main() 