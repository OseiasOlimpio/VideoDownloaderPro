import yt_dlp
import os
from downloader.ffmpeg_service import compress

def download(url, progress_callback, mode, preset):

    output = "%(title)s.%(ext)s"

    def hook(d):
        if d['status'] == 'downloading':
            total = d.get('total_bytes') or d.get('total_bytes_estimate')
            downloaded = d.get('downloaded_bytes', 0)
    
            if total:
                percent = downloaded / total * 100
            else:
                percent = 0
    
            progress_callback({
                "status": "downloading",
                "percent": percent,
                "filename": os.path.basename(d.get("filename", "")),
                "eta": d.get('_eta_str', '')
            })
    
        elif d['status'] == 'finished':
            progress_callback({"status": "processing"})

    if mode == "mp3":
        ydl_opts = {
            'format': 'bestaudio',
            'outtmpl': output,
            'progress_hooks': [hook],
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        progress_callback({
            "status": "finished",
            "path": os.getcwd()
        })

    else:
        temp_file = "temp_video.mp4"

        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': temp_file,
            'merge_output_format': 'mp4',
            'progress_hooks': [hook],
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        final_name = "video_comprimido.mp4"
        compress(temp_file, final_name, preset)
        os.remove(temp_file)

        progress_callback({
            "status": "finished",
            "path": os.getcwd()
        })
