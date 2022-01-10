from __future__ import annotations

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
    # Special
    # Caps/Esc swap
    110: 30,
    30: 110,
}

switcheroo = ";".join(f"{src}/{dest}" for dest, src in KEYMAP.items())
print('\N{DCS}"z' + switcheroo + "\N{ST}")
