from __future__ import annotations

import sys
import tty

tty.setcbreak(sys.stdin.fileno())

# Nuke the display
print("\N{CSI}2J")  # ED - 5-180
print("\N{CSI}95;1;1;57;131$x") # DECFRA 5-55

# Invert the top half
print("\N{CSI}1;1;10;10;7$r")  # DECCARA

# Move the cursor up there somewhere idk
print("BEFORE MOVE")
print("\N{CSI}5;50H")  # CUP
print("AFTER MOVE")
# print()
# print("\N{CSI}7mwat??\N{CSI}0m")

input()

print("\N{CSI}1;1;10;10;7$r")  # DECCARA

input()

