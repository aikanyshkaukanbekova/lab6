#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':

    text = input("Введите предложение: ")
    for i in range(2, len(text), 3):
        print(text[i])

