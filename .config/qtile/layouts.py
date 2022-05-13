from libqtile import layout
from libqtile.config import Match
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

def init_floating_layouts():
    return layout.Floating(
            float_rules=[
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
