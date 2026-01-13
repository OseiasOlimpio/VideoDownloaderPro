import subprocess
import os
import sys

def ffmpeg_path():
    base = getattr(sys, '_MEIPASS', os.path.abspath("."))
    return os.path.join(base, "ffmpeg", "ffmpeg.exe")

PRESETS = {
    "alta": "18",
    "media": "22",
    "leve": "26"
}

def compress(input_file, output_file, preset):
    subprocess.run([
        ffmpeg_path(),
        "-i", input_file,
        "-c:v", "libx264",
        "-preset", "slow",
        "-crf", PRESETS[preset],
        "-c:a", "aac",
        "-b:a", "128k",
        output_file
    ], creationflags=subprocess.CREATE_NO_WINDOW)