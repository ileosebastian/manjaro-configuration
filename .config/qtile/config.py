# LIBRARIES
from typing import List  # noqa: F401
# My imports
from groups import init_groups
from keys import init_keys
from keys import init_const_mouse
from keys import group_types
from layouts import init_layouts
from screens import init_screens
from variables import default_font, default_font_size
from my_qtile_functions import autostart
from rules import init_floating_layout
from theming import theme


PYTHONTRACEMALLOC = 1


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
kind = "numbers"

defaut_layouts = {
        'bg_color': 'b9b9b9',
        'active_bg': '717171',
        'active_fg': '868686',
        'inactive_bg': '535353',
        'inactive_fg': '686868',
        'border_focus': '868686',
        'border_focus_fixed': '868686',
        'border_focus_stack': '868686',
        'border_normal': '535353',
        'border_normal_fixed': '535353',
        'border_normal_stack': '535353',
        'border_width': 8,
        'border_width_single': 0,
        'single_border_width': 0,
        'max_border_width': 0,
        'fullscreen_border_width': 0,
        'fontsize': 10,
        'padding_left': 0,
        'grow_amount': 10,
        'lower_right': True,
        'margin': 25,
        'ratio': 0.6,
        'insert_position': 0
}

df_layouts = theme.layouts
df_widgets = theme.widgets

# KEYS
keys = init_keys()
# Drag floating layouts.
mouse = init_const_mouse()

# GROUPS
groups = init_groups(kind)
keys.extend(group_types(groups, kind))

# LAYOUTS
layouts = init_layouts()
floating_layout = init_floating_layout(df_layouts)

# WIDGETS
# widget_defaults = dict(
        # font=default_font,
        # fontsize=default_font_size,
        # padding=2,
# )
widget_defaults = df_widgets
extension_defaults = widget_defaults.copy()

# SCREENS
screens = init_screens()

wmname = "LG3D"  # Neede for some Java apps: LG3D

# My Functions
autostart()
