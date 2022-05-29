#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':

    s = input("Введите предложение: ")

    if 'чу' in s:
        print(s.find('чу'))
    if 'щу' in s:
        print(s.find('щу')+1)

