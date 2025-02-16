import pygame
import pygame_gui
import threading
import sys
import os
import re
import unicodedata
from modules.data_handlers.pygame_obj_generator import *
from modules.data_handlers.fetch_resource import *
from  modules.functionality.convert_to_media import *
from modules.functionality.identify_video_information import *

class DownloadWindow:
    def __init__(self,window_size, window_title, clock, fps, screen, conversion_data:dict):
        #fetching app metadata
        self.window_title = window_title
        self.window_size = window_size
        self.clock = clock
        self.fps = fps
        self.time_delta = self.clock.tick(self.fps)/1000.0
        self.status = False
        self.downloading = False

        #media metadata
        self.conversion_data = conversion_data
        self.file_type = self.conversion_data.get('File_type')
        self.path = self.conversion_data.get('Path')
        self.video_url = self.conversion_data.get('Video_URL')
        
        #setting up screen
        self.screen = screen
        pygame.display.set_caption(self.window_title)
        #fetching resources
        self.resources = fetch(path='resources/icons').begin()

        #setting up GUI manager and GUI generator
        self.gui_manager = pygame_gui.UIManager(window_size, theme_path='resources/themes/download_window_theme.json')
        self.gui_generator = GenerateUI(self.gui_manager)

        #setting up loop boolean
        self.running = True

        #generating logo
        self.logo = GenerateRect(scale=(400,200), position=(400,110), pygame_object=self.resources[3])
        self.logo_scaled = self.logo.scaled()
        self.logo_rect = self.logo.rect()

        #generating GUI elements
        self.starting_text_fetching_log = "<font face='verdana' color='#5500FF' size=3.5><b>Fetching Log</b></font><br>"
        self.fetch_progress_log = []
        self.progress_bar = self.gui_generator.progressbar(position=(20,self.window_size[1]//2+100), dimension=(self.window_size[0]-30, 50), id='#progress_bar')
        self.fetching_log = self.gui_generator.text_box(position=(20,self.window_size[1]//2), dimension=(self.window_size[0]-30, 200), id='#fetch_log', html_text=self.starting_text_fetching_log)
        
        self.download_label = self.gui_generator.label(position=(10, 300), dimension=(350,50), text=f'Downloading YoutTube Video as {self.file_type}...', id='#download_label')
        self.progress_bar.hide()
        self.download_label.hide()

    def run(self):
        #initialize threads
        fetch_link_metadata = threading.Thread(target=self.fetch_link_metadata)
        download_single_video_thread = threading.Thread(target=self.download_single_video)
        download_playlist_thread = threading.Thread(target=self.download_playlist)

        fetch_link_metadata.start()

        while self.running:
            #quit the program if done 
            if self.status:
                self.running = False
                pygame.quit()
                sys.exit()

            #running download threads if fetching thread is done
            try:
                if fetch_link_metadata.is_alive() == False and self.downloading == False and self.link_type == "Video":
                        #start converting and downloading single Video
                        self.download_label.show()
                        self.progress_bar.show()
                        self.fetching_log.hide()
                        download_single_video_thread.start()

                elif fetch_link_metadata.is_alive() == False and self.downloading == False and self.link_type == "Playlist":
                        #start converting and downloading Videos in provided playlist link
                        self.download_label.show()
                        self.progress_bar.show()
                        self.fetching_log.hide()
                        download_playlist_thread.start()
            except:
                pass

            #updating fetch log
            while self.fetch_progress_log:
                msg = self.fetch_progress_log.pop(0)
                self.fetching_log.append_html_text(msg)  

            #render objects
            self.screen.fill((0,0,0))
            self.screen.blit(self.logo_scaled, self.logo_rect)
            self.gui_manager.update(self.time_delta)
            self.gui_manager.draw_ui(self.screen)

            pygame.display.flip()
            pygame.display.update()

            #event handler
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()
                
                self.gui_manager.process_events(event)

    def download_single_video(self):
        try:
            self.downloading = True
            if self.file_type == 'Mp3':
                Convert(self.video_url, self.path, self.progress_bar).Mp3()

            elif self.file_type == 'Mp4':
                Convert(self.video_url, self.path, self.progress_bar).Mp4()
            
            self.status = True
        except:
            self.gui_generator.message_window(position=(300,150), dimension=(100,200), id='#warning',window_title='Alert', always_on_top=True,html_message=f'the process timed out, try again')
    
    def download_playlist(self):
        try:
            self.downloading = True
            path = os.path.join(self.path, self.sanitize_filenames(self.title))
            converted_videos = 0

            for video_url in self.url:
                #check desired file type
                if self.file_type == 'Mp3':
                    Convert(video_url, path, self.progress_bar).Mp3()
                elif self.file_type == 'Mp4':
                    Convert(video_url, path, self.progress_bar).Mp4()
                
                converted_videos += 1

                #updating label and resetting progress bar
                self.download_label.set_text(f'Downloadied {converted_videos} of {len(self.url)} Videos in the playlist as {self.file_type}...')
                self.progress_bar.set_current_progress(0)

                if self.running == False:
                    break

            self.status = True
        except:
            self.gui_generator.message_window(position=(300,150), dimension=(100,200), id='#warning',window_title='Alert', always_on_top=True,html_message=f'the process timed out, try again')
    
    def fetch_link_metadata(self):
        try:
            link_metadata = LinkInformation(self.video_url, self.fetch_progress_log).get_metadata()

            self.link_type = link_metadata.get('Type')
            self.title = link_metadata.get('Title')
            self.url = link_metadata.get('Url')
        except:
            self.gui_generator.message_window(position=(300,150), dimension=(100,200), id='#warning',window_title='Alert', always_on_top=True,html_message=f'something went wrong during the fetching process check the fetching log for more details and try again')

    def sanitize_filenames(self, filename):
        # Remove invalid characters
        filename = re.sub(r'[<>:"/\\|?*\n\r\t]', '', filename)
        
        # Normalize Unicode (fixes hidden characters)
        filename = unicodedata.normalize("NFKD", filename)
        
        # Remove leading/trailing spaces
        filename = filename.strip()
        
        # Ensure filename is not a reserved Windows name
        reserved_names = {"CON", "PRN", "AUX", "NUL",
                        "COM1", "COM2", "COM3", "COM4", "COM5", "COM6", "COM7", "COM8", "COM9",
                        "LPT1", "LPT2", "LPT3", "LPT4", "LPT5", "LPT6", "LPT7", "LPT8", "LPT9"}
        
        if filename.upper() in reserved_names:
            filename += "_safe" 

        
        return filename
