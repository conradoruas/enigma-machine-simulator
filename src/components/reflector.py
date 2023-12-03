from .alphabet import alphabet

import pygame

class Reflector:
    left: str
    right: str

    def __init__(self, wiring: str) -> None:
        self.left = alphabet
        self.right = wiring

    def reflect(self, signal: int) -> int:
        letter = self.right[signal]
        return self.left.index(letter)
    
    def draw(self, screen, x:int, y:int, w:int, h:int, font:pygame.font) -> None:
        r = pygame.Rect(x,y,w,h)
        pygame.draw.rect(screen, "#333333", r, width=2, border_radius=15)

        for index in range(26):
            letter = self.left[index]
            letter = font.render(letter, True, "#333333")
            text_box = letter.get_rect(center = (x+w/4, y+(index+1)*h/27))
            screen.blit(letter, text_box)

            letter = self.right[index]
            letter = font.render(letter, True, "#333333")
            text_box = letter.get_rect(center = (x+3*w/4, y+(index+1)*h/27))
            screen.blit(letter, text_box)
