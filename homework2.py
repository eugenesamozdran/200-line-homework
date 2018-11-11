from math import exp, pi, sqrt
from sys import argv

x, m, s = float(argv[1]), float(argv[2]), float(argv[3])

def f(x):
    print (exp(-((x-m)**2)/((s**2)*2))/(sqrt(2*pi)*s))

print (x, m, s)
f(x)
