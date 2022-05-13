# LIBRARIES
from typing import List  # noqa: F401
# My imports
from groups import init_groups
from keys import init_keys
from keys import init_const_mouse
from keys import group_types
from layouts import init_layouts, init_floating_layouts
from screens import init_screens
from variables import default_font, default_font_size
from my_qtile_functions import autostart


PYTHONTRACEMALLOC = 1


# KEYS
keys = init_keys()


# GROUPS
kind = "numbers"
groups = init_groups(kind)
keys.extend(group_types(groups, kind))


# LAYOUTS
layouts = init_layouts()
floating_layout = init_floating_layouts()


# WIDGETS
widget_defaults = dict(
        font=default_font,
        fontsize=default_font_size,
        padding=2,
)
extension_defaults = widget_defaults.copy()


# SCREENS
screens = init_screens()


# Drag floating layouts.
mouse = init_const_mouse()


# VARIABLE SETTINGS
dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wmname = "LG3D"  # Neede for some Java apps: LG3D


# My Functions
autostart()
