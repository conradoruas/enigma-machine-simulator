from typing import List

from .alphabet import alphabet
import pygame

class Plugboard:
    left: str = alphabet
    right: str = alphabet

    def __init__(self, pairs: List[str]) -> None:
        self._configure_pairs(pairs)

    def _configure_pairs(self, pairs: List[str]) -> None:
        for pair in pairs:
            A = pair[0]
            B = pair[1]
            index_A = self.left.find(A)
            index_B = self.left.find(B)
            self.left = self.left[:index_A] + B + self.left[index_A + 1 :]
            self.left = self.left[:index_B] + A + self.left[index_B + 1 :]

    def forward(self, signal: int) -> int:
        letter = self.right[signal]
        return self.left.find(letter)

    def backward(self, signal: int) -> int:
        letter = self.left[signal]
        return self.right.find(letter)

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