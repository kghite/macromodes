"""
Supported hardware

Rotary Encoder: KY-040
OLED: SSD1306
Digital Buttons/Switches
"""


import adafruit_displayio_ssd1306
import board
import busio
import digitalio
import displayio
import rotaryio

from adafruit_debouncer import Debouncer


class TrackingIncrementalEncoder:
    # https://stackoverflow.com/questions/75387394/subclassing-weird-behavior-in-circuitpython
    def __init__(self, gpio1, gpio2):
        self.io = rotaryio.IncrementalEncoder(gpio1, gpio2)
        self.last_position = 0


switches: dict = {}
encoders: dict = {}
screens: dict = {}


def create_switch(name: str, gpio):
    """
    Creates a new debounced button and adds it to the switches dict as
        Key - switch id (sid): string
        Value - switch object: Debouncer
    """
    pin = digitalio.DigitalInOut(gpio)
    pin.direction = digitalio.Direction.INPUT
    pin.pull = digitalio.Pull.UP
    switch = Debouncer(pin)
    switches[name] = switch


def check_all_switches() -> list:
    """
    Return a list of all switches that were "just pressed"
        as defined by the Adafruit Debouncer
    """
    # Compile all just pressed ids
    just_pressed = []
    for sid, switch in switches.items():
        if switch.fell:
            just_pressed.append(sid)
    return just_pressed


def create_encoder(name, gpio1, gpio2):
    """
    Creates a new tracked encoder and adds it to the encoders dict as
        Key - enocder id (eid): string
        Value - encoder object: TrackingIncrementalEncoder
    """
    encoder = TrackingIncrementalEncoder(gpio1, gpio2)
    encoders[name] = encoder


def check_all_encoders() -> list:
    """
    Return a list of all encoders that have updated as a tuple (eid, update)
        update is directional, not positional (positive or negative movement)
    """
    updated = []
    for eid, encoder in encoders.items():
        position = encoder.io.position

        if position != encoder.last_position:
            update = 1 if position > encoder.last_position else -1
            encoder.last_position = position
            updated.append((eid, update))
    return updated


def create_screen(name, scl, sda):
    """
    Creates a new oled screen and adds it to the screens dict as
        Key - oled id (oid): string
        Value - screen object: TODO
    """
    i2c = busio.I2C(scl=scl, sda=sda)
    display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)
    display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)
