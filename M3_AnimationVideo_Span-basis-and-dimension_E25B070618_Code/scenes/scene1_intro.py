"""Scene 1: Hook and Introduction (~30 seconds)."""

from __future__ import annotations
from manim import (
    Create,
    DOWN,
    FadeIn,
    FadeOut,
    GrowArrow,
    LEFT,
    RIGHT,
    Scene,
    UP,
    VGroup,
    Write,
)

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


class Scene1Intro(Scene):
    """Opening hook, two standard vectors, and four-topic roadmap."""

    def construct(self) -> None:
        apply_theme()

        # 0. Opening Frame: Title, Concept, Student Name & ID (0:00 - 0:05)
        open_title = make_title("Span, Basis and Dimension", font_size=44, color=TEXT_MAIN)
        open_concept = make_subtitle(
            "How Vectors Build a Space  •  Linear Algebra & Calculus (M3)",
            font_size=24,
            color=HIGHLIGHT_COLOR,
        )
        open_student = make_card(
            make_subtitle("Harsh Sharma   |   Student ID: E25B070618", font_size=22, color=TEXT_MAIN),
            padding_x=0.38,
            padding_y=0.18,
            border_color=PRIMARY_COLOR,
        )
        opening_frame = VGroup(open_title, open_concept, open_student).arrange(DOWN, buff=0.32)
        self.play(FadeIn(opening_frame, shift=UP * 0.15), run_time=1.4)
        self.wait(2.8)
        self.play(FadeOut(opening_frame), run_time=0.8)

        # 1. Opening hook question (0:05 - 0:11)
        hook = make_title("Can just two arrows create an entire plane?", font_size=36)
        hook.move_to([0, 0.2, 0])
        self.play(Write(hook), run_time=2.0)
        self.wait(3.0)
        self.play(hook.animate.to_edge(UP, buff=0.45).scale(0.75), run_time=1.0)

        # 2. Blank coordinate grid + two unit vectors (0:08 - 0:18)
        plane = make_plane(x_range=(-4, 4, 1), y_range=(-2, 2, 1), x_length=8.2, y_length=4.2)
        plane.shift(DOWN * 0.35)
        self.play(Create(plane), run_time=2.0)

        v1_arrow = make_vector(plane, (1, 0), color=PRIMARY_COLOR)
        v2_arrow = make_vector(plane, (0, 1), color=SECONDARY_COLOR)

        v1_label = make_math_text("v₁ = (1, 0)", font_size=22, color=PRIMARY_COLOR)
        v1_label.next_to(v1_arrow.get_end(), DOWN + RIGHT, buff=0.14)

        v2_label = make_math_text("v₂ = (0, 1)", font_size=22, color=SECONDARY_COLOR)
        v2_label.next_to(v2_arrow.get_end(), UP + LEFT, buff=0.14)

        self.play(GrowArrow(v1_arrow), FadeIn(v1_label), run_time=1.6)
        self.play(GrowArrow(v2_arrow), FadeIn(v2_label), run_time=1.6)
        self.wait(3.5)

        # 3. Title & learning objective roadmap (0:18 - 0:30)
        self.play(FadeOut(hook), run_time=0.8)

        title = make_title("Span, Basis and Dimension", font_size=40, color=TEXT_MAIN)
        subtitle = make_subtitle("How Vectors Build a Space", font_size=24, color=HIGHLIGHT_COLOR)
        header = VGroup(title, subtitle).arrange(DOWN, buff=0.12).to_edge(UP, buff=0.35)

        self.play(
            FadeIn(header, shift=DOWN * 0.2),
            plane.animate.set_opacity(0.35),
            v1_arrow.animate.set_opacity(0.45),
            v2_arrow.animate.set_opacity(0.45),
            v1_label.animate.set_opacity(0.45),
            v2_label.animate.set_opacity(0.45),
            run_time=1.5,
        )

        pill_specs = [
            ("1. Span", PRIMARY_COLOR),
            ("2. Independence", SECONDARY_COLOR),
            ("3. Basis", HIGHLIGHT_COLOR),
            ("4. Dimension", RESULTANT_COLOR),
        ]
        pills = VGroup(
            *[
                make_card(
                    make_subtitle(label, font_size=20, color=color),
                    padding_x=0.28,
                    padding_y=0.16,
                    border_color=color,
                )
                for label, color in pill_specs
            ]
        ).arrange(RIGHT, buff=0.3)
        pills.to_edge(DOWN, buff=0.45)

        self.play(FadeIn(pills, lag_ratio=0.18, shift=UP * 0.15), run_time=2.2)
        self.wait(6.5)

        # Clean exit
        self.play(
            FadeOut(header),
            FadeOut(pills),
            FadeOut(plane),
            FadeOut(v1_arrow),
            FadeOut(v2_arrow),
            FadeOut(v1_label),
            FadeOut(v2_label),
            run_time=1.2,
        )
