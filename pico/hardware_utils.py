"""
Supported hardware

Rotary Encoder: KY-040
OLED: SSD1306
Digital Buttons/Switches
"""

import board
import digitalio
import rotaryio

from adafruit_debouncer import Debouncer


class TrackingIncrementalEncoder(rotaryio.IncrementalEncoder):

    last_position: int = None


switches: dict = {}
encoders: dict = {}


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
    encoder.last_position = encoder.position

    encoders[name] = encoder


def check_all_encoders() -> list:
    """
    Return a list of all encoders that have updated as a tuple (eid, update)
        update is directional, not positional (positive or negative movement)
    """
    updated = []
    for eid, encoder in encoders.items():
        position = encoder.position
        if position != encoder.last_position:
            update = 1 if position > encoder.last_position else -1
            encoder.last_position = position
            updated.append((eid, update))
    return updated
