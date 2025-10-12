import os
import shutil

# Source and destination directories
source_dir = "frames"
dest_dir = "reduced_frames"

# Create destination directory
os.makedirs(dest_dir, exist_ok=True)

# Get all frame files
frame_files = sorted([f for f in os.listdir(source_dir) if f.startswith("frame_") and f.endswith(".png")])

print(f"Found {len(frame_files)} total frames")
print(f"Selecting every 3rd frame (keeping frames 0, 3, 6, 9, ...)")

# Select every 3rd frame (indices 0, 3, 6, 9, ...)
selected_frames = [frame_files[i] for i in range(0, len(frame_files), 3)]

print(f"Selected {len(selected_frames)} frames")

# Copy selected frames with new sequential numbering
for new_idx, frame_file in enumerate(selected_frames):
    source_path = os.path.join(source_dir, frame_file)
    dest_filename = f"frame_{new_idx:04d}.png"
    dest_path = os.path.join(dest_dir, dest_filename)

    shutil.copy2(source_path, dest_path)

    if (new_idx + 1) % 20 == 0:
        print(f"  Copied {new_idx + 1} frames...")

print(f"\nDone! Copied {len(selected_frames)} frames to {dest_dir}/")
print(f"Frame range: frame_0000.png to frame_{len(selected_frames)-1:04d}.png")
