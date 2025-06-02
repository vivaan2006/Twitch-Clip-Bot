import os
import subprocess

OUT_DIR = "output"
TITLED_DIR = "output/titled"

def add_title(input_path, output_path, title_text):
    command = [
        "/usr/local/bin/ffmpeg",
        "-i", input_path,
        "-vf",
        f"drawtext=text='{title_text}':fontfile=/Library/Fonts/Arial.ttf:fontcolor=white:fontsize=60:"
        f"x=(w-text_w)/2:y=100:box=1:boxcolor=black@0.6:boxborderw=10",
        "-c:v", "libx264", "-preset", "fast", "-crf", "23",
        "-c:a", "aac", "-b:a", "128k",
        "-movflags", "+faststart",
        output_path,
        "-y"
    ]
    print(f"📝 Adding title: '{title_text}' to {input_path}")
    subprocess.run(command, check=True)
    print(f"✅ Titled clip saved to {output_path}")

def main():
    os.makedirs(TITLED_DIR, exist_ok=True)

    for file in os.listdir(OUT_DIR):
        if file.endswith(".mp4") and not file.startswith("titled_"):
            input_path = os.path.join(OUT_DIR, file)
            base_title = file.replace(".mp4", "").replace("_", " ")
            title_text = base_title[:40]
            output_path = os.path.join(TITLED_DIR, f"titled_{file}")
            try:
                add_title(input_path, output_path, title_text)
            except Exception as e:
                print(f"❌ Error on {file}: {e}")

if __name__ == "__main__":
    main()
