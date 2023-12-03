from typing import List

from .alphabet import alphabet
from .keyboard import Keyboard
from .plugboard import Plugboard
from .reflector import Reflector
from .rotor import Rotor

class Enigma:
    keyboard: Keyboard
    plugboard: Plugboard
    reflector: Reflector
    rotors: List[Rotor]

    def __init__(
        self,
        keyboard: Keyboard,
        plugboard: Plugboard,
        reflector: Reflector,
        rotors: List[Rotor],
    ) -> None:
        self.keyboard = keyboard
        self.plugboard = plugboard
        self.reflector = reflector
        self.rotors = rotors

    def _rotate_rotors(self) -> None:
        if self.rotors[1].left[0] == self.rotors[1].notch and self.rotors[2].left[0] == self.rotors[2].notch:
            self.rotors[0].rotate()
            self.rotors[1].rotate()
            self.rotors[2].rotate()
        elif self.rotors[1].left[0] == self.rotors[1].notch:
            self.rotors[0].rotate()
            self.rotors[1].rotate()
            self.rotors[2].rotate()
        elif self.rotors[2].left[0] == self.rotors[2].notch:
            self.rotors[1].rotate()
            self.rotors[2].rotate()
        else:
            self.rotors[2].rotate()

    def set_rings(self, rings: List[int]) -> None:
        for index in range(len(self.rotors)):
            self.rotors[index].set_ring(rings[index])

    def set_key(self, key: str) -> None:
        for index in range(len(self.rotors)):
            self.rotors[index].rotate_to_letter(key[index].upper())

    def encipher(self, message: str) -> str:
        encrypted_message = ""
        for letter in message.upper():
            encrypted_message += self.encipher_letter(letter)
        return encrypted_message

    def encipher_letter(self, letter: str) -> str:
        if letter not in alphabet:
            return letter

        self._rotate_rotors()

        signal = self.keyboard.forward(letter)
        signal = self.plugboard.forward(signal)

        for rotor in self.rotors[::-1]:
            signal = rotor.forward(signal)

        signal = self.reflector.reflect(signal)

        for rotor in self.rotors:
            signal = rotor.backward(signal)

        signal = self.plugboard.backward(signal)
        return self.keyboard.backward(signal)