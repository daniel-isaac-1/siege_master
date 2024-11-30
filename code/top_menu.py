# top_menu.py
import os
import sys
import pygame
from campaign import campaign_mode
from custom import custom_game_mode
from shop import open_shop

def show_top_menu(WINDOW):
    # Define dimensions
    WIDTH, HEIGHT = WINDOW.get_size()

    # Define colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    BUTTON_NORMAL = (100, 100, 100)  # Original grey
    BUTTON_HOVER = (70, 70, 70)      # Darker grey on hover
    TEXT_BAR_COLOR = (0, 0, 0, 150)  # Semi-transparent grey

    # Define fonts
    MENU_FONT = pygame.font.SysFont("arial", 48)
    BUTTON_FONT = pygame.font.SysFont("arial", 36)

    # Load background image
    script_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(script_dir, '..', 'images', 'main_menu.jpg')

    if not os.path.exists(image_path):
        print(f"Background image not found at {image_path}")
        pygame.quit()
        sys.exit()

    try:
        background_image = pygame.image.load(image_path)
        background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
    except pygame.error as e:
        print(f"Unable to load background image: {e}")
        pygame.quit()
        sys.exit()

    running = True

    # Define the handle_button_action function inside show_top_menu
    def handle_button_action(action):
        nonlocal running  # To modify the running variable from the outer scope
        if action == "campaign":
            campaign_mode(WINDOW)
        elif action == "custom":
            custom_game_mode(WINDOW)
        elif action == "shop":
            open_shop(WINDOW)
        elif action == "back":
            running = False
            return

    while running:
        # Draw background image
        WINDOW.blit(background_image, (0, 0))

        # Event handling
        mx, my = pygame.mouse.get_pos()
        click = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Exit the entire program if the window is closed
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        # Draw semi-transparent grey bar behind the "Main Menu" text
        text_bar_width = WIDTH  # Extend across the entire width
        text_bar_height = 80
        text_bar_x = 0  # Start from the left edge
        text_bar_y = HEIGHT // 4 - (text_bar_height // 2)  # Center vertically around the text

        text_bar = pygame.Surface((text_bar_width, text_bar_height), pygame.SRCALPHA)
        text_bar.fill(TEXT_BAR_COLOR)
        WINDOW.blit(text_bar, (text_bar_x, text_bar_y))

        # Draw menu title
        title_surface = MENU_FONT.render("Main Menu", True, WHITE)
        title_rect = title_surface.get_rect(center=(WIDTH // 2, HEIGHT // 4))
        WINDOW.blit(title_surface, title_rect)

        # Define buttons with updated text
        buttons = [
            {"text": "Campaign", "rect": pygame.Rect(WIDTH // 2 - 150, HEIGHT // 2 - 90, 300, 50), "action": "campaign"},
            {"text": "Custom", "rect": pygame.Rect(WIDTH // 2 - 150, HEIGHT // 2 - 30, 300, 50), "action": "custom"},
            {"text": "Shop", "rect": pygame.Rect(WIDTH // 2 - 150, HEIGHT // 2 + 30, 300, 50), "action": "shop"},
            {"text": "Back", "rect": pygame.Rect(WIDTH // 2 - 150, HEIGHT // 2 + 90, 300, 50), "action": "back"},
        ]

        for button in buttons:
            # Change button color on hover
            if button["rect"].collidepoint((mx, my)):
                pygame.draw.rect(WINDOW, BUTTON_HOVER, button["rect"])
                if click:
                    handle_button_action(button["action"])
            else:
                pygame.draw.rect(WINDOW, BUTTON_NORMAL, button["rect"])

            # Render button text
            button_text = BUTTON_FONT.render(button["text"], True, WHITE)
            button_rect = button_text.get_rect(center=button["rect"].center)
            WINDOW.blit(button_text, button_rect)

        pygame.display.update()
