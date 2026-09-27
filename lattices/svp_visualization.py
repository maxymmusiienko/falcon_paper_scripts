import numpy as np
import matplotlib.pyplot as plt

b1 = np.array([2.0, 0.5])
b2 = np.array([0.5, 2.0])
B = np.column_stack((b1, b2))

c_range = np.arange(-2, 7)
C1, C2 = np.meshgrid(c_range, c_range)
coords = np.vstack([C1.ravel(), C2.ravel()])
all_points = (B @ coords).T

norms = np.linalg.norm(all_points, axis=1)
non_zero = norms > 1e-4

lambda_1 = np.min(norms[non_zero])
exact_candidates = all_points[np.isclose(norms, lambda_1, atol=1e-5)]
cand = exact_candidates[0]
exact_sol = cand if (cand[0] >= 0 and cand[1] >= 0) else -cand

gamma = 2.2
gamma_lambda_1 = gamma * lambda_1

appr_mask = (
    non_zero &
    (norms <= gamma_lambda_1 + 1e-5) &
    (all_points[:, 0] >= -1e-5) &
    (all_points[:, 1] >= -1e-5)
)
appr_solutions = all_points[appr_mask]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6.5), sharex=True, sharey=True)


xlims = (-1.0, 7.0)
ylims = (-1.0, 6.5)

def draw_vec(ax, v, color="#2e7d32", label=None):
    ax.annotate(
        "", xy=(v[0], v[1]), xytext=(0, 0),
        arrowprops=dict(
            arrowstyle="->", lw=2.4, color=color,
            shrinkA=0, shrinkB=0, mutation_scale=18
        ),
        zorder=5
    )
    if label:
        ax.plot([], [], color=color, lw=2.4, label=label)

for ax, title in zip([ax1, ax2], ["SVP Solution (Exact)", "apprSVP Solution (Approximate)"]):
    ax.axhline(0, color="gray", lw=1.2, ls="--", alpha=0.7)
    ax.axvline(0, color="gray", lw=1.2, ls="--", alpha=0.7)

    vis = all_points[
        (all_points[:, 0] >= xlims[0] - 1) & (all_points[:, 0] <= xlims[1] + 1) &
        (all_points[:, 1] >= ylims[0] - 1) & (all_points[:, 1] <= ylims[1] + 1)
    ]
    ax.scatter(vis[:, 0], vis[:, 1], color="black", s=35, alpha=0.8, zorder=3, label=r"Lattice $\mathcal{L}$")

    ax.scatter(0, 0, color="black", s=60, zorder=6)
    ax.text(-0.5, -0.5, "$O$", fontsize=12, fontweight="bold")

    ax.set_xlim(xlims)
    ax.set_ylim(ylims)
    ax.set_aspect("equal")
    ax.grid(True, linestyle=":", alpha=0.4)
    ax.set_title(title, fontsize=13, pad=12)

draw_vec(ax1, exact_sol, color="#2e7d32", label=r"Solution of the SVP: $\|v\| = \lambda_1$")
ax1.legend(loc="upper left", frameon=True, fontsize=10)

for i, pt in enumerate(appr_solutions):
    lbl = r"Solutions $\gamma$-SVP ($\|v\| \leq \gamma \lambda_1$)" if i == 0 else None
    draw_vec(ax2, pt, color="#2e7d32", label=lbl)
ax2.legend(loc="upper left", frameon=True, fontsize=10)

# ... ваш код побудови ліній та точок ...

plt.tight_layout()
fig.savefig("lattice_svp.pdf", bbox_inches="tight")
plt.show()
