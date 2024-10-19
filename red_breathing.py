# SPDX-FileCopyrightText: 2024, Rylie Pavlik <rylie@ryliepavlik.com>
#
# SPDX-License-Identifier: MIT
"""
Solid red on the 4 main pixels, slowly brightening and dimming.

Intended for use as code.py
"""

from adafruit_led_animation.animation.pulse import Pulse

from colors import RED
from pixels import PIXELS_STRIP

# See this URL for meaning of parameters
# https://docs.circuitpython.org/projects/led-animation/en/latest/api.html#adafruit-led-animation-animation-pulse
anim = Pulse(
    PIXELS_STRIP,
    speed=0.1,
    color=RED,
    breath=3,
    period=10,
    max_intensity=0.5,
    min_intensity=0.1,
)

while True:
    anim.animate()
