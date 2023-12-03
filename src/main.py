from components import Enigma, Keyboard, Plugboard, Reflector, Rotor, alphabet, Interface

def main() -> None:
    keyboard = Keyboard()
    plugboard = Plugboard(["OB", "CD", "EF"])
    I = Rotor(alphabet.wiring_enigma_rotor_I, alphabet.notch_enigma_rotor_I)
    II = Rotor(alphabet.wiring_enigma_rotor_II, alphabet.notch_enigma_rotor_II, True)
    III = Rotor(alphabet.wiring_enigma_rotor_III, alphabet.notch_enigma_rotor_III)
    #IV = Rotor(alphabet.wiring_enigma_rotor_IV, alphabet.notch_enigma_rotor_IV)
    #V = Rotor(alphabet.wiring_enigma_rotor_V, alphabet.notch_enigma_rotor_V)
    #A = Reflector(alphabet.wiring_enigma_reflector_A)
    B = Reflector(alphabet.wiring_enigma_reflector_B)
    enigma = Enigma(keyboard, plugboard, B, [I, II, III])
    enigma.set_key("LUZ")
    enigma.set_rings([1, 1, 1])

    interface = Interface(enigma)
    interface.run()
if __name__ == "__main__":
    main()
