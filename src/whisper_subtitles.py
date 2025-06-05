# src/whisper_subtitles.py

import os
import whisper
import argparse
from pathlib import Path

def transcribe_to_srt(model, video_path: str, srt_path: str, language: str):
    """
    Run Whisper on `video_path` and write a corresponding .srt file at `srt_path`.
    """
    print(f"⏳ Transcribing “{video_path}” → “{srt_path}” …")
    result = model.transcribe(video_path, language=language, fp16=False)

    def format_timestamp(seconds: float) -> str:
        h = int(seconds // 3600)
        m = int((seconds % 3600) // 60)
        s = int(seconds % 60)
        ms = int((seconds - int(seconds)) * 1000)
        return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"

    with open(srt_path, "w", encoding="utf-8") as f:
        for i, segment in enumerate(result["segments"], start=1):
            start_ts = format_timestamp(segment["start"])
            end_ts   = format_timestamp(segment["end"])
            text     = segment["text"].strip()
            f.write(f"{i}\n")
            f.write(f"{start_ts} --> {end_ts}\n")
            f.write(f"{text}\n\n")
    print(f"✅ Wrote subtitles to “{srt_path}”")

def batch_transcribe_dir(input_dir: str, output_dir: str, language: str):
    """
    For each .mp4 in input_dir, generate a matching .srt in output_dir.
    """
    os.makedirs(output_dir, exist_ok=True)
    model = whisper.load_model("small")  # or "base"/"medium" if you prefer

    for filename in os.listdir(input_dir):
        if not filename.lower().endswith(".mp4"):
            continue
        video_path = os.path.join(input_dir, filename)
        base_name  = Path(filename).stem
        srt_path   = os.path.join(output_dir, base_name + ".srt")
        transcribe_to_srt(model, video_path, srt_path, language)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate Whisper‐based SRT subtitles for all .mp4 files in a folder."
    )
    parser.add_argument(
        "--input-dir", required=True,
        help="Directory containing your titled .mp4 files"
    )
    parser.add_argument(
        "--output-dir", required=True,
        help="Directory where .srt files should be written"
    )
    parser.add_argument(
        "--language", default="en",
        help="Language code (e.g. en, es). Default: en"
    )
    args = parser.parse_args()
    batch_transcribe_dir(args.input_dir, args.output_dir, args.language)