import pygame
import pygame_gui
from modules.data_handlers.pygame_obj_generator import *
from modules.data_handlers.fetch_resource import *


class SelectionWindow:
    def __init__(self,window_size, window_title, clock, fps, screen, url):
        #fetching app metadata
        self.window_title = window_title
        self.window_size = window_size
        self.clock = clock
        self.fps = fps
        self.time_delta = self.clock.tick(self.fps)/1000.0
        self.url = url

        #setting up screen
        self.screen = screen
        pygame.display.set_caption(self.window_title)

        #fetching resources
        self.resources = fetch(path='resources/icons').begin()

        #setting up GUI manager and GUI generator
        self.gui_manager = pygame_gui.UIManager(window_size, 'resources/themes/selection_window_theme.json')
        self.gui_generator = GenerateUI(self.gui_manager)

        #setting up loop boolean
        self.running = True

        #generating logo
        self.logo = GenerateRect(scale=(400,200), position=(400,110), pygame_object=self.resources[3])
        self.logo_scaled = self.logo.scaled()
        self.logo_rect = self.logo.rect()

        #generating GUI elements
        self.Mp3_button = self.gui_generator.button(position=(175, 200), dimension=(200, 250), text='', id='#Mp3_button', tool_tip='Convert YouTube Video into Mp3 format')
        self.Mp4_button = self.gui_generator.button(position=(420, 200), dimension=(200, 250), text='', id='#Mp4_button', tool_tip='Convert YouTube Video into Mp4 format')

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
                
                if event.type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == self.Mp3_button:
                        result = [self.url, 'Mp3']
                        self.running = False
                        return result
                    elif event.ui_element == self.Mp4_button:
                        result = [self.url, 'Mp4']
                        self.running = False
                        return result
                
                self.gui_manager.process_events(event)




