from PIL import Image

def add_overlay(base_path, overlay_path, output_path, position=(0, 0), size=(150, 150), opacity=255):
    base_img = Image.open(base_path).convert("RGBA")
    overlay_img = Image.open(overlay_path).convert("RGBA")
    
    overlay_img = overlay_img.resize(size)
    overlay_img.putalpha(opacity)
    
    base_img.paste(overlay_img, position, overlay_img)
    base_img.save(output_path)

