#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':

    word_1 = input("Введите первое слово: ")
    word_2 = input("Введите второе слово: ")

    word_1 = list(set(word_1.lower()))
    word_2 = list(set(word_2.lower()))

    list_word1 = list(word_1)
    list_word2 = list(word_2)

    list_word1.sort()
    list_word2.sort()

    if list_word1 == list_word2:
        print("Можно")
    else:
        print("Нельзя")