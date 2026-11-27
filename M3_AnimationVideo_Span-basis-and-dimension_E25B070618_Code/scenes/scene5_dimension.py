"""Scene 5: Understanding Dimension (~60 seconds)."""

from __future__ import annotations
from manim import (
    Arrow3D,
    Create,
    DEGREES,
    DOWN,
    FadeIn,
    FadeOut,
    LEFT,
    Line3D,
    NumberLine,
    Polygon,
    RIGHT,
    ThreeDAxes,
    ThreeDScene,
    UP,
    VGroup,
)

from utils.theme import (
    AXIS_COLOR,
    GRID_LINE_COLOR,
    HIGHLIGHT_COLOR,
    PRIMARY_COLOR,
    RESULTANT_COLOR,
    SECONDARY_COLOR,
    TEXT_MAIN,
    TEXT_SEC,
    apply_theme,
    make_card,
    make_math_text,
    make_subtitle,
    make_title,
)


class Scene5Dimension(ThreeDScene):
    """Smooth progression from R^1 (Line) -> R^2 (Plane) -> R^3 (3D Space)."""

    def construct(self) -> None:
        apply_theme()

        # Start with flat 2D camera orientation
        self.set_camera_orientation(phi=0 * DEGREES, theta=-90 * DEGREES)

        # Fixed HUD elements (sized so title and definition card never overlap)
        header = make_title("4. Understanding Dimension", font_size=30).to_edge(UP + LEFT, buff=0.35)
        def_card = make_card(
            make_math_text("dim(V) = # of vectors in any basis", font_size=18, color=HIGHLIGHT_COLOR),
            padding_x=0.24,
            padding_y=0.13,
            border_color=HIGHLIGHT_COLOR,
        ).to_edge(UP + RIGHT, buff=0.35)

        self.add_fixed_in_frame_mobjects(header, def_card)
        self.play(FadeIn(header), FadeIn(def_card), run_time=2.0)
        self.wait(4.5)

        # ------------------------------------------------------------------
        # Stage 1: R^1 — A Line (Dimension 1)
        # ------------------------------------------------------------------
        num_line = NumberLine(
            x_range=[-4, 4, 1],
            length=8.0,
            color=AXIS_COLOR,
            include_numbers=False,
        )
        v1_1d = Arrow3D(
            start=[0, 0, 0],
            end=[1.2, 0, 0],
            color=PRIMARY_COLOR,
            thickness=0.03,
        )
        badge_1d = make_card(
            VGroup(
                make_math_text("ℝ¹  (Line)", font_size=22, color=TEXT_MAIN),
                make_math_text("Basis: {(1)}   ⇒   dim(ℝ¹) = 1", font_size=20, color=PRIMARY_COLOR),
            ).arrange(DOWN, buff=0.08),
            padding_x=0.3,
            padding_y=0.16,
            border_color=PRIMARY_COLOR,
        ).to_edge(DOWN, buff=0.35)

        self.add_fixed_in_frame_mobjects(badge_1d)
        self.play(Create(num_line), FadeIn(v1_1d), FadeIn(badge_1d), run_time=2.8)
        self.wait(8.5)

        # ------------------------------------------------------------------
        # Stage 2: R^2 — A Plane (Dimension 2)
        # ------------------------------------------------------------------
        axes_2d = ThreeDAxes(
            x_range=[-3.5, 3.5, 1],
            y_range=[-2.5, 2.5, 1],
            z_range=[-2, 2, 1],
            x_length=7.0,
            y_length=5.0,
            z_length=4.0,
            axis_config={"color": AXIS_COLOR, "stroke_width": 2.0},
        )
        # Hide z-axis initially for R^2
        axes_2d.z_axis.set_opacity(0)

        plane_patch = Polygon(
            axes_2d.c2p(-3, -2, 0),
            axes_2d.c2p(3, -2, 0),
            axes_2d.c2p(3, 2, 0),
            axes_2d.c2p(-3, 2, 0),
            fill_color=HIGHLIGHT_COLOR,
            fill_opacity=0.12,
            stroke_color=GRID_LINE_COLOR,
            stroke_width=1.5,
        )
        e1 = Arrow3D(start=axes_2d.c2p(0, 0, 0), end=axes_2d.c2p(1.2, 0, 0), color=PRIMARY_COLOR, thickness=0.03)
        e2 = Arrow3D(start=axes_2d.c2p(0, 0, 0), end=axes_2d.c2p(0, 1.2, 0), color=SECONDARY_COLOR, thickness=0.03)

        badge_2d = make_card(
            VGroup(
                make_math_text("ℝ²  (Plane)", font_size=22, color=TEXT_MAIN),
                make_math_text("Basis: {(1,0), (0,1)}   ⇒   dim(ℝ²) = 2", font_size=20, color=SECONDARY_COLOR),
            ).arrange(DOWN, buff=0.08),
            padding_x=0.3,
            padding_y=0.16,
            border_color=SECONDARY_COLOR,
        ).to_edge(DOWN, buff=0.35)

        self.play(FadeOut(num_line), FadeOut(v1_1d), FadeOut(badge_1d), run_time=1.0)
        self.remove_fixed_in_frame_mobjects(badge_1d)

        self.add_fixed_in_frame_mobjects(badge_2d)
        self.play(Create(axes_2d.x_axis), Create(axes_2d.y_axis), FadeIn(plane_patch), run_time=2.0)
        self.play(FadeIn(e1), FadeIn(e2), FadeIn(badge_2d), run_time=2.0)
        self.wait(10.5)

        # ------------------------------------------------------------------
        # Stage 3: R^3 — 3D Space (Dimension 3)
        # ------------------------------------------------------------------
        badge_3d = make_card(
            VGroup(
                make_math_text("ℝ³  (3D Space)", font_size=22, color=TEXT_MAIN),
                make_math_text("Basis: {(1,0,0), (0,1,0), (0,0,1)}   ⇒   dim(ℝ³) = 3", font_size=19, color=RESULTANT_COLOR),
            ).arrange(DOWN, buff=0.08),
            padding_x=0.3,
            padding_y=0.16,
            border_color=RESULTANT_COLOR,
        ).to_edge(DOWN, buff=0.35)

        self.play(FadeOut(badge_2d), run_time=0.8)
        self.remove_fixed_in_frame_mobjects(badge_2d)

        # Smoothly tilt camera into 3D
        axes_2d.z_axis.set_opacity(1)
        e3 = Arrow3D(start=axes_2d.c2p(0, 0, 0), end=axes_2d.c2p(0, 0, 1.2), color=RESULTANT_COLOR, thickness=0.03)

        self.move_camera(phi=65 * DEGREES, theta=-45 * DEGREES, run_time=2.8)
        self.add_fixed_in_frame_mobjects(badge_3d)
        self.play(Create(axes_2d.z_axis), FadeIn(e3), FadeIn(badge_3d), run_time=2.0)

        # Gentle 3D orbit so depth is unmistakable
        self.begin_ambient_camera_rotation(rate=0.18)
        self.wait(16.0)
        self.stop_ambient_camera_rotation()

        # Clean exit
        self.play(
            FadeOut(axes_2d),
            FadeOut(plane_patch),
            FadeOut(e1),
            FadeOut(e2),
            FadeOut(e3),
            FadeOut(badge_3d),
            FadeOut(header),
            FadeOut(def_card),
            run_time=1.4,
        )
