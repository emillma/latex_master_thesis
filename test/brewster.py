import sympy as sp
from sympy import Matrix
import symforce as sf
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
from pathlib import Path


n_air = sp.symbols("\\eta_a", real=True, positive=True)
n_water = sp.symbols("\\eta_w", real=True, positive=True)

a_air = sp.symbols("\\theta_i", real=True, positive=True)
a_water = sp.symbols("\\theta_r", real=True, positive=True)


a_water_f = sp.asin(sp.sin(a_air) * n_air / n_water)
# n_water_f = (n_air * sp.sin(a_air)) / sp.sin(a_water)

vals = {
    n_air: 1,
    n_water: 1.33,
    # n_water: 1.33,
    a_water: a_water_f,
}
r_s = (n_air * sp.cos(a_air) - n_water * sp.cos(a_water)) / (
    n_air * sp.cos(a_air) + n_water * sp.cos(a_water)
)
r_p = (n_water * sp.cos(a_air) - n_air * sp.cos(a_water)) / (
    n_water * sp.cos(a_air) + n_air * sp.cos(a_water)
)


r_s = sp.simplify((r_s).subs(vals))
r_p = sp.simplify((r_p).subs(vals))


# print(sp.latex(sp.simplify(r_s)), "\n")
# print(sp.latex(sp.simplify(r_p)), "\n")
# print(sp.latex(r_s), "\n")
# print(sp.latex(r_p), "\n")
# dolp = r_p / r_s


x = np.linspace(0, 100, 300)
a = np.arctan(x)
f_s = sp.lambdify(a_air, r_s.subs(vals), "numpy")
f_p = sp.lambdify(a_air, r_p.subs(vals), "numpy")
fig, ax = plt.subplots()

p = f_p(a)
s = f_s(a)


# ax.plot(x, s**2, label="$s_1$")
# ax.plot(x, p**2, c="#ff00ff", label="p")
ax.legend()
ax.plot(x, np.sqrt(s**4 - p**4) / (s**2 + p**2), label="p")
# ax.plot(x, s**2 / (s**2 + p**2), label="p")
plt.savefig(Path(__file__).parent / "brewster.pdf")
