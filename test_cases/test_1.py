import pygame
import pygame_gui

# Initialize pygame
pygame.init()

# Set up display
WINDOW_SIZE = (800, 600)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("UIMessageWindow Example")

# Set up pygame_gui
ui_manager = pygame_gui.UIManager(WINDOW_SIZE)

# Create a message window (position and size: x=250, y=200, width=300, height=200)
message_rect = pygame.Rect(250, 200, 300, 200)
message_text = "<b>Hello!</b> This is a <i>UIMessageWindow</i> in <u>pygame_gui</u>."

# Create the UIMessageWindow instance
message_window = pygame_gui.windows.UIMessageWindow(
    rect=message_rect,
    html_message=message_text,
    manager=ui_manager,
    window_title="Message Box"
)

# Main loop
clock = pygame.time.Clock()
running = True
while running:
    time_delta = clock.tick(60) / 1000.0  # Limit frame rate to 60 FPS

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Handle UI events
        ui_manager.process_events(event)

    # Update UI Manager
    ui_manager.update(time_delta)

    # Clear screen
    screen.fill((30, 30, 30))

    # Draw UI elements
    ui_manager.draw_ui(screen)

    # Refresh display
    pygame.display.update()

# Quit pygame
pygame.quit()
