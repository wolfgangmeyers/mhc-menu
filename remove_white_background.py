from PIL import Image
import os

# Directory containing frames
frames_dir = "santa_frames"

# Get all frame files
frame_files = sorted([f for f in os.listdir(frames_dir) if f.endswith(".png")])

print(f"Found {len(frame_files)} frames to process")
print("Removing white backgrounds and making them transparent...")

# Process each frame
for idx, frame_file in enumerate(frame_files):
    file_path = os.path.join(frames_dir, frame_file)

    # Open image
    img = Image.open(file_path)

    # Convert to RGBA if not already
    img = img.convert("RGBA")

    # Get pixel data
    data = img.getdata()

    # Create new pixel data with white pixels made transparent
    new_data = []
    for item in data:
        # If pixel is white or near-white (RGB values all > 200), make it transparent
        # We use 200 threshold to catch light gray/off-white backgrounds
        if item[0] > 200 and item[1] > 200 and item[2] > 200:
            # Make transparent (alpha = 0)
            new_data.append((255, 255, 255, 0))
        else:
            # Keep original pixel
            new_data.append(item)

    # Update image with new data
    img.putdata(new_data)

    # Save back to same file
    img.save(file_path, "PNG")

    if (idx + 1) % 20 == 0:
        print(f"  Processed {idx + 1}/{len(frame_files)} frames...")

print(f"\nDone! Processed {len(frame_files)} frames.")
print(f"All white backgrounds have been made transparent.")
