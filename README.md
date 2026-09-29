# Falcon Lattice Visualizations & Research Tooling

A Python-based toolkit for visual, numerical, and algorithmic exploration of foundational concepts in Lattice-Based Cryptography. This repository serves as supplementary research software for a Master's thesis focusing on the post-quantum signature scheme Falcon (Fast-Fourier Lattice-based Compact Signatures over NTRU).

---

## Motivation & Objectives

The primary goal of this repository is to bridge theoretical definitions and geometric intuition behind lattice hard problems and trapdoor designs:
* Basis Quality: Illustrating the discrepancy between "good" (short, nearly orthogonal) bases and "bad" (skewed, highly correlated) bases spanning the identical full-rank lattice.
* Core Lattice Problems: Visualizing exact vs. approximate hardness assumptions:
  * SVP (Shortest Vector Problem) and gamma-SVP (Approximate SVP).
  * CVP (Closest Vector Problem) and gamma-CVP (Approximate CVP / BDD).
* Publication-Quality Figures: Exporting standalone vector graphics (.pdf, .svg) for seamless embedding into LaTeX thesis manuscripts.

---


## Script Overview & Execution

1. Lattice Basis Quality (lattices/basis_quality.py)
Demonstrates the geometric asymmetry between private and public representations of the same lattice:
* Good Basis: Short, quasi-orthogonal vectors.
* Bad Basis: High condition-number vectors obtained via unimodular transformations.
Command:
python lattices/basis_quality.py

2. Shortest Vector Problem (lattices/svp_visualization.py)
* Exact SVP: Identifies the first successive minimum lambda_1.
* gamma-SVP: Highlights candidate vectors residing inside the relaxation boundary.
Command:
python lattices/svp_visualization.py

3. Closest Vector Problem (lattices/cvp_visualization.py)
Given an arbitrary target vector outside the lattice:
* Exact CVP: Finds the node that minimizes Euclidean distance to target.
* gamma-CVP: Illustrates acceptable decoder outputs within the bounded region.
Command:
python lattices/cvp_visualization.py

---
