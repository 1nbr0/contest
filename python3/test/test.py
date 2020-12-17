width=24

def triangles(t, m, b):
    for size in range(1, t + 1, 2):
        print((size * "*").center(width))
    for size in range(3, 3 + 1, 4):
        print(("0 " + size * "*" + " 0").center(width))
    for size in range(7, m + 1, 4):
        print((size * "*").center(width))
    for size in range(5, 5 + 1, 4):
        print(("0    " + size * "*" + "    0").center(width))
    for size in range(11, b + 1, 6):
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