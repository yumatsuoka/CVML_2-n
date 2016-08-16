#!/usr/bin/env
# -*- coding: utf-8 -*-

"""
10:
"""

# python2とpython3のprint文の互換用おまじない
from __future__ import print_function

#from '1-1-6'
n_nlist = [i for i in range(1, 101)]

for i in n_nlist:
    (print("fizzbuzz", end=" ")) if (i % 15 == 0)\
else ((print("fizz", end=" ")) if (i % 3 == 0)\
else ((print("buzz", end=" ")) if (i % 5 == 0)\
else(print(i, end=" "))))

"""
python3からはprint文がprint関数になったので、
print()の最後にendを入れることで改行を防ぐことができる
"""
