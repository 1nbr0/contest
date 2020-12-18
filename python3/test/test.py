# -*- coding:latin1 -*
width=23

def star(n):
    for i in range(n):
        print(("*" + (" " * 4) + "*" + (" " * 4) + "*").center(width))
        print(((" " * 2) + "*" + (" " * 2) + "*" + (" " * 2) + "*"+ (" " * 2)).center(width))
        print(((" " * 5) + "*" + (" " * 5)).center(width))
        print(("*" + " " + "*" + " " + "*" + " " + "*" + " " + "*" + " " + "*").center(width))
        print(((" " * 5) + "*" + (" " * 5)).center(width))
        print(((" " * 2) + "*" + (" " * 2) + "|" + (" " * 2) + "*"+ (" " * 2)).center(width))
        print(("*" + (" " * 4) + "|" + (" " * 4) + "*").center(width))

def triangles(t, m, b):
    for size in range(1, t + 1, 2):
        print((size * "*").center(width))
    for size in range(3, 3 + 1, 4):
        print(("0 " + size * "*" + " 0").center(width))
    for size in range(7, m + 1, 4):
        print((size * "*").center(width))
    for size in range(5, 5 + 1, 4):
        print(("0" + ( " " * 4 ) + size * "*" + ( " " * 4 ) + "0").center(width))
    for size in range(11, b + 1, 6):
        print((size * "*").center(width))

def tinsel(n):
    for size in range(n):
        print((4 * "| " + 5 * "*" + 4 * " |").center(width))
    for size in range(n):
        print((4 * "0 " + 5 * "*" + 4 * " 0").center(width))

def trunc(n):
    for i in range(n):
        print((5 * "*").center(width))
        
star(1)
triangles(8, 16, 24)
tinsel(1)
trunc(1)
