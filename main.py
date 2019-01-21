import logging
import sys

from memory import Memory
from rom import Rom

mem = Memory()
romF = Rom()


def init():
    logging.basicConfig(level=logging.DEBUG)
    # inicializar memoria
    # mem = Memory()

    # abrir archivo de bios
    with open("bios.rom", mode="rb") as biosFile:
        boot = biosFile.read()  # b para binario???

    logging.debug("print boot")
    logging.debug(boot)
    # mem.load(boot, "C000")
    mem.load(boot, 49152)


init()
logging.debug("initializing...")
logging.debug("init done...")
logging.debug("Loading ROM...")
if sys.argv[1]:
    logging.debug("argument supplied %s" % sys.argv[1])
    with open(sys.argv[1], mode="rb") as f:
        romFile = f.read()
        # rom.load(f.read())
        # logging.debug(rom)
        # mem.memprint(0, len(rom), "bin")

else:
    logging.debug("No file supplied as argument...")
