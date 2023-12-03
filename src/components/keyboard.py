from .alphabet import alphabet

import pygame

class Keyboard:
    def forward(self, letter: str) -> int:
        return alphabet.index(letter.upper())

    def backward(self, signal: int) -> str:
        return alphabet[signal]

    def draw(self, screen, x, y, w, h, font) -> None:
        r = pygame.Rect(x,y,w,h)
        pygame.draw.rect(screen, "#333333", r, width=2, border_radius=15)
        
        for index in range(26):
            letter = alphabet[index]
            letter = font.render(letter, True, "#333333")
            text_box = letter.get_rect(center = (x+w/2, y+(index+1)*h/27))
            screen.blit(letter, text_box)