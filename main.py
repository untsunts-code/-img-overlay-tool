from src.overlay import add_overlay

if __name__ == "__main__":
    add_overlay(
        base_path="overlays/base.jpg",
        overlay_path="overlays/icon.png",
        output_path="output/result.png",
        position=(50, 50),
        size=(180, 180),
        opacity=180
    )

