# -*- coding:latin1 -*
"""
    Christmas tree
    NIVEAU 2
    Robin TURPIN & Tudi MOUGEOT
    17 et 18 d�cembre 2020
    python 3.7
"""
width=23

def triangles(t, m, b):
    for size in range(1, t + 1, 2):
        print((size * "*").center(width))
    for size in range(3, m + 1, 4):
        print((size * "*").center(width))
    for size in range(5, b + 1, 6):
        print((size * "*").center(width))

def trunc(n):
    for size in range(n):
        print((5 * "*").center(width))

triangles(8, 16, 24)
trunc(3)