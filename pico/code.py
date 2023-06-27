"""
MacroModes
"""

import board
import digitalio

import hardware_utils as hw

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
# Test rotary encoder
hw.create_encoder('main', board.GP15, board.GP14)
hw.create_switch('encoder', board.GP13)
hw.create_switch('K1', board.GP7)

while True:
    # TODO: Cycle mode on key press
    # Update mode
    responses = modes[0]

    # Test switches
    for switch in hw.switches.values():
        switch.update()

    pressed = hw.check_all_switches()
    if len(pressed) > 0:
        print(pressed)
    updated = hw.check_all_encoders()
