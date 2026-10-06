import numpy as np
import matplotlib.pyplot as plt

poly_A = np.poly1d([0.15, -0.6, 0.2, 2.0])
poly_B = np.poly1d([-0.1, 0.5, 0.4, -1.0])

poly_add = poly_A + poly_B
poly_mul = poly_A * poly_B

x_vals = np.linspace(-1.5, 4.0, 500)

eval_pts = np.array([-0.5, 1.0, 2.2, 3.4])

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6.5))

col_A = "#e53935"
col_B = "#ec407a"
col_add = "#7cb342"
col_mul = "#1e88e5"


def setup_axis(ax, title):
    ax.axhline(0, color="black", lw=1.2)
    ax.axvline(0, color="black", lw=1.2)

    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)

    ax.set_title(title, fontsize=13, pad=15, fontweight="bold")
    ax.grid(True, linestyle=":", alpha=0.4)

    for spine in ax.spines.values():
        spine.set_color("#37474f")
        spine.set_linewidth(1.1)


ax1.plot(x_vals, poly_A(x_vals), color=col_A, lw=2.2, label=r"$A(x) \in \mathcal{P}_3$")
ax1.plot(x_vals, poly_B(x_vals), color=col_B, lw=2.2, label=r"$B(x) \in \mathcal{P}_3$")
ax1.plot(x_vals, poly_add(x_vals), color=col_add, lw=2.4, label=r"$C(x) = A(x) + B(x)$")

for i, xp in enumerate(eval_pts):
    ya, yb, yc = poly_A(xp), poly_B(xp), poly_add(xp)
    ymin, ymax = min(ya, yb, yc), max(ya, yb, yc)

    ax1.vlines(xp, ymin - 0.2, ymax + 0.2, color="#90a4ae", ls="--", lw=1.3, zorder=2)
    ax1.scatter([xp, xp, xp], [ya, yb, yc], color=[col_A, col_B, col_add],
                s=55, edgecolors="black", lw=1.1, zorder=4)
    ax1.text(xp, ymin - 0.6, f"$x_{i}$", ha="center", fontsize=10, fontweight="semibold")

setup_axis(ax1, "Point-Value Addition: $C(x_k) = A(x_k) + B(x_k)$")
ax1.set_ylim(-3.5, 6.0)
ax1.legend(loc="upper left", frameon=True, fontsize=10)

ax2.plot(x_vals, poly_A(x_vals), color=col_A, lw=2.0, alpha=0.85, label=r"$A(x)$")
ax2.plot(x_vals, poly_B(x_vals), color=col_B, lw=2.0, alpha=0.85, label=r"$B(x)$")
ax2.plot(x_vals, poly_mul(x_vals), color=col_mul, lw=2.4, label=r"$C(x) = A(x) \cdot B(x)$")

for i, xp in enumerate(eval_pts):
    ya, yb, ym = poly_A(xp), poly_B(xp), poly_mul(xp)
    ymin, ymax = min(ya, yb, ym), max(ya, yb, ym)

    ax2.vlines(xp, ymin - 0.3, ymax + 0.3, color="#90a4ae", ls="--", lw=1.3, zorder=2)
    ax2.scatter([xp, xp, xp], [ya, yb, ym], color=[col_A, col_B, col_mul],
                s=55, edgecolors="black", lw=1.1, zorder=4)
    ax2.text(xp, ymin - 0.8, f"$x_{i}$", ha="center", fontsize=10, fontweight="semibold")

setup_axis(ax2, "Point-Value Multiplication: $C(x_k) = A(x_k) \\cdot B(x_k)$")
ax2.set_ylim(-8.0, 9.0)
ax2.legend(loc="upper left", frameon=True, fontsize=10)

plt.tight_layout()

plt.savefig("point_value_operations.pdf", bbox_inches="tight", dpi=300)

plt.show()
