def encoder_switch_pressed():
    print('LOG: Encoder switch pressed')


def encoder_updated(name: str, direction: int):
    print(f'LOG: {name} updated {direction}')


def switch_pressed(name: str):
    print(f'LOG: {name} pressed')
