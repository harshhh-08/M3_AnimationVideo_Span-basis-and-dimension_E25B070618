"""Scene 6: Summary and Credits (~15 seconds)."""

from __future__ import annotations
from manim import DOWN, FadeIn, FadeOut, LEFT, Scene, UP, VGroup

from utils.theme import (
    HIGHLIGHT_COLOR,
    PRIMARY_COLOR,
    RESULTANT_COLOR,
    SECONDARY_COLOR,
    TEXT_MAIN,
    TEXT_SEC,
    apply_theme,
    make_card,
    make_subtitle,
    make_title,
)


class Scene6Summary(Scene):
    """Three core takeaways followed by credits and AI-tool disclosure."""

    def construct(self) -> None:
        apply_theme()

        title = make_title("Key Takeaways", font_size=38, color=TEXT_MAIN).to_edge(UP, buff=0.55)
        self.play(FadeIn(title, shift=DOWN * 0.15), run_time=1.0)

        items = [
            ("1. Span", "Describes every vector a set can generate via linear combinations.", PRIMARY_COLOR),
            ("2. Basis", "A linearly independent spanning set — complete and minimal.", HIGHLIGHT_COLOR),
            ("3. Dimension", "The number of vectors in any basis of the space.", RESULTANT_COLOR),
        ]

        cards = VGroup()
        for heading, desc, color in items:
            h_txt = make_subtitle(heading, font_size=24, color=color)
            d_txt = make_subtitle(desc, font_size=20, color=TEXT_MAIN)
            row = VGroup(h_txt, d_txt).arrange(DOWN, aligned_edge=LEFT, buff=0.06)
            cards.add(make_card(row, padding_x=0.35, padding_y=0.2, border_color=color))

        cards.arrange(DOWN, buff=0.28).next_to(title, DOWN, buff=0.45)

        self.play(FadeIn(cards, lag_ratio=0.25, shift=UP * 0.12), run_time=2.8)
        self.wait(5.0)
        self.play(FadeOut(title), FadeOut(cards), run_time=1.0)

        # Credits & AI Disclosure (Closing Frame)
        cred_title = make_title("Span, Basis and Dimension", font_size=34, color=TEXT_MAIN)
        cred_sub = make_subtitle(
            "Created by Harsh Sharma  |  Student ID: E25B070618",
            font_size=23,
            color=HIGHLIGHT_COLOR,
        )
        cred_lines = VGroup(
            make_subtitle("M3 Linear Algebra & Calculus — Internal Assessment", font_size=20, color=TEXT_MAIN),
            make_subtitle("Animation: Python & Manim Community Edition", font_size=19, color=TEXT_SEC),
            make_subtitle("Narration: Human Voice-Over (separately recorded)", font_size=19, color=TEXT_SEC),
            make_subtitle("AI Disclosure: AI assistance used for Manim structuring & storyboard formatting;", font_size=17, color=TEXT_SEC),
            make_subtitle("all mathematical content and explanations verified by the author.", font_size=17, color=TEXT_SEC),
        ).arrange(DOWN, buff=0.12)

        credits_group = VGroup(cred_title, cred_sub, cred_lines).arrange(DOWN, buff=0.26)
        self.play(FadeIn(credits_group), run_time=1.2)
        self.wait(3.2)
        self.play(FadeOut(credits_group), run_time=1.0)
