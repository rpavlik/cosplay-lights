# SPDX-FileCopyrightText: 2024, Rylie Pavlik <rylie@ryliepavlik.com>
#
# SPDX-License-Identifier: MIT
"""
Class to combine multiple NeoPixel objects into one virtual string.

Utility, do not use as code.py
"""


class MaskLeds:
    def __init__(self, pixels4, center) -> None:
        self.pixels = pixels4
        self.center = center
        # self.pixel_values = [0, 0, 0, 0, 0]

    def _get_buf_and_index(self, i):
        if i < 2:
            return self.pixels, i
        if i == 2:
            return self.center, 0
        return self.pixels, i - 1

    def __setitem__(self, index, val):

        if isinstance(index, slice):
            # start, stop, step = index.indices(self.pixel_values)
            if index.start is None:
                print(index)
                return
            step = index.step or 1
            start = index.start
            stop = index.stop or start
            for val_i, in_i in enumerate(range(start, stop, step)):
                unit_val = val[val_i]
                buf, bufidx = self._get_buf_and_index(in_i)
                buf[bufidx] = unit_val
        else:
            buf, bufidx = self._get_buf_and_index(index)
            buf[bufidx] = val

    def __getitem__(self, index):
        buf, bufidx = self._get_buf_and_index(index)
        return buf[bufidx]

    def __len__(self):
        return 5

    def show(self):
        self.pixels.show()
        self.center.show()

    def fill(self, color):
        self.pixels.fill(color)
        self.center.fill(color)
