# shop.py
import os
import sys
import pygame

def open_shop(WINDOW):
    # Define dimensions
    WIDTH, HEIGHT = WINDOW.get_size()

    # Define colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    BUTTON_NORMAL = (100, 100, 100)  # Original grey
    BUTTON_HOVER = (70, 70, 70)      # Darker grey on hover
    TEXT_BAR_COLOR = (128, 128, 128, 180)  # Semi-transparent grey
    OVERLAY_COLOR = (0, 0, 0, 150)  # Semi-transparent black for message background

    # Define fonts
    MENU_FONT = pygame.font.SysFont("arial", 48)
    BUTTON_FONT = pygame.font.SysFont("arial", 36)
    MESSAGE_FONT = pygame.font.SysFont("arial", 36)

    # Load background image
    script_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(script_dir, '..', 'images', 'shop.jpg')

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

        # Draw semi-transparent grey bar behind the "Shop" text
        text_bar_width = WIDTH  # Extend across the entire width
        text_bar_height = 80
        text_bar_x = 0  # Start from the left edge
        text_bar_y = HEIGHT // 4 - (text_bar_height // 2)  # Center vertically around the text

        text_bar = pygame.Surface((text_bar_width, text_bar_height), pygame.SRCALPHA)
        text_bar.fill(TEXT_BAR_COLOR)
        WINDOW.blit(text_bar, (text_bar_x, text_bar_y))

        # Draw shop title
        title_surface = MENU_FONT.render("Shop", True, WHITE)
        title_rect = title_surface.get_rect(center=(WIDTH // 2, HEIGHT // 4))
        WINDOW.blit(title_surface, title_rect)

        # Define buttons
        buttons = [
            {"text": "Buy Dragon Units", "rect": pygame.Rect(WIDTH // 2 - 150, HEIGHT // 2 - 90, 300, 50), "action": "buy_dragons"},
            {"text": "Buy Wizard Units", "rect": pygame.Rect(WIDTH // 2 - 150, HEIGHT // 2 - 30, 300, 50), "action": "buy_wizards"},
            {"text": "Back", "rect": pygame.Rect(WIDTH // 2 - 150, HEIGHT // 2 + 30, 300, 50), "action": "back"},
        ]

        for button in buttons:
            # Change button color on hover
            if button["rect"].collidepoint((mx, my)):
                pygame.draw.rect(WINDOW, BUTTON_HOVER, button["rect"])
                if click:
                    action = button["action"]
                    if action in ["buy_dragons", "buy_wizards"]:
                        # Display temporary text message
                        display_shop_coming_soon(WINDOW)
                    elif action == "back":
                        running = False
                        return
            else:
                pygame.draw.rect(WINDOW, BUTTON_NORMAL, button["rect"])

            # Render button text
            button_text = BUTTON_FONT.render(button["text"], True, WHITE)
            button_rect = button_text.get_rect(center=button["rect"].center)
            WINDOW.blit(button_text, button_rect)

        pygame.display.update()

def display_shop_coming_soon(WINDOW):
    # Get window dimensions
    WIDTH, HEIGHT = WINDOW.get_size()

    # Create semi-transparent overlay
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 150))  # Semi-transparent black

    # Render the message text
    MESSAGE_FONT = pygame.font.SysFont("arial", 48)
    message_text = "Shop Functionality Coming Soon!"
    text_surface = MESSAGE_FONT.render(message_text, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))

    # Create a surface for the text background
    bg_width = text_rect.width + 40
    bg_height = text_rect.height + 20
    bg_surface = pygame.Surface((bg_width, bg_height), pygame.SRCALPHA)
    bg_surface.fill((0, 0, 0, 200))  # More opaque background for the text

    # Get the position to blit the background surface
    bg_rect = bg_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))

    # Display the message for 3 seconds
    start_time = pygame.time.get_ticks()
    display_duration = 3000  # milliseconds
    displaying = True

    while displaying:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Blit the overlay
        WINDOW.blit(overlay, (0, 0))

        # Blit the background surface
        WINDOW.blit(bg_surface, bg_rect.topleft)

        # Blit the text onto the window
        WINDOW.blit(text_surface, text_rect)

        pygame.display.update()

        # Check if 3 seconds have passed
        if pygame.time.get_ticks() - start_time > display_duration:
            displaying = False
