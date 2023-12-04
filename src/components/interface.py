from components import alphabet, Enigma

import pygame

class Interface:
    def __init__(self, enigma:Enigma) -> None:
        pygame.init()
        pygame.font.init()
        pygame.display.set_caption("Enigma Machine Simulator")

        self.width = 1600
        self.height = 900
        self.screen = pygame.display.set_mode((self.width, self.height))
        

        self.running = True
        self.enigma = enigma

        #define fonts
        self.BOLD = pygame.font.SysFont("Roboto", 25, bold=True)
        self.MONO = pygame.font.SysFont("Roboto", 25)

        # define margins and gap
        self.margins = {"left": 200, "right": 200, "top": 200, "bottom": 200}
        self.gap = 50
    
    def run(self):
        INPUT = ""
        OUTPUT = ""
        while self.running:
            #background
            self.screen.fill("#f5f5f5")

            #text input
            text = self.BOLD.render(INPUT, True, "#333333")
            text_box = text.get_rect(center = (self.width/2, self.margins["top"]/2))
            self.screen.blit(text, text_box)

            text = self.MONO.render(OUTPUT, True, "#333333")
            text_box = text.get_rect(center = (self.width/2, self.margins["top"]/2+20))
            self.screen.blit(text, text_box)

            #draw enigma machine
            self.draw()
            #update screen
            pygame.display.flip()

            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            INPUT = INPUT + " "
                            OUTPUT = OUTPUT + " "
                        else:
                            key = event.unicode
                            if key.lower() in alphabet.alphabet.lower():
                                letter = key.upper()
                                INPUT = INPUT + letter
                                cipher = self.enigma.encipher(letter)
                                OUTPUT = OUTPUT + cipher
        pygame.quit()


    def draw(self):
        x = self.margins["left"]
        y = self.margins["top"]
        w = (self.width - self.margins["left"] - self.margins["right"] - 5*self.gap)/6
        h = self.height - self.margins["top"] - self.margins["bottom"]

        for components in [self.enigma.reflector,self.enigma.rotors[0], self.enigma.rotors[1],self.enigma.rotors[2], self.enigma.plugboard, self.enigma.keyboard]:
            components.draw(self.screen, x, y, w, h, self.BOLD)
            x += w + self.gap

        names = ["Refletor", "Rotor Esquerda", "Rotor Meio", "Rotor Direita", "Placa de Plug", "Teclado"]
        y = self.margins["top"]*3/4
        for i in range(6):
            x = self.margins["left"] + w/2+ i*(w + self.gap)
            title = self.MONO.render(names[i], True, "#333333")
            text_box = title.get_rect(center = (x,y))
            self.screen.blit(title, text_box)
