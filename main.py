import pygame
import pygame_gui
from modules.windows.main_window import *
from modules.windows.conversion_selection_window import *
from modules.windows.download_window import *

#initializing pygame
pygame.init()

#setting up app metadata
window_title = 'YouTube to Local Media'
window_size = (800, 500)
fps = 30
clock = pygame.time.Clock()

#setting up the screen
screen = pygame.display.set_mode(window_size)

def download_window(window_size, window_title, clock, fps, screen, result):
    DownloadWindow(window_size, window_title, clock, fps, screen, result).run()

def selection_window(window_size, window_title, clock, fps, screen, url):
    result = SelectionWindow(window_size, window_title, clock, fps, screen, url).run()
    download_window(window_size, window_title, clock, fps, screen, result)

def main_window(window_size, window_title, clock, fps, screen):
    data = MainWindow(window_size, window_title, clock, fps, screen).run()
    selection_window(window_size, window_title, clock, fps, screen, data)


main_window(window_size, window_title, clock, fps, screen)
