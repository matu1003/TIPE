from random import random
from matplotlib import pyplot as plt

X = [random() for _ in range(10)]
Y = [x*2 + 1 for x in X]
e = 0.01

w = random()
b = random()

W = [w]
B = [b]
E = []

for i in range(1000):
    x = X[i%10]
    y = Y[i%10]
    z = x * w + b
    Er = 0.5*((z-y)**2)
    E.append(Er)
    print(Er)
    w -= e * x * (w * x + b - y)* Er
    b -= e * (w * x + b - y) * Er
    W.append(w)
    B.append(b)
    print(w, b)

plt.plot(W)
plt.plot(B)
plt.show()
