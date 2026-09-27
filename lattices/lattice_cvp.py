import numpy as np
import matplotlib.pyplot as plt

b1 = np.array([2.0, 0.5])
b2 = np.array([0.5, 2.0])
B = np.column_stack((b1, b2))

c_range = np.arange(-2, 7)
C1, C2 = np.meshgrid(c_range, c_range)
coords = np.vstack([C1.ravel(), C2.ravel()])
all_points = (B @ coords).T

target = np.array([3.4, 2.7])

distances = np.linalg.norm(all_points - target, axis=1)

d_min = np.min(distances)
exact_cvp_sol = all_points[np.argmin(distances)]

gamma = 2.4
gamma_d = gamma * d_min
appr_mask = distances <= gamma_d + 1e-5
appr_cvp_sols = all_points[appr_mask]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6.5), sharex=True, sharey=True)

xlims = (-1.0, 7.0)
ylims = (-1.0, 6.5)

def draw_arrow(ax, start, end, color="#2e7d32", label=None):
    ax.annotate(
        "", xy=end, xytext=start,
        arrowprops=dict(
            arrowstyle="->", lw=2.4, color=color,
            shrinkA=0, shrinkB=0, mutation_scale=18
        ),
        zorder=5
    )
    if label:
        ax.plot([], [], color=color, lw=2.4, label=label)

for ax, title in zip([ax1, ax2], ["CVP Solution (Exact)", "apprCVP Solution (Approximate)"]):
    # Осі координат
    ax.axhline(0, color="gray", lw=1.2, ls="--", alpha=0.7)
    ax.axvline(0, color="gray", lw=1.2, ls="--", alpha=0.7)

    vis = all_points[
        (all_points[:, 0] >= xlims[0] - 1) & (all_points[:, 0] <= xlims[1] + 1) &
        (all_points[:, 1] >= ylims[0] - 1) & (all_points[:, 1] <= ylims[1] + 1)
    ]
    ax.scatter(vis[:, 0], vis[:, 1], color="black", s=35, alpha=0.8, zorder=3, label=r"Lattice $\mathcal{L}$")

    ax.scatter(0, 0, color="black", s=60, zorder=6)
    ax.text(-0.5, -0.5, "$O$", fontsize=12, fontweight="bold")

    ax.scatter(target[0], target[1], color="#d62728", marker="x", s=90, lw=2.5, zorder=7, label=r"Target $t \notin \mathcal{L}$")
    ax.text(target[0] + 0.15, target[1] - 0.25, "$t$", fontsize=13, color="#d62728", fontweight="bold")

    ax.set_xlim(xlims)
    ax.set_ylim(ylims)
    ax.set_aspect("equal")
    ax.grid(True, linestyle=":", alpha=0.4)
    ax.set_title(title, fontsize=13, pad=12)

draw_arrow(ax1, target, exact_cvp_sol, color="#2e7d32", label=r"Solution of the CVP: $\|v - t\| = \operatorname{dist}(t, \mathcal{L})$")
ax1.legend(loc="upper left", frameon=True, fontsize=10)

for i, pt in enumerate(appr_cvp_sols):
    lbl = r"Solutions $\gamma$-CVP ($\|v - t\| \leq \gamma \cdot \operatorname{dist}(t, \mathcal{L})$)" if i == 0 else None
    draw_arrow(ax2, target, pt, color="#2e7d32", label=lbl)
ax2.legend(loc="upper left", frameon=True, fontsize=10)

plt.tight_layout()
fig.savefig("lattice_cvp.pdf", bbox_inches="tight")
plt.show()