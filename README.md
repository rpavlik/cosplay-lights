# Cosplay Lights

Rylie Pavlik

## About

This is some very simple CircuitPython code intended for driving a short series of NeoPixel addressable RGB (or RGBW) LEDs.

The development hardware was a QT Py (SAMD21) "Haxpress" (with the added SPI Flash), then moved to a QT Py RP2040, with LiPoly battery BFF.

In addition to the three files not named "red" or "trans", plus one of those renamed to "code.py" (see below),
The following dependencies are needed, for at least some of the patterns.
I use circup to get them installed.

- adafruit_led_animation
- adafruit_fancyled
- neopixel

## Usage

In case you happen to have been made something by Rylie that uses this:

The device is programmed using CircuitPython, which among other things means it shows up as a USB flash drive when you plug it in. The file
called "code.py" is the one that runs. There are several options for that file (all the files starting with "red" or "trans"), you can read these files in
Notepad (they have info at the top), but basically, if you copy 'trans_flag_new.py' to code.py, you will get a static trans flag pattern (good for
testing), while 'red_breathing.py' copied to code.py is what I imagine you will want for standard cosplay purposes. Feel free to play with the
parameters in that file, I have copies of everything so there is nothing you can break.

There are three files that do not start with "red" or "trans" (`colors.py`, `maskleds.py`, and `pixels.py`), plus some directories. These are required but do not need to be modified.

`pixels.py` is where the pixels actually being used are configured: for development a weatherproof segment of NeoPixel tape was used before moving to the NeoPixel "buttons".

**If you were not told to use this code by Rylie**... probably don't use it?
I mean, you are welcome to use it at your own risk, it is MIT licensed open source,
but it's also not the best ever.
(`maskleds.py` is pretty cool, though.)
**I did this as a favor to a friend**, and will be adapting it for my own future use,
but this was the first actual project I did start-to-finish with addressable LEDs.
So see <https://learn.adafruit.com> for actual tutorials and things.

## Bill of Materials

For one particular "embodiment", where four neopixels plus the one on the QT Py board were used.

| AdaFruit PID | Desc | Unit Price | Qty | Price | URL |
|--------------|------|------------|-----|-------|-----|
| 4776 | NeoPixel RGBW Mini Button PCB - Pack of 10 | $4.95 | 0.4 | $1.98 | <http://adafru.it/4776> |
| 4900 | Adafruit QT Py RP2040 | $9.95 | 1 | $9.95 | <http://adafru.it/4900> |
| 5397 | Adafruit LiIon or LiPoly Charger BFF Add-On for QT Py | $4.95 | 1 | $4.95 | <http://adafru.it/5397> |
| 3064 | JST 2-pin Extension Cable with On/Off Switch - JST PH2 | $2.95 | 1 | $2.95 | <http://adafru.it/3064> |