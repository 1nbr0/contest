"""
    Christmas tree
    NIVEAU 3
    Robin TURPIN & Tudi MOUGEOT
    17 et 18 décembre 2020
    python 3.7
"""
width=24

def triangles(t, m, b):
    for size in range(1, t + 1, 2):
        print((size * "*").center(width))
    for size in range(3, m + 1, 4):
        print((size * "*").center(width))
    for size in range(5, b + 1, 6):
        print((size * "*").center(width))

def tinsel(n):
    for size in range(n):
        print((4 * "| " + 5 * "*" + 4 * " |").center(width))
    for size in range(n):
        print((4 * "0 " + 5 * "*" + 4 * " 0").center(width))

def trunc(n):
    for size in range(n):
        print((5 * "*").center(width))

triangles(8, 16, 24)
tinsel(1)
trunc(1)