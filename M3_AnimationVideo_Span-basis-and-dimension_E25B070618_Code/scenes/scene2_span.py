"""Scene 2: Understanding Span (~60 seconds)."""

from __future__ import annotations
from manim import (
    Create,
    DOWN,
    Dot,
    FadeIn,
    FadeOut,
    GrowArrow,
    LEFT,
    NumberPlane,
    Polygon,
    RIGHT,
    Scene,
    Transform,
    UP,
    VGroup,
    ValueTracker,
    always_redraw,
)

from utils.math_helpers import linear_combination
from utils.theme import (
    HIGHLIGHT_COLOR,
    PRIMARY_COLOR,
    RESULTANT_COLOR,
    SECONDARY_COLOR,
    TEXT_MAIN,
    TEXT_SEC,
    apply_theme,
    make_card,
    make_math_text,
    make_plane,
    make_subtitle,
    make_title,
    make_vector,
)


class Scene2Span(Scene):
    """Visualise linear combinations of (1, 0) and (0, 1) generating R^2."""

    def construct(self) -> None:
        apply_theme()

        # Header & definition card
        header = make_title("1. Understanding Span", font_size=34).to_edge(UP + LEFT, buff=0.4)
        def_line1 = make_math_text(
            "Span{v₁, v₂} = { a·v₁ + b·v₂ | a, b ∈ ℝ }",
            font_size=20,
            color=HIGHLIGHT_COLOR,
        )
        def_line2 = make_math_text(
            "a(1, 0) + b(0, 1) = (a, b)",
            font_size=20,
            color=TEXT_MAIN,
        )
        def_card = make_card(
            VGroup(def_line1, def_line2).arrange(DOWN, aligned_edge=LEFT, buff=0.1),
            padding_x=0.28,
            padding_y=0.18,
        ).to_edge(UP + RIGHT, buff=0.35)

        plane = make_plane(x_range=(-4, 4, 1), y_range=(-3, 3, 1), x_length=8.8, y_length=5.1)
        plane.shift(DOWN * 0.55)

        self.play(FadeIn(header), FadeIn(def_card), Create(plane), run_time=2.2)

        # Base vectors v1 and v2
        v1 = (1.0, 0.0)
        v2 = (0.0, 1.0)
        v1_base = make_vector(plane, v1, color=PRIMARY_COLOR)
        v2_base = make_vector(plane, v2, color=SECONDARY_COLOR)
        v1_lbl = make_math_text("v₁", font_size=20, color=PRIMARY_COLOR).next_to(
            v1_base.get_end(), DOWN, buff=0.1
        )
        v2_lbl = make_math_text("v₂", font_size=20, color=SECONDARY_COLOR).next_to(
            v2_base.get_end(), LEFT, buff=0.1
        )
        self.play(GrowArrow(v1_base), GrowArrow(v2_base), FadeIn(v1_lbl), FadeIn(v2_lbl), run_time=1.8)
        self.wait(2.5)

        # Helper to animate a specific (a, b) worked example
        eq_box = make_math_text("a = 2,  b = 1  ⇒  2v₁ + 1v₂ = (2, 1)", font_size=22, color=RESULTANT_COLOR)
        eq_box.to_edge(LEFT, buff=0.45).shift(UP * 2.15)

        def show_example(a: float, b: float, label_text: str, prev_group: VGroup | None = None) -> tuple[VGroup, Dot]:
            rx, ry = linear_combination(a, v1, b, v2)
            scaled_v1 = make_vector(plane, (a * v1[0], a * v1[1]), color=PRIMARY_COLOR)
            shifted_v2 = make_vector(
                plane,
                (b * v2[0], b * v2[1]),
                color=SECONDARY_COLOR,
                start_coords=(a * v1[0], a * v1[1]),
            )
            result_vec = make_vector(plane, (rx, ry), color=RESULTANT_COLOR, stroke_width=6.0)
            tip_dot = Dot(plane.c2p(rx, ry), color=RESULTANT_COLOR, radius=0.08)
            pt_lbl = make_math_text(f"({rx:g}, {ry:g})", font_size=20, color=RESULTANT_COLOR)
            pt_lbl.next_to(tip_dot, UP + RIGHT, buff=0.1)

            new_eq = make_math_text(label_text, font_size=21, color=RESULTANT_COLOR)
            new_eq.to_edge(LEFT, buff=0.45).shift(UP * 2.15)

            if prev_group is not None:
                self.play(FadeOut(prev_group), run_time=0.6)

            self.play(FadeIn(new_eq), run_time=0.7)
            self.play(GrowArrow(scaled_v1), run_time=1.4)
            self.play(GrowArrow(shifted_v2), run_time=1.4)
            self.play(GrowArrow(result_vec), FadeIn(tip_dot), FadeIn(pt_lbl), run_time=1.6)
            self.wait(2.5)

            keep_dot = Dot(plane.c2p(rx, ry), color=HIGHLIGHT_COLOR, radius=0.07)
            self.add(keep_dot)
            grp = VGroup(scaled_v1, shifted_v2, result_vec, tip_dot, pt_lbl, new_eq)
            return grp, keep_dot

        # Example 1: (2, 1)
        grp1, dot1 = show_example(2, 1, "a = 2,  b = 1  ⇒  2v₁ + 1v₂ = (2, 1)")
        # Example 2: (-1, 2)
        grp2, dot2 = show_example(-1, 2, "a = -1, b = 2  ⇒  -1v₁ + 2v₂ = (-1, 2)", prev_group=grp1)
        # Example 3: (1.5, -1.5)
        grp3, dot3 = show_example(1.5, -1.5, "a = 1.5, b = -1.5  ⇒  (1.5, -1.5)", prev_group=grp2)
        self.play(FadeOut(grp3), run_time=0.8)

        # Continuous sweep with ValueTrackers
        a_tr = ValueTracker(1.5)
        b_tr = ValueTracker(-1.5)

        dyn_v1 = always_redraw(
            lambda: make_vector(plane, (a_tr.get_value(), 0), color=PRIMARY_COLOR)
        )
        dyn_v2 = always_redraw(
            lambda: make_vector(
                plane,
                (0, b_tr.get_value()),
                color=SECONDARY_COLOR,
                start_coords=(a_tr.get_value(), 0),
            )
        )
        dyn_res = always_redraw(
            lambda: make_vector(
                plane,
                (a_tr.get_value(), b_tr.get_value()),
                color=RESULTANT_COLOR,
                stroke_width=5.5,
            )
        )
        dyn_readout = always_redraw(
            lambda: make_math_text(
                f"a = {a_tr.get_value():.1f},  b = {b_tr.get_value():.1f}  ⇒  ({a_tr.get_value():.1f}, {b_tr.get_value():.1f})",
                font_size=21,
                color=RESULTANT_COLOR,
            )
            .to_edge(LEFT, buff=0.45)
            .shift(UP * 2.15)
        )

        self.add(dyn_v1, dyn_v2, dyn_res, dyn_readout)
        self.play(a_tr.animate.set_value(-2.5), b_tr.animate.set_value(-1.5), run_time=3.2)
        self.play(a_tr.animate.set_value(3.0), b_tr.animate.set_value(2.0), run_time=3.2)
        self.play(a_tr.animate.set_value(-2.0), b_tr.animate.set_value(2.0), run_time=2.8)

        # Reveal lattice points and full plane fill
        lattice_dots = VGroup(
            *[
                Dot(plane.c2p(x, y), color=HIGHLIGHT_COLOR, radius=0.055)
                for x in range(-3, 4)
                for y in range(-2, 3)
            ]
        )
        plane_fill = Polygon(
            plane.c2p(-4, -3),
            plane.c2p(4, -3),
            plane.c2p(4, 3),
            plane.c2p(-4, 3),
            fill_color=HIGHLIGHT_COLOR,
            fill_opacity=0.18,
            stroke_width=0,
        )

        self.play(FadeIn(lattice_dots, lag_ratio=0.02), run_time=3.5)
        self.play(FadeIn(plane_fill), run_time=2.5)

        conclusion = make_card(
            make_subtitle("Every point (x, y) in ℝ² is reachable  ⇒  Span{v₁, v₂} = ℝ²", font_size=22, color=HIGHLIGHT_COLOR),
            padding_x=0.35,
            padding_y=0.16,
            border_color=HIGHLIGHT_COLOR,
        ).to_edge(DOWN, buff=0.25)

        self.play(FadeIn(conclusion, shift=UP * 0.15), run_time=1.4)
        self.wait(8.5)

        # Clean exit
        self.remove(dyn_v1, dyn_v2, dyn_res, dyn_readout)
        self.play(
            FadeOut(
                VGroup(
                    header,
                    def_card,
                    plane,
                    v1_base,
                    v2_base,
                    v1_lbl,
                    v2_lbl,
                    dot1,
                    dot2,
                    dot3,
                    lattice_dots,
                    plane_fill,
                    conclusion,
                )
            ),
            run_time=1.2,
        )
