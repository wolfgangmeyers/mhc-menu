from PIL import Image
import os

# Input video file
video_file = r"C:\Users\wolfg\Downloads\grok-video-30f1ea0b-e13a-40ad-bdd2-f19266fcf2c9.mp4"

# Create output directory for drink frames (raw, no background removal)
output_dir = "drink_frames_raw"
os.makedirs(output_dir, exist_ok=True)

print("Extracting frames from drink fairy video (no background removal)...")

try:
    import imageio.v3 as iio

    print(f"Processing video: {video_file}")

    # Read video metadata
    props = iio.improps(video_file)
    print(f"Video properties: {props}")

    frame_count = 0

    # Read ALL frames (no skipping)
    for frame_idx, frame in enumerate(iio.imiter(video_file)):
        # Convert to PIL Image
        img = Image.fromarray(frame)

        # Resize to 512px width (maintaining aspect ratio)
        new_width = 512
        aspect_ratio = img.height / img.width
        new_height = int(new_width * aspect_ratio)
        resized_img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)

        # Save frame (no background removal)
        output_path = os.path.join(output_dir, f"frame_{frame_count:04d}.png")
        resized_img.save(output_path)

        frame_count += 1

        if frame_count % 10 == 0:
            print(f"  Processed {frame_count} frames...")

    print(f"\nDone! Extracted {frame_count} frames.")
    print(f"Output saved to: {output_dir}/")

except ImportError:
    print("ERROR: imageio not available.")
    print("Please install it: pip install imageio")
