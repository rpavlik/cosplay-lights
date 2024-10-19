# SPDX-FileCopyrightText: 2024, Rylie Pavlik <rylie@ryliepavlik.com>
#
# SPDX-License-Identifier: MIT
"""
Fades in and out a trans pride flag across all 5 pixels.

Intended for use as code.py
"""

from adafruit_led_animation.animation.pulse import Pulse
from adafruit_led_animation.group import AnimationGroup
from colors import TRANS_BLUE, TRANS_PINK, TRANS_WHITE
from pixels import get_trans_pixel_subsets

blue_pixels, pink_pixels, white_pixels = get_trans_pixel_subsets()

anim = AnimationGroup(
    Pulse(blue_pixels, speed=0.1, color=TRANS_BLUE),
    Pulse(pink_pixels, speed=0.1, color=TRANS_PINK),
    Pulse(white_pixels, speed=0.1, color=TRANS_WHITE),
    sync=True,
)


while True:
    anim.animate()
