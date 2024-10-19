# SPDX-FileCopyrightText: 2024, Rylie Pavlik <rylie@ryliepavlik.com>
#
# SPDX-License-Identifier: MIT
"""
Cycles through the colors of the trans pride flag on all pixels.

Intended for use as code.py
"""

from maskleds import MaskLeds
import time
from adafruit_led_animation.animation.colorcycle import ColorCycle
from colors import TRANS_FLAG
from pixels import PIXELS_STRIP, CENTER_PIXEL

pixels = MaskLeds(PIXELS_STRIP, CENTER_PIXEL)

# anim = ColorCycle(pixels, 0.5, colors=TRANS_FLAG)

while True:
    # anim.animate()
    for i, color in enumerate(TRANS_FLAG):
        pixels[i] = color
    pixels.show()
    time.sleep(5)
