import yt_dlp
import re 
import os

class Convert:
    def __init__(self, media_url:str , path:str, progress_bar=None):
        self.media_url= media_url
        self.media_title = self.get_video_title(media_url)
        self.path = path
        self.progress = 0
        self.progress_bar = progress_bar
    
    def progress_hook(self, d):
        if d['status'] == 'downloading':
            percent_str = d['_percent_str']

            # Remove ANSI escape codes
            percent_str = re.sub(r'\x1b\[[0-9;]*m', '', percent_str)

            # Remove extra spaces and percentage sign, then convert to int
            percent_str = percent_str.strip().replace('%', '')
            self.progress = int(float(percent_str))
            
            self.progress_bar.set_current_progress(self.progress)
            

    def Mp3(self):
        ydl_opts = {
            'outtmpl': f'{self.path}/{self.media_title}.%(ext)s',
            'format': 'bestvideo+bestaudio/best',
            'merge_output_format': 'mp4',
            'quiet': True,
            'no_warnings': True,
            'progress_hooks': [self.progress_hook],
            'postprocessors' : [{
                'key': 'FFmpegExtractAudio',   
                'preferredcodec': 'mp3',       
                'preferredquality': '192',    
            }],
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([self.media_url])
        
        return
        
    
    def Mp4(self):
        check_available_audio_and_video = self.get_format_with_audio_and_video(self.media_url)
        ydl_opts = {
                'cookies-from-browser': 'chrome',
                'outtmpl': f'{self.path}/{self.media_title}.%(ext)s',
                'format': check_available_audio_and_video[0],
                'quiet': True,
                'no_warnings': True,
                'progress_hooks': [self.progress_hook],
                'subtitleslangs': ['en'],
                'writesubtitles': True,
                'subtitlesformat': 'srt',
                'postprocessors': [{
                    'key': 'FFmpegVideoConvertor',
                    'preferedformat': 'mp4'
                }]
            }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([self.media_url])

        return
    
    def get_video_title(self, url):
        ydl_opts = {
            'quiet': True,
            'no_warnings': True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            return info.get('title', 'Unknown Title')
    
    def get_format_with_audio_and_video(self, url):
        available_formats = []
        ydl_opts = {'quiet': True}

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False) 

        formats = info.get('formats', [])

        for fmt in formats:
            if fmt.get('ext') == 'mp4' and fmt.get('acodec') != 'none' and fmt.get('vcodec') != 'none':
                available_formats.append(fmt['format_id'])

        return available_formats