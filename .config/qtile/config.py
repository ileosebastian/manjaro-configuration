'''
    LIBRARIES
'''
from typing import List  # noqa: F401

from libqtile import layout
from libqtile.config import Click, Drag, Key, Match
from libqtile.lazy import lazy

# My imports

from groups import init_groups
from keys import init_keys
from keys import init_const_mouse
from keys import group_types
from layouts import init_layouts
from screens import init_screens
from my_qtile_functions import autostart


PYTHONTRACEMALLOC = 1

mod = "mod4"
terminal = "alacritty"

# My variables
# Dracula Color Palette
background = "#282a36"
current_line = "#44475a"
foreground = "#f8f8f2"
comment = "#6272a4"
cyan = "#8be9fd"
green = "#50fa7b"
orange = "#ffb86c"
pink = "#ff79c6"
purple = "#bd93f9"
red = "#ff5555"
yellow = "#f1fa8c"

default_font = "Agave Nerd Font"
default_font_size = 16

bar_bg_color = background
bar_size = 28

# --- global var to functions


'''
    KEYS
'''
keys = init_keys()


'''
    GROUPS
'''
kind = "numbers"
groups = init_groups(kind)
keys.extend(group_types(groups, kind))


'''
    LAYOUTS
'''
layouts = init_layouts()


'''
    WIDGETS
'''
widget_defaults = dict(
    font=default_font,
    fontsize=default_font_size,
    padding=2,
)
extension_defaults = widget_defaults.copy()


'''
    SCREENS
'''
screens = init_screens()


'''
    MOUSE LAYOUTS
'''
# Drag floating layouts.
mouse = init_const_mouse()

'''
    VARIABLE SETTINGS
'''
dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False


floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class='confirmreset'),  # gitk
        Match(wm_class='makebranch'),  # gitk
        Match(wm_class='maketag'),  # gitk
        Match(wm_class='ssh-askpass'),  # ssh-askpass
        Match(title='branchdialog'),  # gitk
        Match(title='pinentry'),  # GPG key password entry
        Match(wm_class="oblogout"),
        Match(wm_class="notification"),
    ],
    border_focus=current_line,
    border_normal=comment,
    border_width=1
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# Needed for some Java apps
# wmname = "LG3D"
wmname = "LG3D"


'''
    FUNCTIONS
'''
autostart()