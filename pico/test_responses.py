def encoder_switch_pressed():
    print('TEST: Encoder switch pressed')


def encoder_updated(direction: int):
    print('TEST: +') if direction > 0 else print('TEST: -')
