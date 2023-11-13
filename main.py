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
        
def install_ffmpeg():
    
    print('Checking for ffmpeg')
    
    #!!!!! The code below doesnt work !!!!!!
    
    
    # try:
    #     subprocess.run(["ffmpeg", "-version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # except FileNotFoundError:
    #     print("ffmpeg not found. Installing...")
    #     subprocess.run(["apt-get", "install", "-y", "ffmpeg"])  #] Change this line based on your package manager
    #     system = platform.system().lower()
        
    #     if system == "linux":
    #         # For Debian-based systems (Ubuntu, etc.)
    #         subprocess.run(["sudo", "apt-get", "install", "-y", "ffmpeg"])
    #     elif system == "darwin":
    #         # For macOS using Homebrew
    #         subprocess.run(["brew", "install", "ffmpeg"])
    #     elif system == "windows":
    #         # For Windows using Chocolatey
    #         subprocess.run(["choco", "install", "ffmpeg"], shell=True)
    #     else:
    #         print("Unsupported operating system. Please install ffmpeg manually.")
            
if __name__ == "__main__":
    # install_ffmpeg()
    custom_clipboard_monitor()
