from PIL import Image
import os

# Source and destination directories
source_dir = "winter_frames_raw"
dest_dir = "winter_frames"

# Get all frame files
frame_files = sorted([f for f in os.listdir(source_dir) if f.endswith(".png")])

print(f"Found {len(frame_files)} frames to process")
print("Removing white backgrounds and making them transparent...")

# Process each frame
for idx, frame_file in enumerate(frame_files):
    source_path = os.path.join(source_dir, frame_file)
    dest_path = os.path.join(dest_dir, frame_file)

    # Open image
    img = Image.open(source_path)

    # Convert to RGBA if not already
    img = img.convert("RGBA")

    # Get pixel data
    data = img.getdata()

    # Create new pixel data with white pixels made transparent
    new_data = []
    for item in data:
        # If pixel is very close to pure white (RGB values all > 245), make it transparent
        # Higher threshold (245 instead of 200) to avoid eating away the snowball
        if item[0] > 245 and item[1] > 245 and item[2] > 245:
            # Make transparent (alpha = 0)
            new_data.append((255, 255, 255, 0))
        else:
            # Keep original pixel
            new_data.append(item)

    # Update image with new data
    img.putdata(new_data)

    # Save to destination directory
    img.save(dest_path, "PNG")

    if (idx + 1) % 20 == 0:
        print(f"  Processed {idx + 1}/{len(frame_files)} frames...")

print(f"\nDone! Processed {len(frame_files)} frames.")
print(f"All white backgrounds have been made transparent.")
