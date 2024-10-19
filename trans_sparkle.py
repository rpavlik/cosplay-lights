# SPDX-FileCopyrightText: 2024, Rylie Pavlik <rylie@ryliepavlik.com>
#
# SPDX-License-Identifier: MIT
"""
This one is kind of painful to look at. Flickers a trans pride flag on all 5 pixels.

Intended for use as code.py
"""

from adafruit_led_animation.animation.sparkle import Sparkle
from adafruit_led_animation.group import AnimationGroup
from maskleds import MaskLeds
from colors import TRANS_BLUE, TRANS_PINK, TRANS_WHITE
from pixels import PIXELS_STRIP, CENTER_PIXEL

pixels = MaskLeds(PIXELS_STRIP, CENTER_PIXEL)
sparkles = AnimationGroup(
    Sparkle(pixels, speed=0.1, color=TRANS_BLUE, mask=[0, 4]),
    Sparkle(pixels, speed=0.1, color=TRANS_PINK, mask=[1, 3]),
    Sparkle(pixels, speed=0.1, color=TRANS_WHITE, mask=[2]),
    sync=True,
)


while True:
    sparkles.animate()
