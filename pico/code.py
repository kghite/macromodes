"""
MacroModes
"""

import board
import digitalio

import config
import hardware_utils as hw

import rotaryio

# Dynamic import to sync custom modes
modes = []
for mode in config.modules:
    try:
        modes.append(__import__(mode))
    except ImportError:
        print("Error importing custom module: ", mode)

# TODO: Convert to config
# Set up rotary encoder
hw.create_encoder("Main", board.GP15, board.GP14)
hw.create_switch("Encoder", board.GP13)

# Set up keys
hw.create_switch("K1", board.GP7)

# Set up screen
#hw.create_screen("OLED", board.GP17, board.GP16)

while True:
    # TODO: Cycle mode on key press
    # Update mode
    responses = modes[0]

    # Switches
    for switch in hw.switches.values():
        switch.update()
    pressed = hw.check_all_switches()
    for sid in pressed:
        responses.switch_pressed(sid)

    # Encoders
    updated = hw.check_all_encoders()
    for eid, direction in updated:
        responses.encoder_updated(eid, direction)
