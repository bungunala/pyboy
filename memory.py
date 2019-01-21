import logging


class Memory:
    memory = bytearray(65536)

    def __init__(self):
        for i in range(0, len(self.memory)):
            self.memory[i] = 0

    # cargar el archivo de la rom
    def load(self, data, offset):
        logging.debug("loading data into loc %X and up." % offset)
        for i in range(0, len(data)):
            self.memory[int(i + offset)] = data[i]

    # imprime bytes de la "memoria", empezando en offset
    def memprint(self, offset, _bytes, mode="hex"):
        if mode == "hex":
            for i in range(0, _bytes, 2):
                print("{0:X}:\t {1:02X}\t{2:02X}".format(i + offset, self.memory[i + offset],
                                                         self.memory[i + 1 + offset]))
        elif mode == "bin":
            for i in range(0, _bytes, 2):
                print("{0:X}:\t {1:08b}".format(i + offset, self.memory[i + offset]))

    # no se para que es
    def memprintat(self, offset, mode="hex"):
        if mode == "hex":
            print("{0:X}:\t {1:X}".format(offset, self.memory[offset]))
        elif mode == "bin":
            print("{0:X}:\t {2:08b}".format(offset, self.memory[offset]))
