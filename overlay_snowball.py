from PIL import Image
import os

# Paths
overlay_path = "snowball-overlay.png"
frames_dir = "winter_frames"

# Starting frame number
start_frame = 51

# Overlay size and position
overlay_size = (524, 514)
overlay_position = (10, 204)

print(f"Loading overlay image: {overlay_path}")
overlay_img = Image.open(overlay_path)

# Resize overlay to specified size
overlay_resized = overlay_img.resize(overlay_size, Image.Resampling.LANCZOS)
print(f"Resized overlay to {overlay_size}")

# Get all frame files
all_frames = sorted([f for f in os.listdir(frames_dir) if f.endswith(".png")])

# Filter to frames 51 and onwards
frames_to_process = [f for f in all_frames if int(f.split("_")[1].split(".")[0]) >= start_frame]

print(f"Found {len(frames_to_process)} frames to process (frame_{start_frame:04d} onwards)")
print(f"Overlaying snowball at position {overlay_position}...")

# Process each frame
for idx, frame_file in enumerate(frames_to_process):
    frame_path = os.path.join(frames_dir, frame_file)

    # Open the frame
    frame = Image.open(frame_path)

    # Convert to RGBA to support transparency
    if frame.mode != "RGBA":
        frame = frame.convert("RGBA")

    # Paste the overlay onto the frame at the specified position
    # Using the overlay's alpha channel as mask to preserve transparency
    frame.paste(overlay_resized, overlay_position, overlay_resized if overlay_resized.mode == "RGBA" else None)

    # Save back to the same file
    frame.save(frame_path, "PNG")

    if (idx + 1) % 20 == 0:
        print(f"  Processed {idx + 1}/{len(frames_to_process)} frames...")

print(f"\nDone! Overlaid snowball on {len(frames_to_process)} frames.")
print(f"Frames {start_frame} through {len(all_frames)-1} now have the snowball overlay.")
