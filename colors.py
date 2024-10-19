# SPDX-FileCopyrightText: 2024, Rylie Pavlik <rylie@ryliepavlik.com>
#
# SPDX-License-Identifier: MIT
"""
Color constants.

Utility, do not use as code.py
"""

import adafruit_fancyled.adafruit_fancyled as fancy

# Experimentally determined on target pixels https://www.adafruit.com/product/4776
LEVELS = (0.35, 0.25, 0.25)

TRANS_BLUE_RAW = fancy.CRGB(91, 206, 250)  # 0x5bcefa
TRANS_BLUE = fancy.gamma_adjust(TRANS_BLUE_RAW, brightness=LEVELS).pack()
TRANS_PINK_RAW = fancy.CRGB(245, 169, 184)  # 0xf5a9b8
TRANS_PINK = fancy.gamma_adjust(TRANS_PINK_RAW, brightness=LEVELS).pack()
TRANS_WHITE_RAW = fancy.CRGB(255, 255, 255)
TRANS_WHITE = fancy.gamma_adjust(TRANS_WHITE_RAW, brightness=LEVELS).pack()

TRANS_FLAG = (
    TRANS_BLUE,
    TRANS_PINK,
    TRANS_WHITE,
    TRANS_PINK,
    TRANS_BLUE,
)


RED_RAW = (255, 0, 0)
RED = fancy.gamma_adjust(RED_RAW, brightness=LEVELS).pack()
