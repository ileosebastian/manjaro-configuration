from libqtile import layout
from variables import background, current_line, foreground, comment, cyan
from variables import green, orange, pink, purple, red, yellow


def init_layouts():
    return [
        layout.Columns(
            border_focus=green,
            border_focus_stack=[comment, green],
            border_normal=current_line,
            border_width=3,
            margin=10
        ),
        layout.Max(),
    ]
