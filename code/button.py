# button.py
import pygame

class Button:
    def __init__(self, text, rect, font, bg_color, hover_color, text_color):
        self.text = text
        self.rect = pygame.Rect(rect)
        self.font = font
        self.bg_color = bg_color
        self.hover_color = hover_color
        self.text_color = text_color

    def draw(self, window, mouse_pos, mouse_click):
        if self.rect.collidepoint(mouse_pos):
            pygame.draw.rect(window, self.hover_color, self.rect)
            if mouse_click:
                return True
        else:
            pygame.draw.rect(window, self.bg_color, self.rect)

        text_surf = self.font.render(self.text, True, self.text_color)
        text_rect = text_surf.get_rect(center=self.rect.center)
        window.blit(text_surf, text_rect)
        return False

