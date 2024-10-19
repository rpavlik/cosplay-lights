# SPDX-FileCopyrightText: 2024, Rylie Pavlik <rylie@ryliepavlik.com>
#
# SPDX-License-Identifier: MIT
"""
Chasing "comet" red on all pixels, bouncing back and forth.
Think KITT.

Intended for use as code.py
"""

from maskleds import MaskLeds
from pixels import PIXELS_STRIP, CENTER_PIXEL
from adafruit_led_animation.animation.comet import Comet

pixels = MaskLeds(PIXELS_STRIP, CENTER_PIXEL)

anim = Comet(
    pixels,
    speed=0.1,
    color=0x770000,
    tail_length=3,
    bounce=True,
    # Uncommenting this keeps them quite bright, basically pulses them "dark"
    # background_color=0x330000,
)

while True:
    anim.animate()
