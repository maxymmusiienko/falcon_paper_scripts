import numpy as np
import matplotlib.pyplot as plt

# Параметри з Example 2.6
q = 17
psi = 2
omega = 4

# Степені psi^k mod 17 для k = 0, ..., 7
k_psi = np.arange(8)
psi_powers = [(psi**k) % q for k in k_psi]

# Степені omega^m mod 17 для m = 0, ..., 3
m_omega = np.arange(4)
omega_powers = [(omega**m) % q for m in m_omega]

# Кольори для 4 пар протилежних за знаком елементів (psi^{k+4} = -psi^k mod 17)
colors_psi = ["#d32f2f", "#1976d2", "#388e3c", "#f57c00"]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 7.5))

# Допоміжна функція налаштування рамки навколо сабплота
def set_frame_style(ax):
    ax.set_xlim(-1.45, 1.45)
    ax.set_ylim(-1.45, 1.45)
    ax.set_aspect("equal")
    # Приховуємо тільки шкалу з числами
    ax.set_xticks([])
    ax.set_yticks([])
    # Оформлюємо видиму рамку навколо графіка
    for spine in ax.spines.values():
        spine.set_visible(True)
        spine.set_color("#37474f")
        spine.set_linewidth(1.3)

# -------------------------------------------------------------
# 1. Графік для <psi> (порядок 2n = 8)
# -------------------------------------------------------------
angles_psi = np.linspace(np.pi / 2, -3 * np.pi / 2, 8, endpoint=False)
x_psi = np.cos(angles_psi)
y_psi = np.sin(angles_psi)

theta = np.linspace(0, 2 * np.pi, 300)
ax1.plot(np.cos(theta), np.sin(theta), ls="--", color="#cfd8dc", lw=1.2, zorder=1)

for i in range(8):
    nxt = (i + 1) % 8
    ax1.annotate(
        "", xy=(x_psi[nxt], y_psi[nxt]), xytext=(x_psi[i], y_psi[i]), zorder=2
    )

for k in range(4):
    c = colors_psi[k]
    ax1.plot([x_psi[k], x_psi[k + 4]], [y_psi[k], y_psi[k + 4]],
             ls=":", color=c, lw=1.6, alpha=0.7, zorder=3)
    ax1.scatter([x_psi[k], x_psi[k + 4]], [y_psi[k], y_psi[k + 4]],
                s=120, color=c, edgecolors="black", lw=1.3, zorder=5)

for k in range(8):
    val = psi_powers[k]
    label = rf"$\psi^{k} \equiv {val}$"
    dx = 0.22 * np.cos(angles_psi[k])
    dy = 0.22 * np.sin(angles_psi[k])
    ax1.text(x_psi[k] + dx, y_psi[k] + dy, label, fontsize=11,
             ha='center', va='center', fontweight='semibold')

ax1.set_title(r"Primitive $2n$-th root of unity $\psi = 2 \in \mathbb{Z}_{17}$ (Order 8)" + "\n" +
              r"Negacyclic property: $\psi^4 \equiv 16 \equiv -1\ (\mathrm{mod}\ 17)$", fontsize=12, pad=15)
set_frame_style(ax1)

# -------------------------------------------------------------
# 2. Графік для <omega> (порядок n = 4)
# -------------------------------------------------------------
angles_om = np.linspace(np.pi / 2, -3 * np.pi / 2, 4, endpoint=False)
x_om = np.cos(angles_om)
y_om = np.sin(angles_om)

ax2.plot(np.cos(theta), np.sin(theta), ls="--", color="#cfd8dc", lw=1.2, zorder=1)

for i in range(4):
    nxt = (i + 1) % 4
    ax2.annotate(
        "", xy=(x_om[nxt], y_om[nxt]), xytext=(x_om[i], y_om[i]), zorder=2
    )

ax2.plot([x_om[0], x_om[2]], [y_om[0], y_om[2]], ls=":", color="#37474f", lw=1.5, alpha=0.5, zorder=3)
ax2.plot([x_om[1], x_om[3]], [y_om[1], y_om[3]], ls=":", color="#37474f", lw=1.5, alpha=0.5, zorder=3)

ax2.scatter(x_om, y_om, s=130, color="#1976d2", edgecolors="black", lw=1.3, zorder=5)

for m in range(4):
    val = omega_powers[m]
    label = rf"$\omega^{m} \equiv {val}$" + (" $\equiv -1$" if val == 16 else "")
    dx = 0.24 * np.cos(angles_om[m])
    dy = 0.24 * np.sin(angles_om[m])
    ax2.text(x_om[m] + dx, y_om[m] + dy, label, fontsize=11,
             ha='center', va='center', fontweight='semibold')

ax2.set_title(r"Primitive $n$-th root of unity $\omega = \psi^2 = 4 \in \mathbb{Z}_{17}$ (Order 4)" + "\n" +
              r"Standard cyclic group: $\omega^2 \equiv -1, \; \omega^4 \equiv 1\ (\mathrm{mod}\ 17)$", fontsize=12, pad=15)
set_frame_style(ax2)

plt.tight_layout()
plt.savefig("ntt_roots_z17.pdf", bbox_inches="tight", dpi=300)
plt.show()
