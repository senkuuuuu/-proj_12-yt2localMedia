import yt_dlp
import re
import time

class LinkInformation:
    def __init__(self, url, progress_log_list):
        self.url = url
        self.progress_log_list = progress_log_list
       
    
    def get_metadata(self):
        
        ydl_opts = {
            'quiet': False,  
            'noprogress': False,  
            'no_warnings': True,
            'logger': Logger(self.progress_log_list)
        }
        
        #fetch info from the video
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(self.url, download=False)

        #check if playlist or single video
        if 'entries' in info:
            print('playlist')
            playlist_name = info.get('title', 'Unknown Playlist')
            video_urls = [entry.get('webpage_url', f"https://www.youtube.com/watch?v={entry['id']}") for entry in info['entries']]
            link_metadata = {
                "Type": "Playlist",
                "Title": playlist_name,
                "Url": video_urls
            }
            print(video_urls)
            return link_metadata
        else:
            print('video')
            video_title = info.get('title', 'Unknown Title')
            link_metadata = {
                "Type":"Video",
                "title": video_title,
                "Url": self.url
            }
            print(link_metadata)
            return link_metadata
    
class Logger:
    def __init__(self, progress_log_list):
        self.progress_log_list = progress_log_list

    def debug(self, msg):
        if any(keyword in msg for keyword in ["Downloading", "Extracting", "Fetching"]):
            time.sleep(1)
            self.progress_log_list.append(f"<br><font face='verdana' color='#0077FF' size=3.5><b>[DEBUG]</b></font> {msg}")  

    def warning(self, msg):
        time.sleep(1)
        self.progress_log_list.append(f"<br><font face='verdana' color='#FF6F00' size=3.5><b>[WARNING]</b></font> {msg}") 
    
    def error(self, msg):
        time.sleep(1)
        self.progress_log_list.append(f"<br><font face='verdana' color='#FF0000' size=3.5><b>[ERROR]</b></font> {msg}")
        
    
        
        
    
