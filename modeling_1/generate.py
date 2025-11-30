import numpy as np

a = 3e-10
n = 2000
x = np.linspace(-1.5 * a, 1.5 * a, n)
U = np.zeros(n)
for i in range(n):
    if -a <= x[i] < -a / 2:
        U[i] = -36
    elif -a / 2 <= x[i] < 0:
        U[i] = -60
    elif 0 <= x[i] < a / 2:
        U[i] = -75
    elif a / 2 <= x[i] <= a:
        U[i] = -40
    else:
        U[i] = 0
ev = 1.6e-19
with open("data_steps.txt", "w", encoding="utf-8") as f:
    for i in range(n):
        f.write(f"{U[i] * ev}\n")
