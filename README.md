# Span, Basis and Dimension — How Vectors Build a Space

- **Student Name:** Harsh Sharma
- **Student ID:** `E25B070618`
- **Course:** Linear Algebra and Calculus (M3) — Internal Assessment
- **Format:** 1920 × 1080 (16:9), MP4, 4m 42s

---

## Repository Deliverables

| Deliverable | File / Folder | Description |
| :--- | :--- | :--- |
| **1. Final Video** | [`M3_AnimationVideo_Span-basis-and-dimension_E25B070618_Video.mp4`](M3_AnimationVideo_Span-basis-and-dimension_E25B070618_Video.mp4) | 1080p 16:9 MP4 with Opening Frame (Title, Concept, Name & ID) and Closing Frame (Summary & Credits) |
| **2. Source Code** | [`M3_AnimationVideo_Span-basis-and-dimension_E25B070618_Code/`](M3_AnimationVideo_Span-basis-and-dimension_E25B070618_Code/) | Complete Python / Manim Community Edition scripts for all 6 scenes |
| **3. Storyboard** | [`M3_AnimationVideo_Span-basis-and-dimension_E25B070618_Storyboard.pdf`](M3_AnimationVideo_Span-basis-and-dimension_E25B070618_Storyboard.pdf) | Six-scene visual and mathematical storyboard |
| **4. Documentation** | [`README.md`](README.md) & [`credits/credits.md`](credits/credits.md) | Setup, rendering instructions, and AI-tool disclosure |

---

## Six-Scene Structure (~4:42)

| Scene | Title | Duration | File |
| :--- | :--- | :--- | :--- |
| 1 | Opening Frame, Hook & Introduction | ~32s | `scenes/scene1_intro.py` |
| 2 | Understanding Span | ~58s | `scenes/scene2_span.py` |
| 3 | Linear Independence & Dependence | ~54s | `scenes/scene3_independence.py` |
| 4 | Understanding Basis | ~67s | `scenes/scene4_basis.py` |
| 5 | Understanding Dimension | ~56s | `scenes/scene5_dimension.py` |
| 6 | Summary & Closing Credits | ~15s | `scenes/scene6_summary.py` |

---

## How to Render the Animation

### 1. System Dependencies (macOS via Homebrew)
```bash
brew install ffmpeg cairo pango pkg-config
```

### 2. Python Virtual Environment
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r M3_AnimationVideo_Span-basis-and-dimension_E25B070618_Code/requirements.txt
```

### 3. Render All Scenes (1080p MP4)
```bash
python M3_AnimationVideo_Span-basis-and-dimension_E25B070618_Code/main.py --quality high
```
