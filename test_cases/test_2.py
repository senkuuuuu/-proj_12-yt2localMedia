import pygame
import pygame_gui
import time

pygame.init()

# Create a Pygame window
window_size = (600, 400)
screen = pygame.display.set_mode(window_size)

# Create a UI manager
manager = pygame_gui.UIManager(window_size)

# Define a text box
text_box = pygame_gui.elements.UITextBox(
    html_text="<b>Hello, world!</b> This is a <i>pygame_gui</i> text box. <br>",
    relative_rect=pygame.Rect(50, 50, 500, 200),
    manager=manager
)

# Main loop
clock = pygame.time.Clock()
running = True
while running:
    time_delta = clock.tick(60) / 1000.0


    time.sleep(1)
    text_box.append_html_text('<b>Hello, world!</b> This is a <i>pygame_gui</i> text box. <br>')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        manager.process_events(event)

    manager.update(time_delta)

    screen.fill((30, 30, 30))
    manager.draw_ui(screen)
    pygame.display.update()

pygame.quit()
