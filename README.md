# Cosplay Lights

Rylie Pavlik

## About

This is some very simple CircuitPython code intended for driving a short series of NeoPixel addressable RGB (or RGBW) LEDs.

The development hardware was a QtPy (SAMD21) Haxpress, then moved to a QtPy RP2040, with LiPoly battery BFF.


## Usage

In case you happen to have been made something by Rylie that uses this:

The device is programmed using CircuitPython, which among other things means it shows up as a USB flash drive when you plug it in. The file
called "code.py" is the one that runs. There are several options for that file (all the files starting with "red" or "trans"), you can read these files in
Notepad (they have info at the top), but basically, if you copy 'trans_flag_new.py' to code.py, you will get a static trans flag pattern (good for
testing), while 'red_breathing.py' copied to code.py is what I imagine you will want for standard cosplay purposes. Feel free to play with the
parameters in that file, I have copies of everything so there is nothing you can break.

There are three files that do not start with "red" or "trans" (`colors.py`, `maskleds.py`, and `pixels.py`), plus some directories. These are required but do not need to be modified.

`pixels.py` is where the pixels actually being used are configured: for development a weatherproof segment of NeoPixel tape was used before moving to the NeoPixel "buttons".

(If you were not told to use this code by Rylie... probably don't use it? I mean, you are welcome to, it is MIT licensed open source, but it's also not the best ever.)
