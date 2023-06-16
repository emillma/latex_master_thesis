import sympy as sp
from sympy import Matrix
import symforce as sf
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
from pathlib import Path

p_perp = sp.symbols("r_perp", real=True, positive=True)
p_para = sp.symbols("r_para", real=True, positive=True)


n_air = sp.symbols("\\eta_a", real=True, positive=True)
n_water = sp.symbols("\\eta_w", real=True, positive=True)

a_air = sp.symbols("\\theta_i", real=True, positive=True)
a_water = sp.symbols("\\theta_r", real=True, positive=True)


vals = {
    n_air: 1,
    n_water: 1.33,
}


a_water_f = sp.asin(sp.sin(a_air) * n_air / n_water)
n_water_f = (n_air * sp.sin(a_air)) / sp.sin(a_water)

r_s = (n_air * sp.cos(a_air) - n_water * sp.cos(a_water)) / (
    n_air * sp.cos(a_air) + n_water * sp.cos(a_water)
)
r_p = (n_water * sp.cos(a_air) - n_air * sp.cos(a_water)) / (
    n_water * sp.cos(a_air) + n_air * sp.cos(a_water)
)


R_s = sp.simplify((r_s).subs(a_water, a_water_f))
R_p = sp.simplify((r_p).subs(a_water, a_water_f))


print(sp.latex(sp.simplify(r_s)), "\n")
print(sp.latex(sp.simplify(r_p)), "\n")
print(sp.latex(R_s), "\n")
print(sp.latex(R_p), "\n")
# dolp = r_p / r_s

sp.asin(n_air / n_water)

x = np.linspace(0, np.pi / 2, 20)
f_x = sp.lambdify(a_air, a_water_f.subs(vals), "numpy")
y = f_x(x)
fig = plt.plot(x, y)
plt.savefig(Path(__file__).parent / "brewster.pdf")
