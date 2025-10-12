from PIL import Image
import os

# Directory containing frames
frames_dir = "reduced_frames"

# Get all PNG files
png_files = sorted([f for f in os.listdir(frames_dir) if f.endswith(".png")])

print(f"Found {len(png_files)} PNG files to convert")
print("Converting to WebP format...")

total_png_size = 0
total_webp_size = 0

# Process each frame
for idx, png_file in enumerate(png_files):
    png_path = os.path.join(frames_dir, png_file)
    webp_file = png_file.replace(".png", ".webp")
    webp_path = os.path.join(frames_dir, webp_file)

    # Get original file size
    png_size = os.path.getsize(png_path)
    total_png_size += png_size

    # Open PNG image
    img = Image.open(png_path)

    # Save as WebP with quality setting (80 is good balance between quality and size)
    # lossless=False for smaller file size, quality=80 for good quality
    img.save(webp_path, "WEBP", quality=80, method=6)

    # Get new file size
    webp_size = os.path.getsize(webp_path)
    total_webp_size += webp_size

    # Delete original PNG file
    os.remove(png_path)

    if (idx + 1) % 20 == 0:
        print(f"  Converted {idx + 1}/{len(png_files)} frames...")

print(f"\nDone! Converted {len(png_files)} frames.")
print(f"\nSize comparison:")
print(f"  Original PNG total: {total_png_size / 1024 / 1024:.2f} MB")
print(f"  New WebP total: {total_webp_size / 1024 / 1024:.2f} MB")
print(f"  Space saved: {(total_png_size - total_webp_size) / 1024 / 1024:.2f} MB ({100 * (total_png_size - total_webp_size) / total_png_size:.1f}%)")
print(f"  Average size per frame: {total_webp_size / len(png_files) / 1024:.1f} KB")
