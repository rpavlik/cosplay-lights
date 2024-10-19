# SPDX-FileCopyrightText: 2024, Rylie Pavlik <rylie@ryliepavlik.com>
#
# SPDX-License-Identifier: MIT
"""
Solid red on the 4 main pixels, with red center pixel slowly brightening and dimming.

Intended for use as code.py
"""

from adafruit_led_animation.animation.pulse import Pulse
from colors import RED
from pixels import PIXELS_STRIP, CENTER_PIXEL

PIXELS_STRIP.fill(RED)
PIXELS_STRIP.brightness = 0.3
PIXELS_STRIP.show()

# See this URL for meaning of parameters
# https://docs.circuitpython.org/projects/led-animation/en/latest/api.html#adafruit-led-animation-animation-pulse
# This time only pulsing the center LED
anim = Pulse(
    CENTER_PIXEL,
    speed=0.1,
    color=RED,
    breath=3,
    period=7,
    max_intensity=0.8,
    min_intensity=0.1,
)

while True:
    anim.animate()
