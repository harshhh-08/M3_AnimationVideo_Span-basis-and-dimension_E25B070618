"""Shared visual theme, palette, and clean UI helpers for Manim scenes."""

from __future__ import annotations
from manim import (
    Arrow,
    DOWN,
    LEFT,
    NumberPlane,
    RIGHT,
    RoundedRectangle,
    Text,
    UP,
    VGroup,
    config,
)
import numpy as np

# ---------------------------------------------------------------------------
# Color Palette (from project specification)
# ---------------------------------------------------------------------------
BG_COLOR = "#101522"
PRIMARY_COLOR = "#4DA3FF"     # v1
SECONDARY_COLOR = "#FFB454"   # v2, v3
RESULTANT_COLOR = "#A78BFA"   # linear combination resultant
HIGHLIGHT_COLOR = "#48D6A5"   # positive / basis / span fill
ERROR_COLOR = "#F87171"       # failed condition / dependent warning
TEXT_MAIN = "#F5F7FA"
TEXT_SEC = "#AAB4C5"
GRID_LINE_COLOR = "#1E293B"
AXIS_COLOR = "#64748B"
CARD_BG = "#161E31"
CARD_BORDER = "#2A3652"

FONT_SANS = "Helvetica Neue"
FONT_MONO = "Menlo"

# Set background color at import time so Manim's camera picks it up immediately.
config.background_color = BG_COLOR


def apply_theme() -> None:
    """Ensure the global Manim background color is set."""
    config.background_color = BG_COLOR


def make_title(text: str, font_size: int = 38, color: str = TEXT_MAIN) -> Text:
    """Create a clean section title."""
    return Text(text, font=FONT_SANS, font_size=font_size, color=color, weight="BOLD")


def make_subtitle(text: str, font_size: int = 24, color: str = TEXT_SEC) -> Text:
    """Create a clean subtitle or explanatory caption."""
    return Text(text, font=FONT_SANS, font_size=font_size, color=color)


def make_math_text(text: str, font_size: int = 26, color: str = TEXT_MAIN) -> Text:
    """Create crisp monospace/math-styled text without requiring external LaTeX."""
    return Text(text, font=FONT_MONO, font_size=font_size, color=color)


def make_plane(
    x_range: tuple[int, int, int] = (-5, 5, 1),
    y_range: tuple[int, int, int] = (-3, 3, 1),
    x_length: float = 9.0,
    y_length: float = 5.4,
) -> NumberPlane:
    """Create a clean, low-clutter 2D coordinate plane."""
    plane = NumberPlane(
        x_range=x_range,
        y_range=y_range,
        x_length=x_length,
        y_length=y_length,
        background_line_style={
            "stroke_color": GRID_LINE_COLOR,
            "stroke_width": 1.2,
            "stroke_opacity": 0.85,
        },
        faded_line_style={
            "stroke_color": GRID_LINE_COLOR,
            "stroke_width": 0.6,
            "stroke_opacity": 0.4,
        },
        axis_config={
            "stroke_color": AXIS_COLOR,
            "stroke_width": 2.0,
            "include_numbers": False,
        },
    )
    return plane


def make_vector(
    plane: NumberPlane,
    coords: tuple[float, float],
    color: str = PRIMARY_COLOR,
    start_coords: tuple[float, float] = (0.0, 0.0),
    stroke_width: float = 5.0,
    tip_length: float = 0.22,
) -> Arrow:
    """Create a vector arrow on a given NumberPlane from start_coords to start_coords + coords."""
    start = plane.c2p(start_coords[0], start_coords[1])
    end = plane.c2p(start_coords[0] + coords[0], start_coords[1] + coords[1])
    return Arrow(
        start=start,
        end=end,
        buff=0,
        color=color,
        stroke_width=stroke_width,
        max_tip_length_to_length_ratio=0.22,
        tip_length=tip_length,
    )


def make_card(
    content: VGroup | Text,
    padding_x: float = 0.4,
    padding_y: float = 0.28,
    border_color: str = CARD_BORDER,
    fill_color: str = CARD_BG,
    fill_opacity: float = 0.92,
) -> VGroup:
    """Wrap text or a VGroup in a subtle dark rounded card."""
    box = RoundedRectangle(
        width=content.width + 2 * padding_x,
        height=content.height + 2 * padding_y,
        corner_radius=0.14,
        stroke_color=border_color,
        stroke_width=1.6,
        fill_color=fill_color,
        fill_opacity=fill_opacity,
    )
    box.move_to(content.get_center())
    return VGroup(box, content)
