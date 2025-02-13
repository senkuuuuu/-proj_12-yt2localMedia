import pygame
import pygame_gui
from pygame_gui.core import ObjectID
from pygame_gui.elements import UIButton

#creating, editing and generating rect for images
class GenerateRect:
    def __init__(self, scale, position, pygame_object):
        self.scale = scale
        self.position = position
        self.py_object = pygame_object
        self.scaled_object = pygame.transform.scale(self.py_object, self.scale)
    
    def scaled(self):
        return self.scaled_object

    def rect(self):
        object_rect = self.scaled_object.get_rect(center = self.position)
        return object_rect

#creating, editing and generating rect for fonts
class GenerateFont:
    def __init__(self, font_color:tuple, font_style:str, size:int):
        self.font_color = font_color
        self.font_style = font_style
        self.size = size

        self.font = pygame.font.SysFont(self.font_style, self.size, bold=True)
    
    def render(self, text:str):
        font_render = self.font.render(text, True, self.font_color)
        return font_render

#GUI generator
class GenerateUI:
    def __init__(self, gui_manager):
        self.gui_manager = gui_manager
    
    def searchbar(self, position:tuple, dimension:tuple, id:str, class_name=None):
        search_bar = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect(position,dimension),
            manager=self.gui_manager,
            object_id=ObjectID(class_id=class_name,object_id=id)
        
        )
        return search_bar
    
    def button(self, position:tuple, dimension:tuple, text:str, id:str, class_name=None, container=None, anchor = None, allow_double_clicks=None, tool_tip = None):
        if tool_tip:
            tool_tip = f'<b><font color=#FF5733 size=4>Info</font></b><br><i>{tool_tip}</i>'
        else:
            pass

        if allow_double_clicks == None:
            allow_double_clicks = False

        button = UIButton(
            relative_rect=pygame.Rect(position, dimension),
            text=text, 
            manager=self.gui_manager,
            object_id=ObjectID(class_id=class_name,object_id=id),
            tool_tip_text=tool_tip,
            container = container,
            anchors = anchor,
            allow_double_clicks = allow_double_clicks
        )
        return button
    
    def scrollcontainer(self, position:tuple, dimension:tuple, id:str):
        scroll_container = pygame_gui.elements.UIScrollingContainer(
            relative_rect=pygame.Rect(position, dimension),
            manager=self.gui_manager,
            object_id = id,
            allow_scroll_y=True,  # Enable vertical scrolling
            allow_scroll_x=False, # Disable horizontal scrolling
            should_grow_automatically=True
        )
        return scroll_container
    
    def panel(self, position:tuple, dimension:tuple, id=None, container = None):
        panel = pygame_gui.elements.UIPanel(
            relative_rect=pygame.Rect(position, dimension),  
            starting_height=1,
            manager=self.gui_manager,
            element_id = id,
            container=container
        )
        return panel
    
    def image(self, position:tuple, dimension:tuple, image_surface,id:str ,container = None ):
        image = pygame_gui.elements.ui_image.UIImage(
            relative_rect=pygame.Rect(position, dimension),  
            image_surface = image_surface,
            manager = self.gui_manager,
            container =  container,
            object_id = id
        )
        return image
    
    def label(self, position:tuple, dimension:tuple,text:str, id:str, container=None, class_name = None):
        label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect(position, dimension),
            manager = self.gui_manager,
            container =  container,
            object_id = ObjectID(class_id=class_name,object_id=id),
            text=text
        )
        return label
    
    def filedialog(self, position:tuple, dimension:tuple,text:str, id:str, initial_path:str):
        file_dialog = pygame_gui.windows.ui_file_dialog.UIFileDialog(
            rect=pygame.Rect(position, dimension),
            manager=self.gui_manager,
            window_title=text,
            allowed_suffixes={'.txt', '.png', '.jpg'},
            initial_file_path=initial_path, 
            object_id=id,
            allow_picking_directories=True  
        )
        return file_dialog
    
    def progressbar(self, position:tuple, dimension:tuple, id:str, container=None):
        progress_bar = pygame_gui.elements.UIProgressBar(
            relative_rect =pygame.Rect(position, dimension),
            manager=self.gui_manager,
            object_id  = id,
            container  = container 

        )
        return progress_bar
    
    def confirmation_window(self,  position:tuple, dimension:tuple, id:str, window_title :str, blocking :bool, long_desc:str):
        
        confirmation_window = pygame_gui.windows.UIConfirmationDialog(
            rect=pygame.Rect(position, dimension),
            manager=self.gui_manager,
            window_title=window_title,
            object_id=id,
            blocking=blocking,
            action_long_desc=long_desc
        )
        return confirmation_window
    
    def message_window(self, position:tuple, dimension:tuple, id:str, window_title :str, always_on_top:bool, html_message:str):

        html_message = f'<b><font color=#FF5733 size=4>Warning</font></b><br><i>{html_message}</i>'
    

        message_window = pygame_gui.windows.UIMessageWindow(
            rect=pygame.Rect(position, dimension),
            manager=self.gui_manager,
            object_id=id,
            window_title=window_title,
            always_on_top = always_on_top,
            html_message = html_message
        )
        return message_window
    



