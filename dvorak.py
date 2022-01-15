from __future__ import annotations

import os
import select
import sys
import time
import tty
from typing import Dict

KEYMAP: Dict[int, int] = {
    # Number Row
    1: 13,
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 6,
    7: 7,
    8: 8,
    9: 9,
    10: 10,
    11: 11,
    12: 12,
    13: 45,
    # Top Row
    17: 41,
    18: 53,
    19: 54,
    20: 26,
    21: 22,
    22: 34,
    23: 35,
    24: 48,
    25: 20,
    26: 39,
    27: 27,
    28: 28,
    # Middle Row
    31: 31,
    32: 25,
    33: 19,
    34: 23,
    35: 24,
    36: 33,
    37: 36,
    38: 21,
    39: 51,
    40: 32,
    41: 55,
    42: 42,
    # Bottom Row
    45: 1,
    46: 40,
    47: 17,
    48: 37,
    49: 38,
    50: 47,
    51: 50,
    52: 52,
    53: 18,
    54: 49,
    55: 46,
}

# Chaos time!
STDIN = sys.stdin.fileno()
tty.setcbreak(STDIN)
polly = select.poll()
polly.register(STDIN, select.POLLIN | select.POLLERR)


def readr() -> str:
    # Blocking read on one byte because there should always be at least one
    ret = os.read(STDIN, 1)
    # Read everything else that's available
    # (I'm sure the terminal will write fast enough)
    while polly.poll(0.1):
        ret += os.read(STDIN, 20)
    return ret.decode("latin-1")


def get_keydef(key: int) -> str:
    print(f"\N{CSI}{key},w", end=" ", flush=True)  # DECRQKD 5-106
    decrpak = readr()
    # These are glorious magical print statments that make the damn thing
    #  actually work, I'm assuming it's something to do with flow control or
    #  something
    print(key, repr(decrpak))
    _, data, _ = decrpak.split("/", maxsplit=3)
    return data


# Reset the keymap (sorry if you were using it lol)
print("Resetting the keyboard")
print("\N{CSI}2+z", end="", flush=True)  # DECPKA 5-87

print("Having a little nap just in case")
time.sleep(0.1)

print("Swapping ESC and capslock")

# Swap ESC and Caps
# print('\N{DCS}"z110/30;30/110;\N{ST}')  # DECCKD 5-31

keydefs: Dict[int, str] = {}
for src in KEYMAP.values():
    keydefs[src] = get_keydef(src)

print("Got key definitons:")
print(keydefs)
print("Swapping everything!")

for dest, src in KEYMAP.items():
    print(
        '\N{DCS}"y',
        f"{dest}/{keydefs[src]}/0",
        "\N{ST}",
        sep="",
        end="",
        flush=True,
    )  # DEKPAK 5-78
