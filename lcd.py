#!/usr/bin/env python
#--- shebang

"""
   LCD Display
"""

from pyA20 import i2c
from time import sleep

I2C_ADDR = 0x3f
ENABLE = 0x04
DATA = 0x01
CMD = 0x00
BLACKLIGHT = 0x08

Alphabet = {
            'A' : 0x41,
            'B' : 0x42,
            'C' : 0x43,
            'D' : 0x44,
            'E' : 0x45,
            'F' : 0x46,
            'G' : 0x47,
            'H' : 0x48,
            'I' : 0x49,
            'J' : 0x4A,
            'K' : 0x4B,
            'L' : 0x4C,
            'M' : 0x4D,
            'N' : 0x4E,
            'O' : 0x4F,
            'P' : 0x50,
            'Q' : 0x51,
            'R' : 0x52,
            'S' : 0x53,
            'T' : 0x54,
            'U' : 0x55,
            'V' : 0x56,
            'W' : 0x57,
            'X' : 0x58,
            'Y' : 0x59,
            'Z' : 0x5A,
            ' ' : 0x20,
            'a' : 0x61,
            'b' : 0x62,
            'c' : 0x63,
            'd' : 0x64,
            'e' : 0x65,
            'f' : 0x66,
            'g' : 0x67,
            'h' : 0x68,
            'i' : 0x69,
            'j' : 0x6A,
            'k' : 0x6B,
            'l' : 0x6C,
            'm' : 0x6D,
            'n' : 0x6E,
            'o' : 0x6F,
            'p' : 0x70,
            'q' : 0x71,
            'r' : 0x72,
            's' : 0x73,
            't' : 0x74,
            'u' : 0x75,
            'v' : 0x76,
            'w' : 0x77,
            'x' : 0x78,
            'y' : 0x79,
            'z' : 0x7A,
            ',' : 0x2C
           }

def delay_ms(time_ms):
    sleep(time_ms / 1000.0)

def delay_us(time_us):
    sleep(time_us / 1000000.0)

def write(byte, mode):
    nibble(byte, mode)
    nibble((byte << 4), mode)
    delay_us(40.0)

def nibble(byte, mode):
    byte = (byte & 0xF0) | mode | BLACKLIGHT
    i2c.write([byte | ENABLE])
    delay_ms(2.0)
    i2c.write([byte & ~ENABLE])
    nibble(byte, mode)
    nibble((byte << 4), mode)
    delay_us(40.0)

def lcd_init(DispSet, EntryMode):
    i2c.init("/dev/i2c-0")
    i2c.open(I2C_ADDR)
    delay_ms(20)
    nibble(0x30, CMD)
    delay_ms(5)
    nibble(0x30, CMD)
    delay_us(110)
    nibble(0x30, CMD)
    nibble(0x20, CMD)
    write(DispSet, CMD)
    write(0x08, CMD)
    write(0x01, CMD)
    write(0x06, CMD)
    write(EntryMode, CMD)

def lcd_message(string):
    message = list(string)
    for x in message:
        write(Alphabet[x], DATA)


def lcd_blinkRow():
    write(0x0C, CMD)
    delay_ms(1000)
    write(0x08, CMD)
    delay_ms(1000)

try:
    #i2c.init("/dev/i2c-0")
    #i2c.open(I2C_ADDR)
    lcd_init(0x28, 0x0C)
    lcd_message("Hello, world")
    while True:
        lcd_blinkRow()
        continue
except KeyboardInterrupt:
    write(0x01, CMD)
    print("Goodbye!")






