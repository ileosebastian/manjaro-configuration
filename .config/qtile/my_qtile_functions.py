from libqtile.lazy import lazy
from libqtile import hook
from libqtile import widget
import os
import subprocess

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


def get_separator():
    return widget.Sep(
                    linewidth=5,
                    padding=0,
                    foreground=current_line,
                    background=background,
                    size_percent=100
                )


@lazy.function
def restart_qtile(qtile):
    qtile.cmd_spawn("setxkbmap us")
    qtile.cmd_restart()


@lazy.function
def change_keymap(qtile):
    qtile.cmd_spawn("changekeymap")

    textbox = qtile.widgets_map["textbox"]
    if textbox.info()["text"] == "ENG":
        qtile.widgets_map["textbox"].update("ESP")
    elif textbox.info()["text"] == "ESP":
        qtile.widgets_map["textbox"].update("ENG")


@hook.subscribe.startup_once
def autostart():
    subprocess.Popen([HOME + '.config/qtile/autostart.sh'])
