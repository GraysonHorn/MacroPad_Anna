# SPDX-FileCopyrightText: 2021 Phillip Burgess for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# MACROPAD Hotkeys: Evernote web application for Mac
# Contributed by Redditor s010sdc

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values
from adafruit_hid.mouse import Mouse


app = {                      # REQUIRED dict, must be named 'app'
    'name' : 'Slack', # Application name
    'macros' : [             # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x004000, 'Srch', [Keycode.COMMAND, 'G']),
        (0x004000, 'LstUnrd', [Keycode.OPTION, Keycode.SHIFT, Keycode.UP_ARROW]),
        (0x004000, 'NxtUnrd', [Keycode.OPTION, Keycode.SHIFT, Keycode.DOWN_ARROW]),
        # 2nd row ----------
        (0x002020, 'OpnUnrd', [Keycode.COMMAND, Keycode.SHIFT, 'A']),
        (0x002020, 'MrkRd', [Keycode.SHIFT, Keycode.ESCAPE]),
        (0x002020, 'MrkUnrd', [Keycode.OPTION, {'buttons':Mouse.LEFT_BUTTON}]),
        # 3rd row ----------
        (0x400040, 'NewMsg', [Keycode.COMMAND, 'N']),
        (0x400040, 'Undo', [Keycode.COMMAND, 'Z']),
        (0x400040, 'SetStat', [Keycode.COMMAND, Keycode.SHIFT, 'Y']),
        # 4th row ----------
        (0x000000, 'Star', [Keycode.COMMAND, Keycode.SHIFT, Keycode.BACKSLASH, -Keycode.COMMAND, -Keycode.SHIFT,
                            -Keycode.BACKSLASH, 'star-struck\n']),
        (0x800000, 'Panda', [Keycode.COMMAND, Keycode.SHIFT, Keycode.BACKSLASH, -Keycode.COMMAND, -Keycode.SHIFT,
                             -Keycode.BACKSLASH, 'panda\n']),
        (0x101010, 'Dance', [Keycode.COMMAND, Keycode.SHIFT, Keycode.BACKSLASH, -Keycode.COMMAND, -Keycode.SHIFT,
                             -Keycode.BACKSLASH, 'dance\n']),
        # Encoder button ---
        (0x000000, 'SECRET', ['Anna accidentally clicked the secret button it says that Gray loves her!'])
    ]
}
