"""Scene 3: Linear Independence and Dependence (~60 seconds)."""

from __future__ import annotations
from manim import (
    Create,
    DOWN,
    Dot,
    FadeIn,
    FadeOut,
    GrowArrow,
    LEFT,
    Line,
    RIGHT,
    Scene,
    UP,
    VGroup,
    ValueTracker,
    always_redraw,
)

from utils.theme import (
    ERROR_COLOR,
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


class Scene3Independence(Scene):
    """Compare linearly independent vectors vs. linearly dependent vectors."""

    def construct(self) -> None:
        apply_theme()

        header = make_title("2. Linear Independence & Dependence", font_size=34).to_edge(UP + LEFT, buff=0.4)
        test_card = make_card(
            make_math_text("Test:  c₁v₁ + c₂v₂ = 0", font_size=22, color=TEXT_MAIN),
            padding_x=0.28,
            padding_y=0.14,
        ).to_edge(UP + RIGHT, buff=0.4)

        self.play(FadeIn(header), FadeIn(test_card), run_time=1.8)
        self.wait(2.0)

        # Left panel: Independent
        left_plane = make_plane(x_range=(-3, 3, 1), y_range=(-2, 2, 1), x_length=5.2, y_length=3.3)
        left_plane.move_to([-3.3, -0.35, 0])
        left_title = make_subtitle("Case A: Independent", font_size=23, color=HIGHLIGHT_COLOR)
        left_title.next_to(left_plane, UP, buff=0.22)

        v1_left = make_vector(left_plane, (1, 0), color=PRIMARY_COLOR)
        v2_left = make_vector(left_plane, (0, 1), color=SECONDARY_COLOR)
        v1_l_lbl = make_math_text("v₁=(1,0)", font_size=17, color=PRIMARY_COLOR).next_to(v1_left, DOWN, buff=0.12)
        v2_l_lbl = make_math_text("v₂=(0,1)", font_size=17, color=SECONDARY_COLOR).next_to(v2_left, LEFT, buff=0.12)

        self.play(Create(left_plane), FadeIn(left_title), run_time=1.6)
        self.play(GrowArrow(v1_left), GrowArrow(v2_left), FadeIn(v1_l_lbl), FadeIn(v2_l_lbl), run_time=1.6)

        indep_eq1 = make_math_text("c₁(1,0) + c₂(0,1) = (0,0)", font_size=18, color=TEXT_MAIN)
        indep_eq2 = make_math_text("⇒  c₁ = 0,  c₂ = 0  (only trivial)", font_size=18, color=HIGHLIGHT_COLOR)
        indep_text = VGroup(indep_eq1, indep_eq2).arrange(DOWN, buff=0.1).next_to(left_plane, DOWN, buff=0.25)
        self.play(FadeIn(indep_text), run_time=1.5)
        self.wait(4.5)

        # Right panel: Dependent
        right_plane = make_plane(x_range=(-3, 3, 1), y_range=(-2, 2, 1), x_length=5.2, y_length=3.3)
        right_plane.move_to([3.3, -0.35, 0])
        right_title = make_subtitle("Case B: Dependent", font_size=23, color=ERROR_COLOR)
        right_title.next_to(right_plane, UP, buff=0.22)

        v1_right = make_vector(right_plane, (1, 0), color=PRIMARY_COLOR)
        # Offset v3 slightly in y visually or draw above axis? Better: draw on axis with distinct tip/thickness
        v3_right = make_vector(right_plane, (2, 0), color=SECONDARY_COLOR, stroke_width=3.8)
        v1_r_lbl = make_math_text("v₁=(1,0)", font_size=17, color=PRIMARY_COLOR).next_to(
            right_plane.c2p(1, 0), DOWN, buff=0.18
        )
        v3_r_lbl = make_math_text("v₃=(2,0) = 2v₁", font_size=17, color=SECONDARY_COLOR).next_to(
            right_plane.c2p(2, 0), UP, buff=0.18
        )

        self.play(Create(right_plane), FadeIn(right_title), run_time=1.6)
        self.play(GrowArrow(v1_right), FadeIn(v1_r_lbl), run_time=1.2)
        self.play(GrowArrow(v3_right), FadeIn(v3_r_lbl), run_time=1.4)

        dep_eq1 = make_math_text("2v₁ - 1v₃ = 0  (c₁=2, c₂=-1 ≠ 0)", font_size=18, color=ERROR_COLOR)
        dep_eq2 = make_math_text("Span{v₁, v₃} = x-axis line only", font_size=18, color=SECONDARY_COLOR)
        dep_text = VGroup(dep_eq1, dep_eq2).arrange(DOWN, buff=0.1).next_to(right_plane, DOWN, buff=0.25)
        self.play(FadeIn(dep_text), run_time=1.5)
        self.wait(3.0)

        # Show combinations trapped on the x-axis line
        span_line = Line(
            right_plane.c2p(-3, 0),
            right_plane.c2p(3, 0),
            color=SECONDARY_COLOR,
            stroke_width=5.0,
            stroke_opacity=0.65,
        )
        t_tracker = ValueTracker(1.5)
        sliding_vec = always_redraw(
            lambda: make_vector(
                right_plane,
                (t_tracker.get_value(), 0),
                color=RESULTANT_COLOR,
                stroke_width=6.0,
            )
        )
        self.play(Create(span_line), run_time=1.5)
        self.add(sliding_vec)
        self.play(t_tracker.animate.set_value(-2.8), run_time=3.0)
        self.play(t_tracker.animate.set_value(2.8), run_time=3.0)
        self.play(t_tracker.animate.set_value(1.0), run_time=2.0)

        # Unreachable point (0, 1)
        unreach_dot = Dot(right_plane.c2p(0, 1), color=ERROR_COLOR, radius=0.08)
        unreach_lbl = make_math_text("✗ (0, 1) unreachable", font_size=16, color=ERROR_COLOR)
        unreach_lbl.next_to(unreach_dot, UP, buff=0.12)
        self.play(FadeIn(unreach_dot), FadeIn(unreach_lbl), run_time=1.5)
        self.wait(7.5)

        # Bottom takeaway
        takeaway = make_card(
            make_subtitle(
                "Independence matters: redundant vectors collapse space instead of expanding it.",
                font_size=21,
                color=TEXT_MAIN,
            ),
            padding_x=0.32,
            padding_y=0.15,
            border_color=HIGHLIGHT_COLOR,
        ).to_edge(DOWN, buff=0.2)
        self.play(FadeIn(takeaway, shift=UP * 0.15), run_time=1.5)
        self.wait(11.0)

        self.remove(sliding_vec)
        self.play(
            FadeOut(
                VGroup(
                    header,
                    test_card,
                    left_plane,
                    left_title,
                    v1_left,
                    v2_left,
                    v1_l_lbl,
                    v2_l_lbl,
                    indep_text,
                    right_plane,
                    right_title,
                    v1_right,
                    v3_right,
                    v1_r_lbl,
                    v3_r_lbl,
                    dep_text,
                    span_line,
                    unreach_dot,
                    unreach_lbl,
                    takeaway,
                )
            ),
            run_time=1.2,
        )
