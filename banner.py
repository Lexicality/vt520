from __future__ import annotations

import sys
import tty

tty.setcbreak(sys.stdin.fileno())


def write(*text) -> None:
    sys.stdout.write("".join((str(t) for t in text)))


CSI = "\N{CSI}"
DCS = "\N{DCS}"
ST = "\N{ST}"

F_OFF = "0"
F_BOLD = "1"
F_UNDER = "4"
F_BLINK = "5"
F_REVERSE = "7"

WIDTH = 132
HEIGHT = 52
WHOLE_SCREEN = f"1;1;{HEIGHT};{WIDTH}"


def deccara(x1: int, y1: int, x2: int, y2: int, fmt: str) -> None:
    write(CSI, y1, ";", x1, ";", y2, ";", x2, ";", fmt, "$r")  # DECCARA 5-28


def cup(x: int, y: int) -> None:
    write(CSI, y, ";", x, "H")  # CUP 5-8


# Nuke the display
def clear_display():
    write(CSI, "2", "J")  # ED - 5-180
    write(
        CSI,
        32,  # space
        ";",
        WHOLE_SCREEN,
        "$x",
    )  # DECFRA 5-55


clear_display()
cup(3, 10)
write("\N{ESC}#3", "Limehouse Labs")
cup(3, 11)
write("\N{ESC}#4", "Limehouse Labs")

deccara(1, 1, WIDTH, 20, F_REVERSE)


# Prevent vim's run banner showing up
cup(WIDTH, HEIGHT)
input()
