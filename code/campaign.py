# campaign.py
import os
import sys
import pygame

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
        click = False  # Reset click at the start of each frame

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.VIDEORESIZE:
                WINDOW = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                WIDTH, HEIGHT = WINDOW.get_size()
                # Rescale background image
                background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        # Get mouse position
        mx, my = pygame.mouse.get_pos()

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

        # Draw "Choose Your Role" text
        role_text = BUTTON_FONT.render("Choose Your Role:", True, WHITE)
        role_rect = role_text.get_rect(center=(WIDTH // 2, HEIGHT // 4))

        # Create a semi-transparent grey bar behind the text
        padding = 20
        role_bar_width = role_rect.width + padding * 2
        role_bar_height = role_rect.height + padding
        role_bar = pygame.Surface((role_bar_width, role_bar_height), pygame.SRCALPHA)
        role_bar.fill(TEXT_BAR_COLOR)
        role_bar_rect = role_bar.get_rect(center=role_rect.center)

        # Blit the bar and then the text
        WINDOW.blit(role_bar, role_bar_rect)
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

        # After drawing, handle clicks
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

    # Define colors and fonts
    WHITE = (255, 255, 255)
    BUTTON_NORMAL = (100, 100, 100)
    BUTTON_HOVER = (70, 70, 70)
    TEXT_BAR_COLOR = (128, 128, 128, 180)

    BUTTON_FONT = pygame.font.SysFont("arial", 32)
    MENU_FONT = pygame.font.SysFont("arial", 48)

    # Load background image based on role
    script_dir = os.path.dirname(os.path.abspath(__file__))
    if role == 'attacker':
        image_name = 'attacker.jpg'
    elif role == 'defender':
        image_name = 'defender.jpg'
    else:
        image_name = 'campaign.jpg'  # Fallback in case of unexpected role

    image_path = os.path.join(script_dir, '..', 'images', image_name)

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
        click = False  # Reset click at the start of each frame

        # Handle events
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

        # After drawing, handle clicks
        if click:
            if back_button["rect"].collidepoint((mx, my)):
                running = False
                return
            # Battle buttons do nothing when clicked

        pygame.display.update()
