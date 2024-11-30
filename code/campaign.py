# campaign.py
import pygame
from castle_build import build_castle
from unit_selection import select_units
from battle import start_battle

def campaign_mode(WINDOW):
    WIDTH, HEIGHT = WINDOW.get_size()

    # Define colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GRAY = (200, 200, 200)
    DARK_GRAY = (160, 160, 160)

    # Define fonts
    MENU_FONT = pygame.font.SysFont("arial", 48)
    BUTTON_FONT = pygame.font.SysFont("arial", 24)

    running = True
    while running:
        WINDOW.fill(WHITE)

        # Draw campaign title
        title_surface = MENU_FONT.render("Campaign Mode", True, BLACK)
        title_rect = title_surface.get_rect(center=(WIDTH // 2, HEIGHT // 8))
        WINDOW.blit(title_surface, title_rect)

        # Choose your role
        role_text = BUTTON_FONT.render("Choose your role:", True, BLACK)
        role_rect = role_text.get_rect(center=(WIDTH // 2, HEIGHT // 4))
        WINDOW.blit(role_text, role_rect)

        # Define role buttons
        role_buttons = [
            {"text": "Attacker", "rect": pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 60, 200, 50), "role": "attacker"},
            {"text": "Defender", "rect": pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2, 200, 50), "role": "defender"},
            {"text": "Back", "rect": pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 60, 200, 50), "role": "back"},
        ]

        mx, my = pygame.mouse.get_pos()
        click = False

        for button in role_buttons:
            if button["rect"].collidepoint((mx, my)):
                pygame.draw.rect(WINDOW, DARK_GRAY, button["rect"])
            else:
                pygame.draw.rect(WINDOW, GRAY, button["rect"])

            button_text = BUTTON_FONT.render(button["text"], True, BLACK)
            button_rect = button_text.get_rect(center=button["rect"].center)
            WINDOW.blit(button_text, button_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
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
    GRAY = (200, 200, 200)
    DARK_GRAY = (160, 160, 160)
    BUTTON_FONT = pygame.font.SysFont("arial", 24)

    running = True
    while running:
        WINDOW.fill(WHITE)

        # Draw selection title
        title_surface = BUTTON_FONT.render(f"Select Battle ({'Attacker' if role == 'attacker' else 'Defender'})", True, BLACK)
        title_rect = title_surface.get_rect(center=(WIDTH // 2, HEIGHT // 8))
        WINDOW.blit(title_surface, title_rect)

        # Define battle buttons
        buttons = []
        for i in range(1, 11):
            x = ((i - 1) % 5) * 150 + WIDTH // 2 - 300
            y = ((i - 1) // 5) * 70 + HEIGHT // 4
            locked = i > 1  # For now, only the first battle is unlocked
            button_text = f"Battle {i}{' (Locked)' if locked else ''}"
            buttons.append({
                "text": button_text,
                "rect": pygame.Rect(x, y, 140, 50),
                "battle_num": i,
                "locked": locked
            })

        # Add back button
        back_button = {"text": "Back", "rect": pygame.Rect(WIDTH // 2 - 70, HEIGHT - 80, 140, 50), "action": "back"}

        mx, my = pygame.mouse.get_pos()
        click = False

        for button in buttons:
            if button["rect"].collidepoint((mx, my)):
                pygame.draw.rect(WINDOW, DARK_GRAY, button["rect"])
            else:
                pygame.draw.rect(WINDOW, GRAY, button["rect"])

            button_text = BUTTON_FONT.render(button["text"], True, BLACK)
            button_rect = button_text.get_rect(center=button["rect"].center)
            WINDOW.blit(button_text, button_rect)

        # Draw back button
        if back_button["rect"].collidepoint((mx, my)):
            pygame.draw.rect(WINDOW, DARK_GRAY, back_button["rect"])
        else:
            pygame.draw.rect(WINDOW, GRAY, back_button["rect"])

        back_text = BUTTON_FONT.render(back_button["text"], True, BLACK)
        back_rect = back_text.get_rect(center=back_button["rect"].center)
        WINDOW.blit(back_text, back_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if click:
            for button in buttons:
                if button["rect"].collidepoint((mx, my)):
                    if not button["locked"]:
                        # Proceed to battle setup
                        # Placeholder: Start the battle process
                        start_battle_process(WINDOW)
                    else:
                        # Show message that battle is locked
                        pass  # Implement a message popup if desired

            if back_button["rect"].collidepoint((mx, my)):
                running = False
                return

        pygame.display.update()

def start_battle_process(WINDOW):
    # Placeholder function to start the battle process
    # You can implement the battle setup phases here
    pass
