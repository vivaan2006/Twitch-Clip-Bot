import os
import subprocess

RAW_DIR = "../raw"
OUT_DIR = "../output"


def convert_clip(input_path, output_path):
    # ffmpeg command:
    # - crop to vertical
    # - scale to 1080x1920
    # - add padding if needed
    # - limit duration to 59 seconds

    command = [
        "ffmpeg",
        "-i", input_path,
        "-vf",
        "scale=1080:1920:force_original_aspect_ratio=decrease,"
        "pad=1080:1920:(ow-iw)/2:(oh-ih)/2",
        "-t", "59",
        "-c:a", "copy",
        output_path
    ]
    print(f"🎞 Converting: {input_path}")
    subprocess.run(command, check=True)
    print(f"✅ Saved to: {output_path}")

def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    for file in os.listdir(RAW_DIR):
        if file.endswith(".mp4"):
            input_path = os.path.join(RAW_DIR, file)
            output_file = f"formatted_{file}"
            output_path = os.path.join(OUT_DIR, output_file)

            try:
                convert_clip(input_path, output_path)
            except Exception as e:
                print(f"❌ Error converting {file}: {e}")

if __name__ == "__main__":
    main()

