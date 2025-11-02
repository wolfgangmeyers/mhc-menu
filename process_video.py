import cv2
import os

# Input video file
video_file = "dreamina-2025-10-12-3065-The fairy is smiling and waving to the v....mp4"

# Create output directory
output_dir = "frames"
os.makedirs(output_dir, exist_ok=True)

# Open video
cap = cv2.VideoCapture(video_file)

if not cap.isOpened():
    print(f"Error: Could not open video file {video_file}")
    exit(1)

# Get video properties
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

print(f"Video properties:")
print(f"  Resolution: {width}x{height}")
print(f"  FPS: {fps}")
print(f"  Total frames: {total_frames}")
print(f"\nProcessing frames...")

frame_count = 0

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Crop to top half
    cropped_height = height // 2
    cropped_frame = frame[0:cropped_height, 0:width]

    # Resize to 512px width (maintaining aspect ratio)
    new_width = 512
    aspect_ratio = cropped_height / width
    new_height = int(new_width * aspect_ratio)
    resized_frame = cv2.resize(cropped_frame, (new_width, new_height))

    # Save frame
    output_path = os.path.join(output_dir, f"frame_{frame_count:04d}.png")
    cv2.imwrite(output_path, resized_frame)

    frame_count += 1

    if frame_count % 10 == 0:
        print(f"  Processed {frame_count}/{total_frames} frames...")

cap.release()

print(f"\nDone! Processed {frame_count} frames.")
print(f"Output saved to: {output_dir}/")
