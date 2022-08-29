# SPDX-FileCopyrightText: 2021 Phillip Burgess for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# MACROPAD Hotkeys example: Safari web browser for Mac

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                    # REQUIRED dict, must be named 'app'
    'name' : 'Bunny Boo', # Application name
    'macros' : [           # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x000040, 'FknWKND', [Keycode.COMMAND, Keycode.OPTION, 'W']),
        (0x200020, 'MUSIC', [Keycode.F4, -Keycode.F4, 'Chrome\n', 0.5,
                              'https://www.youtube.com/watch?v=DXMDWfLclNY\n']),
        (0x000040, 'DANCE', [Keycode.F4, -Keycode.F4, 'Chrome\n', 0.5,
                             'https://dribbble.com/shots/10754795-dancing-couple\n']),      # Scroll up
        # 2nd row ----------
        (0x200020, 'Tab', [Keycode.CONTROL, Keycode.SHIFT, Keycode.TAB]),
        (0x000040, 'HamMsg', 'Arrooo this is hammy! You are da best momma ever!! I cant'
                               'wait to jump on you and snooze and smoochy, and get treats!'
                                'aruff ruff bark'),
        (0x200020, 'LoveMsg', 'I am the luckiest guy alive to have an amazing woman as you in'
                              'my life! My sexy, funny, snuggly, beautiful, loving bunny boo! - F+A G+A'),
        # 3rd row ----------
        (0x000040, 'Reload', [Keycode.COMMAND, 'r']),
        (0x200010, 'Home', [Keycode.COMMAND, 'H']),
        (0x000040, 'Private', [Keycode.COMMAND, 'N']),
        # 4th row ----------
        (0x002020, 'Love', [Keycode.COMMAND, 'n', -Keycode.COMMAND,
                           'https://photos.app.goo.gl/zUmbbNbxqm8QgEQo8\n']),   # Teen Love in new window
        (0x002020, 'Cute', [Keycode.COMMAND, 'n', -Keycode.COMMAND,
                            'https://data.whicdn.com/images/194913184/original.gi\n']),   # Digi-Key in new window
        (0x002020, 'Hammy', [Keycode.COMMAND, 'n', -Keycode.COMMAND,
                             'https://photos.app.goo.gl/XS74ALTCxB552SRr6\n']),  # HamBone in new win
        # Encoder button ---
        (0x000000, '', [Keycode.COMMAND, 'w']) # Close window/tab
    ]
}
