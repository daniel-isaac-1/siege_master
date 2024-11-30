# main.py
import sys
import os
import pygame
from top_menu import show_top_menu

def main():
    # Initialize Pygame
    pygame.init()

    # Set up the display
    WIDTH, HEIGHT = 800, 600
    WINDOW = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
    pygame.display.set_caption("Siege Master")

    # Define colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    BUTTON_NORMAL = (100, 100, 100)  # Original grey
    BUTTON_HOVER = (70, 70, 70)      # Darker grey on hover

    # Define fonts
    TITLE_FONT = pygame.font.SysFont("arial", 72)
    BUTTON_FONT = pygame.font.SysFont("arial", 36)

    # Load background image
    # Calculate the path to the image relative to this file
    script_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(script_dir, '..', 'images', 'title_screen.jpg')
    background_image = pygame.image.load(image_path)
    background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

    # Main loop
    running = True
    while running:
        # Draw background image
        WINDOW.blit(background_image, (0, 0))

        # Event handling
        mx, my = pygame.mouse.get_pos()
        click = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.VIDEORESIZE:
                WINDOW = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                WIDTH, HEIGHT = WINDOW.get_size()
                # If you have a background image, rescale it
                background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        # Draw semi-transparent overlay behind title
        title_bg = pygame.Surface((WIDTH, 100), pygame.SRCALPHA)
        title_bg.fill((0, 0, 0, 150))  # Black with alpha 150/255
        WINDOW.blit(title_bg, (0, HEIGHT // 4 - 50))

        # Draw title
        title_surface = TITLE_FONT.render("Siege Master", True, WHITE)
        title_rect = title_surface.get_rect(center=(WIDTH // 2, HEIGHT // 4))
        WINDOW.blit(title_surface, title_rect)

        # Define buttons
        start_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 50, 200, 50)
        exit_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 20, 200, 50)

        # ===== Removed the semi-transparent overlay behind buttons =====
        # # Draw semi-transparent overlay behind buttons
        # buttons_bg = pygame.Surface((200, 130), pygame.SRCALPHA)
        # buttons_bg.fill((0, 0, 0, 150))
        # WINDOW.blit(buttons_bg, (WIDTH // 2 - 100, HEIGHT // 2 - 60))
        # ================================================================

        # Draw buttons
        # Start button
        if start_button.collidepoint((mx, my)):
            pygame.draw.rect(WINDOW, BUTTON_HOVER, start_button)
            if click:
                show_top_menu(WINDOW)
        else:
            pygame.draw.rect(WINDOW, BUTTON_NORMAL, start_button)

        start_text = BUTTON_FONT.render("Start", True, WHITE)
        start_rect = start_text.get_rect(center=start_button.center)
        WINDOW.blit(start_text, start_rect)

        # Exit button
        if exit_button.collidepoint((mx, my)):
            pygame.draw.rect(WINDOW, BUTTON_HOVER, exit_button)
            if click:
                running = False
                pygame.quit()
                sys.exit()
        else:
            pygame.draw.rect(WINDOW, BUTTON_NORMAL, exit_button)

        exit_text = BUTTON_FONT.render("Exit", True, WHITE)
        exit_rect = exit_text.get_rect(center=exit_button.center)
        WINDOW.blit(exit_text, exit_rect)

        pygame.display.update()

if __name__ == "__main__":
    main()
