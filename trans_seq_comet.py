# SPDX-FileCopyrightText: 2024, Rylie Pavlik <rylie@ryliepavlik.com>
#
# SPDX-License-Identifier: MIT
"""
Sequential "comets" in trans blue, pink, and white, on all pixels.

Intended for use as code.py
"""
from adafruit_led_animation.animation.comet import Comet
from adafruit_led_animation.sequence import AnimationSequence
from maskleds import MaskLeds
from colors import TRANS_BLUE, TRANS_PINK, TRANS_WHITE
from pixels import PIXELS_STRIP, CENTER_PIXEL

pixels = MaskLeds(PIXELS_STRIP, CENTER_PIXEL)


anim = AnimationSequence(
    Comet(pixels, speed=0.1, color=TRANS_BLUE, tail_length=3, bounce=False),
    Comet(pixels, speed=0.1, color=TRANS_PINK, tail_length=3, bounce=False),
    Comet(pixels, speed=0.1, color=TRANS_WHITE, tail_length=3, bounce=False),
    advance_on_cycle_complete=True,
    auto_clear=True,
)


while True:
    anim.animate()
