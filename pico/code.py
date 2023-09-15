"""
MacroModes
"""

import board
import digitalio

import hardware_utils as hw

import rotaryio

# Dynamic import for custom modes to keep in sync
modules = ['test_responses', 'midi_responses']
modes = []
for mode in modules:
    try:
        modes.append(__import__(mode))
    except ImportError:
        print('Error importing custom module: ', mode)


switches = []

# TODO: Convert to config
# Set up rotary encoder
hw.create_encoder('main', board.GP15, board.GP14)
hw.create_switch('encoder', board.GP13)
hw.create_switch('K1', board.GP7)

# Set up keys

# Set up screen

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
