# SPDX-FileCopyrightText: 2024, Rylie Pavlik <rylie@ryliepavlik.com>
#
# SPDX-License-Identifier: MIT
"""
NeoPixel objects.

Utility, do not use as code.py
"""

import board
import neopixel

pixel_pin = board.A0
num_pixels = 4

# This is the real version for https://www.adafruit.com/product/4776
# PIXELS_STRIP = neopixel.NeoPixel(pixel_pin, num_pixels, auto_write=False, pixel_order=neopixel.GRBW)

# This version is for the neopixel tape used for testing.
PIXELS_STRIP = neopixel.NeoPixel(pixel_pin, num_pixels, auto_write=False)

# Onboard neopixel
CENTER_PIXEL = neopixel.NeoPixel(board.NEOPIXEL, 1, auto_write=False)


def get_trans_pixel_subsets():
    """Return the pixels for blue, pink, and white in a trans flag."""
    from adafruit_led_animation.helper import PixelMap

    return (
        PixelMap(PIXELS_STRIP, [0, 3], individual_pixels=True),
        PixelMap(PIXELS_STRIP, [1, 2], individual_pixels=True),
        CENTER_PIXEL,
    )
