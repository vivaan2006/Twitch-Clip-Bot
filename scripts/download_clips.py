import json
import os
import subprocess

RAW_CLIPS_DIR = "../raw/"
CLIPS_JSON_PATH = "../clips/top_clips.json"

def download_clips(clip_url, filename):
    output_path = os.path.join(RAW_CLIPS_DIR, f"{filename}.mp4")
    command = [
        "yt-dlp",
        clip_url,
        "-o", output_path
    ]
    print(f"⬇️ Downloading {clip_url}...")
    subprocess.run(command, check=True)
    print(f"✅ Saved to {output_path}")

def main():
    os.makedirs(RAW_CLIPS_DIR, exist_ok=True)

    with open(CLIPS_JSON_PATH, "r") as f:
        clips = json.load(f)

    for clip in clips:
        clip_url = clip["url"]
        title = clip["title"].replace(" ", "_").replace("/", "_")
        creator = clip["creator_name"]
        filename = f"{creator}_{title[:30]}"

        try:
            download_clips(clip_url, filename)
        except Exception as e:
            print(f"❌ Failed to download {clip_url}: {e}")

if __name__ == "__main__":
    main()