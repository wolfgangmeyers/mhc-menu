from PIL import Image
import subprocess
import os
import json

# Input video file
video_file = "dreamina-2025-10-12-3065-The fairy is smiling and waving to the v....mp4"

# Create output directory
output_dir = "frames"
os.makedirs(output_dir, exist_ok=True)

print("Attempting to extract frames using available tools...")

# Try using Windows Media Foundation or other available video tools
# Let's use a different approach - extract with imageio if available
try:
    import imageio.v3 as iio

    print(f"Processing video: {video_file}")

    # Read video metadata
    props = iio.improps(video_file)
    print(f"Video properties: {props}")

    frame_count = 0

    # Read frames one by one
    for frame_idx, frame in enumerate(iio.imiter(video_file)):
        # Convert to PIL Image
        img = Image.fromarray(frame)

        # Get dimensions
        width, height = img.size

        # Crop to top half
        cropped_img = img.crop((0, 0, width, height // 2))

        # Resize to 512px width (maintaining aspect ratio)
        new_width = 512
        aspect_ratio = cropped_img.height / cropped_img.width
        new_height = int(new_width * aspect_ratio)
        resized_img = cropped_img.resize((new_width, new_height), Image.Resampling.LANCZOS)

        # Save frame
        output_path = os.path.join(output_dir, f"frame_{frame_count:04d}.png")
        resized_img.save(output_path)

        frame_count += 1

        if frame_count % 10 == 0:
            print(f"  Processed {frame_count} frames...")

    print(f"\nDone! Processed {frame_count} frames.")
    print(f"Output saved to: {output_dir}/")

except ImportError:
    print("imageio not available. Trying alternative method...")

    # Check if ffmpeg might be available in a different location
    try:
        result = subprocess.run(['where', 'ffmpeg'], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"Found ffmpeg at: {result.stdout.strip()}")
            print("Please run this command manually:")
            print(f'ffmpeg -i "{video_file}" -vf "crop=iw:ih/2:0:0,scale=512:-1" {output_dir}/frame_%04d.png')
        else:
            print("ffmpeg not found in PATH")
    except Exception as e:
        print(f"Could not locate ffmpeg: {e}")

    print("\nPlease install one of these packages:")
    print("  pip install imageio")
    print("  or")
    print("  pip install opencv-python")
