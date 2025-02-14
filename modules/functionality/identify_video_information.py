import yt_dlp

class LinkInformation:
    def __init__(self, url):
        self.url = url
    
    def get_metadata(self):
        print('works here')
        ydl_opts = {
            'quiet': True,
            'no_warnings': True,
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

        
        
    
