# campaign.py
import os
import sys
import pygame
from castle_build import build_castle
from unit_selection import select_units
from battle import start_battle

def campaign_mode(WINDOW):
    # Initialize Pygame if not already initialized
    if not pygame.get_init():
        pygame.init()

    WIDTH, HEIGHT = WINDOW.get_size()

    # Define colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    BUTTON_NORMAL = (100, 100, 100)  # Original grey
    BUTTON_HOVER = (70, 70, 70)      # Darker grey on hover
    TEXT_BAR_COLOR = (128, 128, 128, 180)  # Semi-transparent grey

    # Define fonts
    MENU_FONT = pygame.font.SysFont("arial", 48)
    BUTTON_FONT = pygame.font.SysFont("arial", 36)

    # Load background image
    script_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(script_dir, '..', 'images', 'campaign.jpg')

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
        # Handle window resize
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.VIDEORESIZE:
                WINDOW = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                WIDTH, HEIGHT = WINDOW.get_size()
                background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        # Get mouse position
        mx, my = pygame.mouse.get_pos()
        click = False

        # Draw background image
        WINDOW.blit(background_image, (0, 0))

        # Draw semi-transparent grey bar behind the title text
        text_bar = pygame.Surface((WIDTH, 80), pygame.SRCALPHA)
        text_bar.fill(TEXT_BAR_COLOR)
        WINDOW.blit(text_bar, (0, HEIGHT // 8 - 40))

        # Draw campaign title
        title_surface = MENU_FONT.render("Campaign Mode", True, WHITE)
        title_rect = title_surface.get_rect(center=(WIDTH // 2, HEIGHT // 8))
        WINDOW.blit(title_surface, title_rect)

        # Choose your role
        role_text = BUTTON_FONT.render("Choose Your Role:", True, WHITE)
        role_rect = role_text.get_rect(center=(WIDTH // 2, HEIGHT // 4))
        WINDOW.blit(role_text, role_rect)

        # Define role buttons
        role_buttons = [
            {"text": "Attacker", "rect": pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 80, 200, 50), "role": "attacker"},
            {"text": "Defender", "rect": pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 20, 200, 50), "role": "defender"},
            {"text": "Back", "rect": pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 40, 200, 50), "role": "back"},
        ]

        for button in role_buttons:
            if button["rect"].collidepoint((mx, my)):
                pygame.draw.rect(WINDOW, BUTTON_HOVER, button["rect"])
            else:
                pygame.draw.rect(WINDOW, BUTTON_NORMAL, button["rect"])

            button_text = BUTTON_FONT.render(button["text"], True, WHITE)
            button_rect = button_text.get_rect(center=button["rect"].center)
            WINDOW.blit(button_text, button_rect)

        # Event handling after drawing
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.VIDEORESIZE:
                WINDOW = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                WIDTH, HEIGHT = WINDOW.get_size()
                background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if click:
            for button in role_buttons:
                if button["rect"].collidepoint((mx, my)):
                    if button["role"] in ["attacker", "defender"]:
                        select_battle(WINDOW, button["role"])
                    elif button["role"] == "back":
                        running = False
                        return

        pygame.display.update()

def select_battle(WINDOW, role):
    WIDTH, HEIGHT = WINDOW.get_size()

    # Define colors and fonts (same as before)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    BUTTON_NORMAL = (100, 100, 100)
    BUTTON_HOVER = (70, 70, 70)
    TEXT_BAR_COLOR = (128, 128, 128, 180)

    BUTTON_FONT = pygame.font.SysFont("arial", 32)
    MENU_FONT = pygame.font.SysFont("arial", 48)

    # Load background image
    script_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(script_dir, '..', 'images', 'campaign.jpg')

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
        # Handle window resize
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.VIDEORESIZE:
                WINDOW = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                WIDTH, HEIGHT = WINDOW.get_size()
                background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        # Get mouse position
        mx, my = pygame.mouse.get_pos()
        click = False

        # Draw background image
        WINDOW.blit(background_image, (0, 0))

        # Draw semi-transparent grey bar behind the title text
        text_bar = pygame.Surface((WIDTH, 80), pygame.SRCALPHA)
        text_bar.fill(TEXT_BAR_COLOR)
        WINDOW.blit(text_bar, (0, HEIGHT // 8 - 40))

        # Draw selection title
        title_text = f"Select Battle ({'Attacker' if role == 'attacker' else 'Defender'})"
        title_surface = MENU_FONT.render(title_text, True, WHITE)
        title_rect = title_surface.get_rect(center=(WIDTH // 2, HEIGHT // 8))
        WINDOW.blit(title_surface, title_rect)

        # Define battle buttons
        buttons = []
        button_width = 300
        button_height = 50
        button_gap = 20
        total_height = 4 * button_height + 3 * button_gap
        start_y = (HEIGHT - total_height) // 2

        for i in range(1, 5):
            x = WIDTH // 2 - button_width // 2
            y = start_y + (i - 1) * (button_height + button_gap)
            locked = i > 1  # For now, only the first battle is unlocked
            button_text = f"Battle {i}" if not locked else f"Battle {i} (Locked)"
            buttons.append({
                "text": button_text,
                "rect": pygame.Rect(x, y, button_width, button_height),
                "battle_num": i,
                "locked": locked
            })

        # Add back button
        back_button = {"text": "Back", "rect": pygame.Rect(WIDTH // 2 - 100, HEIGHT - 80, 200, 50), "action": "back"}

        for button in buttons:
            if button["rect"].collidepoint((mx, my)):
                pygame.draw.rect(WINDOW, BUTTON_HOVER, button["rect"])
            else:
                pygame.draw.rect(WINDOW, BUTTON_NORMAL, button["rect"])

            button_text = BUTTON_FONT.render(button["text"], True, WHITE)
            button_rect = button_text.get_rect(center=button["rect"].center)
            WINDOW.blit(button_text, button_rect)

        # Draw back button
        if back_button["rect"].collidepoint((mx, my)):
            pygame.draw.rect(WINDOW, BUTTON_HOVER, back_button["rect"])
        else:
            pygame.draw.rect(WINDOW, BUTTON_NORMAL, back_button["rect"])

        back_text = BUTTON_FONT.render(back_button["text"], True, WHITE)
        back_rect = back_text.get_rect(center=back_button["rect"].center)
        WINDOW.blit(back_text, back_rect)

        # Event handling after drawing
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.VIDEORESIZE:
                WINDOW = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                WIDTH, HEIGHT = WINDOW.get_size()
                background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if click:
            for button in buttons:
                if button["rect"].collidepoint((mx, my)):
                    if not button["locked"]:
                        start_battle_process(WINDOW, role, button["battle_num"])
                    else:
                        # Display locked message
                        display_locked_message(WINDOW)
            if back_button["rect"].collidepoint((mx, my)):
                running = False
                return

        pygame.display.update()

def start_battle_process(WINDOW, role, battle_num):
    # Placeholder function to start the battle process
    # You can implement the battle setup phases here
    print(f"Starting Battle {battle_num} as {role.capitalize()}...")
    # For now, just display a message or proceed to the next step

def display_locked_message(WINDOW):
    # Display a temporary message that the battle is locked
    WIDTH, HEIGHT = WINDOW.get_size()
    MESSAGE_FONT = pygame.font.SysFont("arial", 36)
    message_text = "Battle Locked!"
    text_surface = MESSAGE_FONT.render(message_text, True, (255, 0, 0))
    text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))

    # Semi-transparent overlay
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 150))

    # Display the message for 2 seconds
    start_time = pygame.time.get_ticks()
    display_duration = 2000  # milliseconds
    displaying = True

    while displaying:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Draw the overlay and message
        WINDOW.blit(overlay, (0, 0))
        WINDOW.blit(text_surface, text_rect)
        pygame.display.update()

        if pygame.time.get_ticks() - start_time > display_duration:
            displaying = False
