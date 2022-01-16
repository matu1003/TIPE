from random import random
from matplotlib import pyplot as plt

a, b, c = 2, 3, 4

T = [random() for _ in range(10)]
X = [random() for _ in range(10)]
Y = [a * T[i] + b * X[i] + c for i in range(10)]
e = 0.1

w1 = random()
w2 = random()
bias = random()

W1 = [w1]
W2 = [w2]
B = [bias]
E = []

for i in range(400):
    x = X[i%10]
    t = T[i%10]
    y = Y[i%10]
    A = w1 * t + w2 * x + bias
    Er = 0.5*((A-y)**2)
    E.append(Er)
    print(Er)
    w1 -= e * t * (A - y)
    w2 -= e * x * (A - y)
    bias -= e * (A - y)
    W1.append(w1)
    W2.append(w2)
    B.append(bias)
    print(w1, w2, bias)
    print()

plt.plot(W1)
plt.plot(W2)
plt.plot(B)
plt.show()
