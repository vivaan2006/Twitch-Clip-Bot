# Twitch Clip Bot 🎥⚡️

Automatically downloads trending Twitch clips, formats them for short-form platforms, adds on-screen titles, and burns in AI-generated subtitles — all in one pipeline.

## ✨ Features

- 📥 Download trending Twitch clips
- 🧹 Crop and reformat clips for TikTok, Shorts, Reels
- 🖋️ Add bold, auto-generated titles using `ffmpeg`
- 💬 Generate and burn subtitles using OpenAI Whisper
- 🧠 Clean, modular pipeline structure
- 🖥️ Works fully locally — no cloud costs!

## 🛠️ Installation

```bash
git clone https://github.com/vivaan2006/Twitch-Clip-Bot.git
cd Twitch-Clip-Bot
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt