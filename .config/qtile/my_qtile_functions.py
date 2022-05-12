from libqtile.lazy import lazy
from libqtile import hook
from libqtile import widget
import os
import subprocess

from variables import background, current_line, foreground, comment, cyan
from variables import green, orange, pink, purple, red, yellow
from variables import HOME, default_font, default_font_size
from variables import bar_bg_color, bar_size


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
