import time
import pyperclip
import certifi

import ssl
import yt_dlp

def download_video_as_mp4(video_url, output_path='music/'):
    options = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4',
        'outtmpl': f'{output_path}%(title)s.%(ext)s',
        'external_downloader_args': ['-e', 'youtube_dl'],
    }

    with yt_dlp.YoutubeDL(options) as ydl:
        info_dict = ydl.extract_info(video_url, download=False)
        video_title = info_dict.get('title', 'Video')
        print(f'Downloading: {video_title}')
        ydl.download([video_url])

def custom_clipboard_monitor():
    previous_clipboard_content = pyperclip.paste()
    
    while True:
        print('awaiting clipboard change')
        system_clipboard_content = pyperclip.paste()
        if system_clipboard_content != previous_clipboard_content:
            print("Updated clipboard content:", system_clipboard_content)
            download_video_as_mp4(system_clipboard_content)
            print('Download Successful')
            previous_clipboard_content = system_clipboard_content

        time.sleep(1)

if __name__ == "__main__":
    custom_clipboard_monitor()

