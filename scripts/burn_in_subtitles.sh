#!/usr/bin/env bash
set -e

# 1) Ensure output/final/ exists
mkdir -p output/final

# 2) Loop over every titled *.mp4
for TT in output/titled/titled_formatted_*.mp4; do
  NAME=$(basename "$TT")
  STRIPPED="${NAME#titled_}"                   # drop "titled_"
  SRT_NAME="${STRIPPED%.mp4}.srt"              # change .mp4 → .srt
  SRC_SRT="output/subtitled/${SRT_NAME}"
  OUT_VIDEO="output/final/${NAME}"

  echo "Burning subtitles into: $TT"
  echo "  ↳ using subtitles: $SRC_SRT"
  echo "  ↳ writing output:  $OUT_VIDEO"

  # 3) Escape any single quotes in the .srt path:
  ESCAPED_SRT="${SRC_SRT//\'/\'\\\'\'}"

  ffmpeg -i "$TT" \
         -vf "subtitles='$ESCAPED_SRT'" \
         -c:v libx264 -preset fast -crf 23 \
         -c:a copy \
         "$OUT_VIDEO" \
         -y
done

echo "✅ All videos with burned‐in subtitles are now in output/final/"
