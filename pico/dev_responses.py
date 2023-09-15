def encoder_switch_pressed():
    print('DEV: Encoder switch pressed')


def encoder_updated(name: str, direction: int):
    print(f'DEV: {name} updated {direction}')


def switch_pressed(name: str):
    print(f'DEV: {name} pressed')
