# SPDX-FileCopyrightText: 2024, Rylie Pavlik <rylie@ryliepavlik.com>
#
# SPDX-License-Identifier: MIT
"""
Old solid trans flag.

Intended for use as code.py
"""

import board
import neopixel
import adafruit_fancyled.adafruit_fancyled as fancy

TRANS_BLUE = fancy.CRGB(91, 206, 250)  # 0x5bcefa
TRANS_PINK = fancy.CRGB(245, 169, 184)  # 0xf5a9b8
TRANS_WHITE = fancy.CRGB(255, 255, 255)

pixel_pin = board.A0
num_pixels = 4

# pixels = neopixel.NeoPixel(pixel_pin, num_pixels, auto_write=False, pixel_order=neopixel.GRBW)
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, auto_write=False)
center_pixel = neopixel.NeoPixel(board.NEOPIXEL, 1, auto_write=False)


TRANS_FLAG = (TRANS_BLUE, TRANS_PINK, TRANS_WHITE, TRANS_PINK, TRANS_BLUE)
levels = (0.35, 0.25, 0.25)


def set_pixels(far_left, left, center, right, far_right):
    pixels[0] = fancy.gamma_adjust(far_left, brightness=levels).pack()
    pixels[1] = fancy.gamma_adjust(left, brightness=levels).pack()
    center_pixel[0] = fancy.gamma_adjust(center).pack()
    pixels[2] = fancy.gamma_adjust(right, brightness=levels).pack()
    pixels[3] = fancy.gamma_adjust(far_right, brightness=levels).pack()
    pixels.show()
    center_pixel.show()


set_pixels(*TRANS_FLAG)
