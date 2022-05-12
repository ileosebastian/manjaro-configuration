from libqtile import bar
from libqtile import widget
from libqtile.config import Screen
from libqtile.lazy import lazy
from my_qtile_functions import get_separator
from my_qtile_functions import change_keymap
import arcobattery
import os


HOME = os.path.expanduser('~/')

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


def init_screens():
    return [
        Screen(
            bottom=bar.Bar(
                [
                    widget.GroupBox(
                        active=green,
                        this_current_screen_border=comment,
                        this_screen_border=yellow,
                        inactive=current_line,
                        urgent_alert_method='block',
                        urgent_border=red,
                        foreground=foreground,
                        disable_drag=True,
                        highlight_method='block',
                        border=red,
                        borderwidth=1,
                        font=default_font,
                        fontsize=24,
                        padding=0,
                        padding_x=8, padding_y=2,
                        margin=10,
                        margin_x=0, margin_y=4
                    ),
                    get_separator(),
                    widget.Prompt(
                        background=current_line,
                        foreground=pink
                    ),
                    widget.Spacer(),
                    widget.Net(
                        background=pink,
                        foreground=foreground,
                        format="{down}   {up}",
                        interface="wlp1s0"
                    ),
                    get_separator(),
                    widget.HDDBusyGraph(
                        background=background,
                        border_color=current_line,
                        fill_color=comment,
                        graph_color=cyan,
                        type="linefill",
                        space_type="used"
                    ),
                    get_separator(),
                    widget.Memory(
                        background=orange,
                        foreground=background,
                        fmt="﬙{}",
                        measure_mem="M"
                    ),
                    get_separator(),
                    widget.CPU(
                        background=yellow,
                        foreground=background,
                        fmt=" {}",
                        format="{freq_current}GHz {load_percent}%"
                    ),
                    get_separator(),
                    widget.ThermalSensor(
                        background=current_line,
                        tag_sensor="Tctl",
                        fmt=" {} | ",
                    ),
                    widget.ThermalSensor(
                        background=current_line,
                        tag_sensor="edge",
                        fmt=" {}",
                    ),
                    get_separator(),
                    widget.Volume(
                        background=cyan,
                        foreground=current_line,
                        fmt="  {}"
                    ),
                    get_separator(),
                    widget.TextBox(
                        background=red,
                        foreground=foreground,
                        font='sans',
                        fontsize=32,
                        fmt="",
                        padding=5,
                        mouse_callbacks={
                            "Button1": lazy.spawn("oblogout")
                        }
                    ),
                ],
                bar_size-6,
                background=bar_bg_color,
                border_width=[2, 2, 0, 2],  # Draw top and bottom borders
                border_color=["#44475a", "#44475a", current_line, "#44475a"]
            ),
            top=bar.Bar(
                [
                    widget.CurrentLayoutIcon(
                        background=background,
                        foreground=red,
                        scale=0.8,
                        fontsize=20,
                        padding=5,
                    ),
                    get_separator(),
                    widget.WindowName(
                        foreground=foreground,
                        fontsize=16,
                        padding=5,
                        fmt=" {}"
                    ),
                    get_separator(),
                    widget.CheckUpdates(
                        background=yellow,
                        colour_have_updates=red,
                        colour_no_updates=background,
                        fontsize=20,
                        padding=5,
                        display_format="{updates} ﮮ",
                        no_update_string="0 ﮮ",
                        update_interval=3600,
                        distro="Arch_checkupdates"
                    ),
                    widget.Systray(
                        background=current_line,
                        icon_size=22,
                        padding=5
                    ),
                    get_separator(),
                    widget.TextBox(
                        background=current_line,
                        foreground=green,
                        fmt="{}",
                        text="ENG",
                        mouse_callbacks={
                            "Button1": change_keymap
                        }
                    ),
                    get_separator(),
                    widget.Clock(
                        # format='%d/%m/%Y %A %H:%M',
                        format=' %d/%m/%Y %A  神 %H:%M',
                        font="Agave Nerd Font Bold",
                        background=purple,
                        foreground=background
                    ),
                    get_separator(),
                    widget.Backlight(
                        background=background,
                        foreground=foreground,
                        backlight_name="amdgpu_bl0",
                        fmt="{} |"
                    ),
                    widget.Battery(
                        background=background,
                        low_background=red,
                        low_foreground=foreground,
                        foreground=foreground,
                        format="{char} {percent:2.0%}",
                        charge_char="",
                        discharge_char="",
                        empty_char="",
                        full_char="F",
                        update_interval=10,
                    ),
                    arcobattery.BatteryIcon(
                        padding=-1,
                        scale=0.8,
                        y_poss=1,
                        scaleadd=1,
                        theme_path=HOME +
                        ".config/qtile/resources/battery_icons_horiz",
                        update_interval=5,
                        background=background
                    )
                ],
                (bar_size-6),
                background=bar_bg_color,
                border_width=[0, 2, 2, 2],  # Draw top and bottom borders
                border_color=["#44475a", "#44475a", current_line, "#44475a"]
            ),
        ),
    ]