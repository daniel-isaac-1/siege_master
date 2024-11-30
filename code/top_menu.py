# top_menu.py
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
    GRAY = (200, 200, 200)
    DARK_GRAY = (160, 160, 160)

    # Define fonts
    MENU_FONT = pygame.font.SysFont("arial", 48)
    BUTTON_FONT = pygame.font.SysFont("arial", 36)

    running = True
    while running:
        WINDOW.fill(WHITE)

        # Draw menu title
        title_surface = MENU_FONT.render("Main Menu", True, BLACK)
        title_rect = title_surface.get_rect(center=(WIDTH // 2, HEIGHT // 4))
        WINDOW.blit(title_surface, title_rect)

        # Define buttons with updated text
        buttons = [
            {"text": "Campaign", "rect": pygame.Rect(WIDTH // 2 - 150, HEIGHT // 2 - 90, 300, 50), "action": "campaign"},
            {"text": "Custom", "rect": pygame.Rect(WIDTH // 2 - 150, HEIGHT // 2 - 30, 300, 50), "action": "custom"},
            {"text": "Shop", "rect": pygame.Rect(WIDTH // 2 - 150, HEIGHT // 2 + 30, 300, 50), "action": "shop"},
            {"text": "Back", "rect": pygame.Rect(WIDTH // 2 - 150, HEIGHT // 2 + 90, 300, 50), "action": "back"},
        ]

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
                    if button["action"] == "campaign":
                        campaign_mode(WINDOW)
                    elif button["action"] == "custom":
                        custom_game_mode(WINDOW)
                    elif button["action"] == "shop":
                        open_shop(WINDOW)
                    elif button["action"] == "back":
                        running = False
                        return

        pygame.display.update()
