# custom.py
import pygame

def custom_game_mode(WINDOW):
    WIDTH, HEIGHT = WINDOW.get_size()

    # Define colors and fonts
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GRAY = (200, 200, 200)
    DARK_GRAY = (160, 160, 160)
    MENU_FONT = pygame.font.SysFont("arial", 48)
    BUTTON_FONT = pygame.font.SysFont("arial", 24)

    running = True
    while running:
        WINDOW.fill(WHITE)

        # Draw custom game title
        title_surface = MENU_FONT.render("Custom Game Mode", True, BLACK)
        title_rect = title_surface.get_rect(center=(WIDTH // 2, HEIGHT // 8))
        WINDOW.blit(title_surface, title_rect)

        # Placeholder text
        placeholder_text = BUTTON_FONT.render("Custom game setup coming soon.", True, BLACK)
        placeholder_rect = placeholder_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        WINDOW.blit(placeholder_text, placeholder_rect)

        # Back button
        back_button = {"text": "Back", "rect": pygame.Rect(WIDTH // 2 - 70, HEIGHT - 80, 140, 50)}

        mx, my = pygame.mouse.get_pos()
        click = False

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
            if back_button["rect"].collidepoint((mx, my)):
                running = False
                return

        pygame.display.update()
