from PIL import Image
import os

# Directory containing drink frames
frames_dir = "drink_frames"

# Get all PNG files
png_files = sorted([f for f in os.listdir(frames_dir) if f.endswith(".png")])

print(f"Found {len(png_files)} PNG frames")
print("Creating drink fairy sprite sheet...")

# Load first image to get dimensions
first_img = Image.open(os.path.join(frames_dir, png_files[0]))
frame_width, frame_height = first_img.size

print(f"Frame dimensions: {frame_width}x{frame_height}")

# Create sprite sheet (horizontal layout - single row)
sprite_width = frame_width * len(png_files)
sprite_height = frame_height

print(f"Horizontal layout: {len(png_files)} frames in a single row")
print(f"Sprite sheet dimensions: {sprite_width}x{sprite_height}")

# Create new image for sprite sheet
sprite_sheet = Image.new('RGBA', (sprite_width, sprite_height), (0, 0, 0, 0))

# Paste each frame into the sprite sheet horizontally
for idx, png_file in enumerate(png_files):
    img = Image.open(os.path.join(frames_dir, png_file))

    x_offset = idx * frame_width
    y_offset = 0

    sprite_sheet.paste(img, (x_offset, y_offset))

    if (idx + 1) % 20 == 0:
        print(f"  Processed {idx + 1}/{len(png_files)} frames...")

# Save sprite sheet as PNG (new file: fairy-sprite-drink.png)
output_path = "fairy-sprite-drink.png"
sprite_sheet.save(output_path, "PNG", optimize=True)

file_size = os.path.getsize(output_path)
print(f"\nDone! Sprite sheet saved to: {output_path}")
print(f"File size: {file_size / 1024:.1f} KB ({file_size / 1024 / 1024:.2f} MB)")
print(f"Total frames: {len(png_files)}")
