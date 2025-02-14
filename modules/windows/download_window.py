import pygame
import pygame_gui
import threading
import sys
from modules.data_handlers.pygame_obj_generator import *
from modules.data_handlers.fetch_resource import *
from  modules.functionality.convert_to_media import *

class DownloadWindow:
    def __init__(self,window_size, window_title, clock, fps, screen, conversion_data:dict):
        #fetching app metadata
        self.window_title = window_title
        self.window_size = window_size
        self.clock = clock
        self.fps = fps
        self.time_delta = self.clock.tick(self.fps)/1000.0
        self.status = False

        #media metadata
        self.conversion_data = conversion_data
        self.file_type = self.conversion_data.get('File_type')
        self.path = self.conversion_data.get('Path')
        self.link_metadata = self.conversion_data.get('Link_metadata')

        #link metadata
        self.link_type = self.link_metadata.get('Type')
        self.title = self.link_metadata.get('Title')
        self.url = self.link_metadata.get('Url')

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
        self.progress_bar = self.gui_generator.progressbar(position=(20,self.window_size[1]//2+100), dimension=(self.window_size[0]-30, 50), id='#progress_bar')
        self.download_label = self.gui_generator.label(position=(10, 300), dimension=(350,50), text=f'Downloading YoutTube Video as {self.file_type}...', id='#download_label')


    def run(self):
        if self.link_type == "Video":
            #start converting and downloading single Video
            download_thread = threading.Thread(target=self.download_single_video)
            download_thread.start()
        elif self.link_type == "Playlist":
            #start converting and downloading Videos in provided playlist link
            download_thread = threading.Thread(target=self.download_playlist)
            download_thread.start()

        while self.running:

            #render objects
            self.screen.fill((0,0,0))
            self.screen.blit(self.logo_scaled, self.logo_rect)
            self.gui_manager.update(self.time_delta)
            self.gui_manager.draw_ui(self.screen)

            pygame.display.flip()

            if self.status:
                self.download_thread.join()
                self.running = False
                pygame.quit()
                sys.exit()

            #event handler
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()
                
                self.gui_manager.process_events(event)

    
    def download_single_video(self):
        if self.file_type == 'Mp3':
            Convert(self.url, self.path, self.progress_bar).Mp3()

        elif self.file_type == 'Mp4':
            Convert(self.url, self.path, self.progress_bar).Mp4()
        
        self.status = True
    
    def download_playlist(self):
        path = os.path.join(self.path, self.title)
        converted_videos = 0
        for video_url in self.url:
            if self.file_type == 'Mp3':
                Convert(video_url, path, self.progress_bar).Mp3()
            elif self.file_type == 'Mp4':
                Convert(video_url, path, self.progress_bar).Mp4()
            
            converted_videos += 1
            self.download_label.set_text(f'Downloadied {converted_videos} of {len(self.url)} Videos in the playlist as {self.file_type}...', id='#download_label')
            self.progress_bar.set_current_progress(0)

            if self.running == False:
                break

        self.status = True

