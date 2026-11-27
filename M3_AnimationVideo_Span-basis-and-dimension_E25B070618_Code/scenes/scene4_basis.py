"""Scene 4: Understanding Basis (~75 seconds)."""

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
    Polygon,
    RIGHT,
    Scene,
    UP,
    VGroup,
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


class Scene4Basis(Scene):
    """Formal definition of a Basis and why both Span and Independence are required."""

    def construct(self) -> None:
        apply_theme()

        header = make_title("3. Understanding Basis", font_size=34).to_edge(UP + LEFT, buff=0.4)

        cond_title = make_subtitle("A set B is a Basis of V if BOTH hold:", font_size=20, color=TEXT_MAIN)
        cond1 = make_math_text("1. Span(B) = V   (reaches everywhere)", font_size=18, color=PRIMARY_COLOR)
        cond2 = make_math_text("2. Linearly Independent (no redundancy)", font_size=18, color=SECONDARY_COLOR)
        cond_card = make_card(
            VGroup(cond_title, cond1, cond2).arrange(DOWN, aligned_edge=LEFT, buff=0.08),
            padding_x=0.28,
            padding_y=0.15,
            border_color=HIGHLIGHT_COLOR,
        ).to_edge(UP + RIGHT, buff=0.32)

        self.play(FadeIn(header), FadeIn(cond_card), run_time=2.2)
        self.wait(4.0)

        # Three comparison columns
        col_x = [-4.3, 0.0, 4.3]
        col_groups: list[VGroup] = []

        # ------------------------------------------------------------------
        # Column 1: Valid Basis {(1, 0), (0, 1)}
        # ------------------------------------------------------------------
        p1 = make_plane(x_range=(-2, 2, 1), y_range=(-2, 2, 1), x_length=3.4, y_length=2.7)
        p1.move_to([col_x[0], -0.45, 0])
        t1 = make_math_text("{(1,0), (0,1)}", font_size=19, color=TEXT_MAIN).next_to(p1, UP, buff=0.18)
        v1_1 = make_vector(p1, (1, 0), color=PRIMARY_COLOR)
        v1_2 = make_vector(p1, (0, 1), color=SECONDARY_COLOR)
        fill1 = Polygon(
            p1.c2p(-2, -2),
            p1.c2p(2, -2),
            p1.c2p(2, 2),
            p1.c2p(-2, 2),
            fill_color=HIGHLIGHT_COLOR,
            fill_opacity=0.16,
            stroke_width=0,
        )
        c1_a = make_math_text("✓ Spans ℝ²", font_size=17, color=HIGHLIGHT_COLOR)
        c1_b = make_math_text("✓ Independent", font_size=17, color=HIGHLIGHT_COLOR)
        c1_v = make_card(
            make_subtitle("VALID BASIS", font_size=17, color=HIGHLIGHT_COLOR),
            padding_x=0.22,
            padding_y=0.1,
            border_color=HIGHLIGHT_COLOR,
        )
        b1 = VGroup(c1_a, c1_b, c1_v).arrange(DOWN, buff=0.08).next_to(p1, DOWN, buff=0.18)

        self.play(Create(p1), FadeIn(t1), run_time=1.6)
        self.play(GrowArrow(v1_1), GrowArrow(v1_2), FadeIn(fill1), run_time=2.2)
        self.play(FadeIn(b1, lag_ratio=0.2), run_time=2.2)
        self.wait(8.5)
        col_groups.append(VGroup(p1, t1, v1_1, v1_2, fill1, b1))

        # ------------------------------------------------------------------
        # Column 2: Redundant {(1, 0), (0, 1), (1, 1)}
        # ------------------------------------------------------------------
        p2 = make_plane(x_range=(-2, 2, 1), y_range=(-2, 2, 1), x_length=3.4, y_length=2.7)
        p2.move_to([col_x[1], -0.45, 0])
        t2 = make_math_text("{(1,0), (0,1), (1,1)}", font_size=18, color=TEXT_MAIN).next_to(p2, UP, buff=0.18)
        v2_1 = make_vector(p2, (1, 0), color=PRIMARY_COLOR)
        v2_2 = make_vector(p2, (0, 1), color=SECONDARY_COLOR)
        v2_3 = make_vector(p2, (1, 1), color=RESULTANT_COLOR)
        fill2 = Polygon(
            p2.c2p(-2, -2),
            p2.c2p(2, -2),
            p2.c2p(2, 2),
            p2.c2p(-2, 2),
            fill_color=HIGHLIGHT_COLOR,
            fill_opacity=0.12,
            stroke_width=0,
        )
        c2_a = make_math_text("✓ Spans ℝ²", font_size=17, color=HIGHLIGHT_COLOR)
        c2_b = make_math_text("✗ Dependent (1,1)=v₁+v₂", font_size=16, color=ERROR_COLOR)
        c2_v = make_card(
            make_subtitle("NOT A BASIS", font_size=17, color=ERROR_COLOR),
            padding_x=0.22,
            padding_y=0.1,
            border_color=ERROR_COLOR,
        )
        b2 = VGroup(c2_a, c2_b, c2_v).arrange(DOWN, buff=0.08).next_to(p2, DOWN, buff=0.18)

        self.play(Create(p2), FadeIn(t2), run_time=1.6)
        self.play(GrowArrow(v2_1), GrowArrow(v2_2), GrowArrow(v2_3), FadeIn(fill2), run_time=2.4)
        self.play(FadeIn(b2, lag_ratio=0.2), run_time=2.4)
        self.wait(10.0)
        col_groups.append(VGroup(p2, t2, v2_1, v2_2, v2_3, fill2, b2))

        # ------------------------------------------------------------------
        # Column 3: Insufficient {(1, 0)}
        # ------------------------------------------------------------------
        p3 = make_plane(x_range=(-2, 2, 1), y_range=(-2, 2, 1), x_length=3.4, y_length=2.7)
        p3.move_to([col_x[2], -0.45, 0])
        t3 = make_math_text("{(1,0)}", font_size=19, color=TEXT_MAIN).next_to(p3, UP, buff=0.18)
        v3_1 = make_vector(p3, (1, 0), color=PRIMARY_COLOR)
        line3 = Line(p3.c2p(-2, 0), p3.c2p(2, 0), color=PRIMARY_COLOR, stroke_width=4.5, stroke_opacity=0.7)
        miss_dot = Dot(p3.c2p(0, 1), color=ERROR_COLOR, radius=0.07)
        c3_a = make_math_text("✗ Fails Span (line only)", font_size=16, color=ERROR_COLOR)
        c3_b = make_math_text("✓ Independent", font_size=17, color=HIGHLIGHT_COLOR)
        c3_v = make_card(
            make_subtitle("NOT A BASIS", font_size=17, color=ERROR_COLOR),
            padding_x=0.22,
            padding_y=0.1,
            border_color=ERROR_COLOR,
        )
        b3 = VGroup(c3_a, c3_b, c3_v).arrange(DOWN, buff=0.08).next_to(p3, DOWN, buff=0.18)

        self.play(Create(p3), FadeIn(t3), run_time=1.6)
        self.play(GrowArrow(v3_1), Create(line3), FadeIn(miss_dot), run_time=2.4)
        self.play(FadeIn(b3, lag_ratio=0.2), run_time=2.4)
        self.wait(10.0)
        col_groups.append(VGroup(p3, t3, v3_1, line3, miss_dot, b3))

        # Summary insight banner
        insight = make_card(
            make_subtitle(
                "Both are essential:  Span = Complete (no gaps)   |   Independence = Minimal (unique coordinates)",
                font_size=19,
                color=TEXT_MAIN,
            ),
            padding_x=0.3,
            padding_y=0.14,
            border_color=HIGHLIGHT_COLOR,
        ).to_edge(DOWN, buff=0.18)

        self.play(FadeIn(insight, shift=UP * 0.12), run_time=1.5)
        self.wait(11.0)

        self.play(FadeOut(VGroup(header, cond_card, insight, *col_groups)), run_time=1.2)
