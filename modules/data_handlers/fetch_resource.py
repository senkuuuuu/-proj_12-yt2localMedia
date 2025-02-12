import os
import pygame
from modules.data_handlers.executable_file_redirector import *

class fetch:
    def __init__(self, path):
        self.path = convert().get_resource_path(path)
        self.resources = []

    def sprites(self):
        for file in os.listdir(self.path):
            file_path = self.path + "/" + file
            pygame_object = pygame.image.load(file_path)
            self.resources.append(pygame_object)
        return self.resources
    
