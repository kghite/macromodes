def encoder_switch_pressed():
    print('MIDI: Encoder switch pressed')


def encoder_updated(name: str, direction: int):
    print(f'MIDI: {name} updated {direction}')


def switch_pressed(name: str):
    print(f'MIDI: {name} pressed')

