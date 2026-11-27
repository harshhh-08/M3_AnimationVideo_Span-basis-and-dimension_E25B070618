"""Pure mathematical helper functions separated from Manim animation logic."""

from __future__ import annotations
import numpy as np


def linear_combination(
    a: float,
    v1: tuple[float, float],
    b: float,
    v2: tuple[float, float],
) -> tuple[float, float]:
    """Compute a * v1 + b * v2 in R^2."""
    return (a * v1[0] + b * v2[0], a * v1[1] + b * v2[1])


def determinant_2x2(v1: tuple[float, float], v2: tuple[float, float]) -> float:
    """Compute the 2x2 determinant [v1 v2] to test linear independence in R^2."""
    return v1[0] * v2[1] - v1[1] * v2[0]


def is_linearly_independent_2d(
    v1: tuple[float, float],
    v2: tuple[float, float],
    tol: float = 1e-9,
) -> bool:
    """Return True if two 2D vectors are linearly independent (non-zero determinant)."""
    return abs(determinant_2x2(v1, v2)) > tol


def spans_r2(vectors: list[tuple[float, float]], tol: float = 1e-9) -> bool:
    """Return True if a list of 2D vectors spans all of R^2 (rank == 2)."""
    if len(vectors) < 2:
        return False
    matrix = np.array(vectors, dtype=float)
    return int(np.linalg.matrix_rank(matrix, tol=tol)) == 2


def is_basis_r2(vectors: list[tuple[float, float]], tol: float = 1e-9) -> bool:
    """Return True if a list of 2D vectors forms a basis of R^2 (size 2 and spans R^2)."""
    return len(vectors) == 2 and spans_r2(vectors, tol=tol)


def to_3d(vec_2d: tuple[float, float]) -> np.ndarray:
    """Convert a 2D tuple (x, y) into a 3D NumPy array (x, y, 0) for Manim."""
    return np.array([vec_2d[0], vec_2d[1], 0.0], dtype=float)
