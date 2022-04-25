from random import random
from matplotlib import pyplot as plt

a, b, c = -4, 2, 3
dispersion = 0.2

epochs = 10000
per_epoch = 10

T = [random() for _ in range(100)]
X = [random() for _ in range(100)]
Y = [a * T[i] + b * X[i] + c + (random()-0.5) * dispersion for i in range(100)]
e = 0.1

w1 = random()
w2 = random()
bias = random()

W1 = [w1]
W2 = [w2]
B = [bias]

for i in range(epochs):
    w1temp = []
    w2temp = []
    btemp = []
    for j in range(per_epoch):
        x = X[((i*per_epoch) +j)%100]
        t = T[((i*per_epoch) +j)%100]
        y = Y[((i*per_epoch) +j)%100]
        A = w1 * t + w2 * x + bias
        Er = 0.5*((A-y)**2)
        w1temp.append(w1 - e * t * (A - y))
        w2temp.append(w2 - e * x * (A - y))
        btemp.append(bias - e * (A - y))
    w1 = sum(w1temp)/per_epoch
    w2 = sum(w2temp)/per_epoch
    bias = sum(btemp)/per_epoch
    W1.append(w1)
    W2.append(w2)
    B.append(bias)

print(w1, w2, bias)
print(w1 * 1 + w2 * 1 + bias)
plt.plot(W1, label = "W1")
plt.plot(W2, label = "W2")
plt.plot(B, label = "B")
plt.xlabel("Etapes")
plt.ylabel("Poids")
plt.legend()
plt.show()
