import numpy as np

a = 3e-10
n = 2000
x = np.linspace(-1.5 * a, 1.5 * a, n)
with open("data.txt", "w", encoding="utf-8") as f:
    for i in range(n):
        f.write(f"{2e3 * x[i] ** 2}\n")
