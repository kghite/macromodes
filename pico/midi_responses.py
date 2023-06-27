def encoder_switch_pressed():
    print('MIDI: Encoder switch pressed')


def encoder_updated(direction: int):
    print('MIDI: +') if direction > 0 else print('MIDI: -')
