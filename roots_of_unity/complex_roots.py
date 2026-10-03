import numpy as np
import matplotlib.pyplot as plt

n = 8
j_indices = np.arange(n)
angles = (2 * j_indices + 1) * np.pi / 8
roots = np.exp(1j * angles)

pair_colors = ["#d32f2f", "#1976d2", "#388e3c", "#f57c00"]

labels = [
    r"$\zeta_0 = e^{i\pi/8}$",
    r"$\zeta_1 = e^{3i\pi/8}$",
    r"$\zeta_2 = e^{5i\pi/8}$",
    r"$\zeta_3 = e^{7i\pi/8}$",
    r"$\zeta_4 = -\zeta_0$",
    r"$\zeta_5 = -\zeta_1$",
    r"$\zeta_6 = -\zeta_2$",
    r"$\zeta_7 = -\zeta_3$"
]

offsets = [
    (0.08, 0.05),
    (0.05, 0.08),
    (-0.27, 0.08),
    (-0.29, 0.05),
    (-0.27, -0.10),
    (-0.24, -0.12),
    (0.05, -0.12),
    (0.08, -0.10)
]

fig, ax = plt.subplots(figsize=(8.5, 8.5))

theta = np.linspace(0, 2 * np.pi, 500)
ax.plot(np.cos(theta), np.sin(theta), color="#cfd8dc", lw=1.2, ls="--", zorder=1)

ax.axhline(0, color="gray", lw=1, ls=":", alpha=0.6)
ax.axvline(0, color="gray", lw=1, ls=":", alpha=0.6)

for j in range(4):
    color = pair_colors[j]
    r1, r2 = roots[j], roots[j + 4]

    ax.plot([r1.real, r2.real], [r1.imag, r2.imag],
            color=color, lw=1.5, ls="--", alpha=0.6, zorder=2)

    ax.scatter([r1.real, r2.real], [r1.imag, r2.imag],
               s=80, color=color, edgecolors="black", lw=1.2, zorder=4,
               label=rf"Roots Pair: $(\zeta_{{{j}}}, \zeta_{{{j + 4}}} = -\zeta_{{{j}}})$")

for i, (root, label, (dx, dy)) in enumerate(zip(roots, labels, offsets)):
    ax.text(root.real + dx, root.imag + dy, label, fontsize=11, zorder=5)

ax.scatter(0, 0, color="black", s=30, zorder=3)
ax.text(-0.06, -0.07, "$0$", fontsize=11)

ax.set_xlim(-1.45, 1.45)
ax.set_ylim(-1.45, 1.45)
ax.set_aspect("equal")
ax.grid(True, linestyle=":", alpha=0.3)

ax.set_xlabel(r"$\mathrm{Re}(z)$", fontsize=11)
ax.set_ylabel(r"$\mathrm{Im}(z)$", fontsize=11)
ax.set_title(r"Roots of $\Phi(x) = x^8 + 1$ with Antipodal Pairs ($\zeta_{j+4} = -\zeta_j$)", fontsize=12, pad=15)
ax.legend(loc="upper left", frameon=True, fontsize=9.5)

plt.tight_layout()

plt.savefig("complex_roots.pdf", bbox_inches="tight", dpi=300)

plt.show()
