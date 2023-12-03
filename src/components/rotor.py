from .alphabet import alphabet

import pygame

class Rotor:
    left: str
    right: str
    notch: str
    rotate_in_notch: bool

    def __init__(self, wiring: str, notch: str, rotate_in_notch: bool = False) -> None:
        self.left = alphabet
        self.right = wiring
        self.notch = notch
        self.rotate_in_notch = rotate_in_notch

    def forward(self, signal: int) -> int:
        letter = self.right[signal]
        return self.left.index(letter)

    def backward(self, signal: int) -> int:
        letter = self.left[signal]
        return self.right.index(letter)

    def rotate(self, steps: int = 1, forward=True) -> None:
        for _ in range(steps):
            if forward:
                self.left = self.left[1:] + self.left[0]
                self.right = self.right[1:] + self.right[0]
            else:
                self.left = self.left[-1] + self.left[:-1]
                self.right = self.right[-1] + self.right[:-1]

    def rotate_to_letter(self, letter: str) -> None:
        steps = self.left.index(letter)
        self.rotate(steps)

    def set_ring(self, ring: int) -> None:
        self.rotate(ring - 1, False)

        notch_index = alphabet.index(self.notch)
        self.notch = alphabet[(notch_index - ring + 1) % len(alphabet)]

    def is_in_notch(self) -> bool:
        return self.left[0] == self.notch

    def __str__(self) -> str:
        return f"{self.left}\n{self.right}"

    def draw(self, screen, x:int, y:int, w:int, h:int, font:pygame.font) -> None:
        r = pygame.Rect(x,y,w,h)
        pygame.draw.rect(screen, "#333333", r, width=2, border_radius=15)

        for index in range(26):
            letter = self.left[index]
            letter = font.render(letter, True, "#333333")
            text_box = letter.get_rect(center = (x+w/4, y+(index+1)*h/27))

            if index == 0:
                pygame.draw.rect(screen, "teal", text_box, border_radius=1)

            if self.left[index] == self.notch:
                letter = font.render(self.notch, True, "#333333")
                pygame.draw.rect(screen, "#333333", text_box, border_radius=1)

            screen.blit(letter, text_box)

            letter = self.right[index]
            letter = font.render(letter, True, "#333333")
            text_box = letter.get_rect(center = (x+3*w/4, y+(index+1)*h/27))
            screen.blit(letter, text_box)