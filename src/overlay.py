import os
import random
from PIL import Image

def add_overlay(base_path, overlay_path, output_path, position=(0, 0), size=(150, 150), opacity=255):
    base_img = Image.open(base_path).convert("RGBA")
    overlay_img = Image.open(overlay_path).convert("RGBA")
    
    overlay_img = overlay_img.resize(size)
    overlay_img.putalpha(opacity)
    
    base_img.paste(overlay_img, position, overlay_img)
    base_img.save(output_path)

def process_batch_images(base_dir, icon_dir, output_dir, size=(180, 180), alpha=200, padding=30):
    base_files = [f for f in os.listdir(base_dir) if f.endswith((".jpg", ".png"))]
    icon_files = [f for f in os.listdir(icon_dir) if f.endswith(".png")]

    os.makedirs(output_dir, exist_ok=True)

    def get_position(corner, base_size, icon_size, padding):
        bw, bh = base_size
        iw, ih = icon_size
        return {
            "bottom-left": (padding, bh - ih - padding),
            "bottom-right": (bw - iw - padding, bh - ih - padding),
        }[corner]

    for base_name, icon_name in zip(base_files, random.sample(icon_files * len(base_files), len(base_files))):
        base_path = os.path.join(base_dir, base_name)
        icon_path = os.path.join(icon_dir, icon_name)
        output_name = base_name.replace(".", "_with_overlay.", 1)
        output_path = os.path.join(output_dir, output_name)

        base_img = Image.open(base_path).convert("RGBA")
        overlay_img = Image.open(icon_path).convert("RGBA")

        overlay_img = overlay_img.resize(size)
        overlay_img.putalpha(alpha)

        corner = random.choice(["bottom-left", "bottom-right"])
        pos = get_position(corner, base_img.size, overlay_img.size, padding)

        base_img.paste(overlay_img, pos, overlay_img)
        base_img.save(output_path)

        print(f"Overlayed {icon_name} onto {base_name} at {corner}, saved to {output_path}")

