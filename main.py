from random import random
from matplotlib import pyplot as plt


X = [random() for _ in range(10)]
Y = [x*10 -4 + (random()-0.5)*0.1 for x in X]
e = 0.1

w = random()
b = random()

W = [w]
B = [b]

for i in range(10000):
    x = X[i%10]
    y = Y[i%10]
    z = x * w + b
    Er = 0.5*((z-y)**2)
    w -= e * x * (z - y)
    b -= e * (z - y)
    W.append(w)
    B.append(b)

print(w, b)
plt.title("1 poids 1 biais pour 10x-4")
plt.xlabel("Etapes")
plt.ylabel("Poids")

plt.plot(W, label = "W")
plt.plot(B, label = "B")
plt.legend()

plt.show()
