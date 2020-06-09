#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 Julian Bustamante <jbustamante35@gmail.com>
#
# Distributed under terms of the MIT license.
# This code is contributed
# by Harshit Agrawal

"""
Python program to generate odd sized magic squares
A function to generate odd sized magic squares
Works only when n is odd
"""
import numpy as np

def magic(n):
    # 2-D array with all
    # slots set to 0
    magicSquare = [[0 for x in range(n)]
                    for y in range(n)]

    # initialie position of 1
    i = n / 2
    j = n - 1

    # Fill the magic square
    # by placing values
    num = 1
    while num <= (n * n):
        if i == -1 and j == n: # 3rd condition
            j = n - 2
            i = 0
        else:

            # next number goes out of
            # right side of square
            if j == n:
                j = 0

            # next number goes
            # out of upper side
            if i < 0:
                i = n - 1

        if magicSquare[int(i)][int(j)]: # 2nd condition
            j = j - 2
            i = i + 1
            continue
        else:
            magicSquare[int(i)][int(j)] = num
            num = num + 1

        j = j + 1
        i = i - 1 # 1st condition
    return magicSquare

def magicshow(magicSquare):
    # Printing magic square
    #print ("Magic Squre for n =", n)
    #print ("Sum of each row or column",
    #        n * (n * n + 1) / 2, "\n")
    n = np.shape(magicSquare)[1]
    for i in range(0, n):
        for j in range(0, n):
            print('%2d ' % (magicSquare[i][j]),
                                    end = '')

            # To display output
            # in matrix form
            if j == n - 1:
                print()
