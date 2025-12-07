import numpy as np
import matplotlib.pyplot as plt

def f(x, p):
    temp = np.full_like(x, 1.0, dtype=np.float64)
    mask = x != 0
    temp[mask] = np.sin(x[mask]) / x[mask]
    
    return np.cos(x) + p * temp

x_min = -15 # нм
x_max = 15
points_number = 20000
x_arr = np.linspace(x_min, x_max, points_number)

p = float(input("Enter P: "))
func_values = f(x_arr, p)

plt.ylim(-2, 5)
plt.xlim(x_min, x_max)
plt.plot(x_arr, func_values)
plt.fill_between(x_arr, np.full_like(x_arr, -1), np.full_like(x_arr, 1), where=abs(func_values) <= 1, alpha=0.3, color="green", label="Разрешённые зоны")
plt.plot(x_arr, np.full_like(x_arr, 1), color="green", linestyle="--")
plt.plot(x_arr, np.full_like(x_arr, -1), color="green", linestyle="--")
plt.title(f"Разрешённые и запрещённые зоны (P={p})")
plt.xlabel(f"αa")
plt.ylabel(f"f(αa, p)")
plt.grid()
plt.legend()
plt.show()
