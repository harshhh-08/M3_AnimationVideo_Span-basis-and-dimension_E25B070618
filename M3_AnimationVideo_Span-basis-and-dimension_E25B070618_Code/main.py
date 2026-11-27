"""Build and concatenate all six Manim scenes into output/final_video.mp4.

Usage:
    python main.py --quality low     # 480p15 fast preview
    python main.py --quality high    # 1920x1080 60fps final MP4
"""

from __future__ import annotations
import argparse
import os
import subprocess
import sys
from pathlib import Path

SCENES = [
    ("scenes/scene1_intro.py", "Scene1Intro"),
    ("scenes/scene2_span.py", "Scene2Span"),
    ("scenes/scene3_independence.py", "Scene3Independence"),
    ("scenes/scene4_basis.py", "Scene4Basis"),
    ("scenes/scene5_dimension.py", "Scene5Dimension"),
    ("scenes/scene6_summary.py", "Scene6Summary"),
]

QUALITY_FLAGS = {
    "low": (["-ql"], "480p15"),
    "medium": (["-qm"], "720p30"),
    "high": (["-qh", "--fps", "30"], "1080p30"),
}


def render_all(quality: str) -> None:
    """Render each scene with Manim and concatenate into output/final_video.mp4."""
    anim_dir = Path(__file__).resolve().parent
    project_root = anim_dir.parent
    output_dir = project_root / "output"
    output_dir.mkdir(parents=True, exist_ok=True)

    flags, res_folder = QUALITY_FLAGS[quality]
    manim_bin = Path(sys.executable).parent / "manim"
    manim_cmd = str(manim_bin) if manim_bin.exists() else "manim"

    env = os.environ.copy()
    env["PYTHONPATH"] = str(anim_dir) + os.pathsep + env.get("PYTHONPATH", "")

    rendered_clips: list[Path] = []

    for rel_file, scene_name in SCENES:
        print(f"\n=== Rendering {scene_name} ({quality}) ===")
        cmd = [manim_cmd, *flags, rel_file, scene_name]
        subprocess.run(cmd, cwd=anim_dir, env=env, check=True)

        stem = Path(rel_file).stem
        clip_path = anim_dir / "media" / "videos" / stem / res_folder / f"{scene_name}.mp4"
        if not clip_path.exists():
            raise FileNotFoundError(f"Expected rendered clip not found: {clip_path}")
        rendered_clips.append(clip_path)

    concat_list = anim_dir / "media" / "concat_list.txt"
    concat_list.parent.mkdir(parents=True, exist_ok=True)
    with concat_list.open("w", encoding="utf-8") as fh:
        for clip in rendered_clips:
            fh.write(f"file '{clip.as_posix()}'\n")

    final_mp4 = output_dir / "final_video.mp4"
    print(f"\n=== Concatenating {len(rendered_clips)} scenes into {final_mp4} ===")
    subprocess.run(
        [
            "ffmpeg",
            "-y",
            "-f",
            "concat",
            "-safe",
            "0",
            "-i",
            str(concat_list),
            "-c",
            "copy",
            str(final_mp4),
        ],
        check=True,
    )
    print(f"\nDone! Final video written to: {final_mp4}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Render M3 Span, Basis and Dimension video.")
    parser.add_argument(
        "--quality",
        choices=list(QUALITY_FLAGS.keys()),
        default="high",
        help="Manim render quality (default: high = 1080p60).",
    )
    args = parser.parse_args()
    render_all(args.quality)


if __name__ == "__main__":
    main()
