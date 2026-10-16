import numpy as np
import matplotlib.pyplot as plt

sigma = 1.0
mu = 0.0
z_vals = np.array([-3, -2, -1, 0, 1, 2, 3])

rho_vals = np.exp(- (z_vals**2) / (2.0 * sigma**2))

norm_factor = np.sum(rho_vals)

probs = rho_vals / norm_factor

fig, ax = plt.subplots(figsize=(9, 5.8))

x_cont = np.linspace(-4.2, 4.2, 500)
y_cont = np.exp(- (x_cont**2) / (2.0 * sigma**2)) / norm_factor
ax.plot(x_cont, y_cont, color="#1976d2", lw=2.0, ls="--", label="Gaussian envelope $\\rho_{\\sigma,\\mu}(x) / \\rho(\\mathbb{Z})$")

bars = ax.bar(z_vals, probs, width=0.38, color="#2e7d32", alpha=0.85,
              edgecolor="black", lw=1.2, zorder=3, label=r"$D_{\mathbb{Z}, 1.0}(z)$ (PMF)")

for z, p in zip(z_vals, probs):
    ax.text(z, p + 0.012, f"{p:.4f}", ha="center", va="bottom", fontsize=10, fontweight="semibold")

ax.axvspan(-3.5, 3.5, color="#e8f5e9", alpha=0.5, zorder=1, label=r"Truncation range $[-3, 3]$ ($\approx 99.6\%$)")

ax.axhline(0, color="black", lw=1.1)
ax.set_xlim(-4.2, 4.2)
ax.set_ylim(0, 0.47)
ax.set_xticks(np.arange(-4, 5))
ax.grid(True, linestyle=":", alpha=0.4, axis="y")

ax.set_xlabel(r"Lattice point $z \in \mathbb{Z}$", fontsize=11)
ax.set_ylabel(r"Probability $\mathbb{P}(X = z)$", fontsize=11)
ax.set_title(r"Centered Discrete Gaussian Distribution $D_{\mathbb{Z}, 1.0}$ ($\sigma = 1.0, \, \mu = 0$)",
             fontsize=12, pad=12, fontweight="bold")

for spine in ax.spines.values():
    spine.set_color("#37474f")
    spine.set_linewidth(1.1)

ax.legend(loc="upper right", frameon=True, fontsize=10)

plt.tight_layout()

plt.savefig("discrete_gaussian_distribution.pdf", bbox_inches="tight", dpi=300)

plt.show()
