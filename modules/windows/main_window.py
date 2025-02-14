import pygame
import pygame_gui
from urllib.parse import urlparse
from modules.data_handlers.pygame_obj_generator import *
from modules.data_handlers.fetch_resource import *


class MainWindow:
    def __init__(self,window_size, window_title, clock, fps, screen):
        #fetching app metadata
        self.window_title = window_title
        self.window_size = window_size
        self.clock = clock
        self.fps = fps
        self.time_delta = self.clock.tick(self.fps)/1000.0 

        #setting up screen
        self.screen = screen
        pygame.display.set_caption(self.window_title)

        #fetching resources
        self.resources = fetch(path='resources/icons').begin()

        #setting up GUI manager and GUI generator
        self.gui_manager = pygame_gui.UIManager(window_size, 'resources/themes/main_window_theme.json')
        self.gui_generator = GenerateUI(self.gui_manager)

        #setting up loop boolean
        self.running = True

        #generating logo
        self.logo = GenerateRect(scale=(400,200), position=(400,110), pygame_object=self.resources[3])
        self.logo_scaled = self.logo.scaled()
        self.logo_rect = self.logo.rect()

        #generating GUI elements
        self.search_bar = self.gui_generator.searchbar(position=(150, 250), dimension=(500, 50), id='#search_bar')
        self.convert_button = self.gui_generator.button(position=(250, 350), dimension=(300, 50), id='#convert_button', text='', tool_tip='Convert the YouTube Video to either Mp3 or Mp4')

    def run(self):

        while self.running:

            #render objects
            self.screen.fill((0,0,0))
            self.screen.blit(self.logo_scaled, self.logo_rect)
            self.gui_manager.update(self.time_delta)
            self.gui_manager.draw_ui(self.screen)

            pygame.display.flip()

            #event handler
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.convert_button.disable()
                        url = self.get_url()
                        if url:
                            return url
                        else:
                            self.message_window =self.gui_generator.message_window(position=(300,150), dimension=(100,200), id='#warning', window_title='Alert!', always_on_top=True, html_message='The string sent is not a valid YouTube link, Try Again')
                            

                if event.type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == self.convert_button:
                        self.convert_button.disable()
                        url = self.get_url()
                        if url:
                            return url
                        else:
                            self.message_window = self.gui_generator.message_window(position=(300,150), dimension=(100,200), id='#warning', window_title='Alert!', always_on_top=True, html_message='The string sent is not a valid YouTube link, Try Again')
                
                if event.type == pygame_gui.UI_WINDOW_CLOSE and event.ui_element == self.message_window:
                    self.convert_button.enable()
                
                self.gui_manager.process_events(event)

    def get_url(self):
        result =self.search_bar.get_text()
        parsed_url = urlparse(result)
        if parsed_url.netloc in ["www.youtube.com", "youtube.com", "youtu.be"]:
            self.running = False
            return result

        