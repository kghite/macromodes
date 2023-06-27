# macromodes

**Drivers and CLI Tools for configuring a Raspberry Pi Pico MacroPad**

[⌨️ Modes](#modes) &nbsp; [📏 Configuration](#configuration-via-cli-tool) &nbsp; [🪛 Hardware Builds](#hardware-build-options) 
&nbsp;
 [👷 Custom Modes](#adding-modes) &nbsp; [📜 License](#license)

---

## Modes

- 🎹 MIDI Controller
- 🧑‍💻 Development Shortcuts
- 🦾 Data Logger

## Configuration via CLI Tool

The MicroModes CLI application allows you to configure API calls, keybindings, media controls, and other custom macros.

**Step 0: Installation**

**Step 1: Hardware Configuration**

**Step 2: Macro Configuration**

## Hardware Build Options

The MacroPad used to test this tooling is based on the build here: https://www.thingiverse.com/thing:5817044

Currently supported I/O devices:
* Rotary Encoder: KY-040
* OLED Screen: SSD1306
* Digital Switch: Buttons, Keyboard Switches, etc.

## Adding Modes

New modes can be developed 

## Loading CircuitPython Code to the Pico

Once you've extended the base code in the `pico` directory, deploy it to your Macropad using the following steps.

**Step 1**

Update the configuration file `hardware_config.toml` to match your hardware configuration.

**Step 2**

Configure the Raspberry Pi Pico board for Circuit Python: [Adafruit Installing CircuitPython Guide](https://learn.adafruit.com/getting-started-with-raspberry-pi-pico-circuitpython/circuitpython).

**Step 3**

Copy this repository to the `CIRCUITPY` drive.

**Optional**

Install the Mu editor to check for wiring error or send live code updates: [codewithmu](https://codewith.mu/)

## License

This code is freely available under the [MIT License](LICENSE).
