import math

import matplotlib.pyplot as plt


def square(value):
    return value * value


def cube(value):
    return value ** 3


def sinus(value):
    return math.sin(value)


def getValues(start, end, f):
    values = []
    for i in range(start, end + 1):
        values.append((i, f(i)))
    return values


items = getValues(-10, 10, cube)
x = [x for x, y in items]
y = [y for x, y in items]

plt.title("Fonction Carré")
plt.plot(x, y)
plt.xlabel('Valeurs de base')
plt.ylabel('Valeurs au carré')
plt.show()
