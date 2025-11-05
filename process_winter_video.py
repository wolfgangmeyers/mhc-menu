from PIL import Image
import os

# Input video file
video_file = r"C:\Users\wolfg\Downloads\grok-video-1083273f-4959-49f4-89d5-82344c01ee1f.mp4"

# Create output directory for winter frames
output_dir = "winter_frames"
os.makedirs(output_dir, exist_ok=True)

print("Extracting frames from winter fairy video...")

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

        # Save frame
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
    print("Or use ffmpeg manually:")
    print(f'ffmpeg -i "{video_file}" -vf "scale=512:-1" {output_dir}/frame_%04d.png')
