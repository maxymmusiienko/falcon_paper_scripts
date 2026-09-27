import numpy as np
import matplotlib.pyplot as plt

b1 = np.array([1, 3])
b2 = np.array([3, 1])
B_good = np.column_stack((b1, b2))


U = np.array([[2, 3],
              [3, 4]])
B_bad = B_good @ U
v1 = B_bad[:, 0]  # [11, 9]
v2 = B_bad[:, 1]  # [15, 13]

# 3. Генерація точок ґратки
c1_range = np.arange(-5, 15)
c2_range = np.arange(-5, 15)
C1, C2 = np.meshgrid(c1_range, c2_range)

# L = c1 * b1 + c2 * b2
lattice_points = (B_good @ np.vstack([C1.ravel(), C2.ravel()])).T

fig, ax = plt.subplots(figsize=(9, 8))

xlims = (-2, 18)
ylims = (-2, 16)

visible_points = lattice_points[
    (lattice_points[:, 0] >= xlims[0] - 2) & (lattice_points[:, 0] <= xlims[1] + 2) &
    (lattice_points[:, 1] >= ylims[0] - 2) & (lattice_points[:, 1] <= ylims[1] + 2)
]

ax.scatter(
    visible_points[:, 0], visible_points[:, 1],
    color="black", s=35, zorder=3, alpha=0.75, label="Lattice $\\mathcal{L}$"
)

def draw_vector(v, color, label):
    ax.annotate(
        "", xy=(v[0], v[1]), xytext=(0, 0),
        arrowprops=dict(
            arrowstyle="->", lw=2.4, color=color,
            shrinkA=0, shrinkB=0, mutation_scale=18
        ),
        zorder=4
    )
    ax.plot([], [], color=color, lw=2.4, label=label)

draw_vector(b1, "#2ca02c", r"Good basis: $b_1=(1, 3)$")
draw_vector(b2, "#66bb6a", r"Good basis: $b_2=(3, 1)$")

draw_vector(v1, "#d62728", r"Bad basis: $v_1=(11, 9)$")
draw_vector(v2, "#e57373", r"Bad basis: $v_2=(15, 13)$")

ax.scatter(0, 0, color="black", s=60, zorder=5)
ax.text(-0.8, -0.8, "$O$", fontsize=12, fontweight="bold")

ax.axhline(0, color="gray", lw=1, ls="--", alpha=0.6)
ax.axvline(0, color="gray", lw=1, ls="--", alpha=0.6)

ax.set_xlim(xlims)
ax.set_ylim(ylims)
ax.set_aspect("equal")
ax.grid(True, linestyle=":", alpha=0.4)
ax.legend(loc="upper left", frameon=True, fontsize=10)
ax.set_title("Visualization of 2D-Lattice: «Good» vs «Bad» basis", fontsize=13, pad=12)

plt.savefig("lattice_basis.pdf", bbox_inches='tight')

plt.tight_layout()
plt.show()

