import pygame
import pygame_gui
import threading
import sys
from modules.data_handlers.pygame_obj_generator import *
from modules.data_handlers.fetch_resource import *
from  modules.functionality.convert_to_media import *

class DownloadWindow:
    def __init__(self,window_size, window_title, clock, fps, screen, media_data):
        #fetching app metadata
        self.window_title = window_title
        self.window_size = window_size
        self.clock = clock
        self.fps = fps
        self.time_delta = self.clock.tick(self.fps)/1000.0
        self.status = False

        #media metadata
        self.media_metadata = media_data
        self.media_url = media_data[0]
        self.path = media_data[1]
        self.file_type = media_data[2]

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

        #start downloading
        self.download_thread = threading.Thread(target=self.download)
        self.download_thread.start()

    def run(self):

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

    
    def download(self):
        if self.file_type == 'Mp3':
            Convert(self.media_url, self.path, self.progress_bar).Mp3()

        elif self.file_type == 'Mp4':
            Convert(self.media_url, self.path, self.progress_bar).Mp4()
        
        self.status = True
