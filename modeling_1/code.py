import numpy as np
import matplotlib.pyplot as plt

def func(x):
    return 0.3e3 * x ** 2

def calculate_potential(pit_type="rectangular"):
    if pit_type == "rectangular":
        p = np.zeros_like(x)
        p[np.abs(x) < a] = -U0 # потенциал внутри ямы. вне - ноль
    elif pit_type == "analytic":
        p = func(x)
    elif pit_type == "table":
        p = []
        with open("data.txt", encoding="utf8") as f:
            for line in f.readlines():
                p.append(float(line))
        p = np.array(p, dtype=float)
    else:
        print("Unsupported type")
        exit(1)
    return p

def hamiltonian():
    H = np.zeros((n, n))
    for i in range(n):
        H[i, i] = h_bar ** 2 / (m_e * dx ** 2) + p[i]
        if i > 0:
            H[i, i - 1] = -h_bar ** 2 / (2 * m_e * dx ** 2)
        if i < n - 1:
            H[i, i + 1] = -h_bar ** 2 / (2 * m_e * dx ** 2)
    return H

def solve_eq(H):
    return np.linalg.eigh(H)

def psi_norm(psi):
    return psi / np.sqrt(np.trapezoid(psi **2, x))

# Константы
ev = 1.6e-19 # эВ
m_e = 9.1093837e-31 # масса электрона
h_bar = 1.0545726e-34 # приведённая постоянная Планка
U0_ev = 55 # глубина потенциальной ямы (эВ)
U0 = U0_ev * ev # глубина потенциальной ямы (Дж)
a = 3e-10 # половина ширины ямы
n = 2000
x = np.linspace(-1.5 * a, 1.5 * a, n)
dx = x[1] - x[0]

pit_type = "rectangular"
p = calculate_potential(pit_type)
H = hamiltonian()

E_values, psi_values = solve_eq(H)
mask = E_values< min(p[0], p[-1])
E_values /= ev
normed_psi_values = psi_norm(psi_values)
# связанные состояния
E_selected = E_values[mask]
psi_selected = normed_psi_values[:, mask]

show_cnt = 7
for i in range(min(show_cnt, len(E_selected))):
    print( E_selected[i])
    plt.plot(x, psi_selected[:, i] + E_selected[i], label=f"E={round(E_selected[i], 2)} eV")
plt.grid()
plt.title("Собственные функции и собственные значения")
plt.legend()
plt.xlabel("x")
plt.ylabel("ψ(x)")
plt.show()
