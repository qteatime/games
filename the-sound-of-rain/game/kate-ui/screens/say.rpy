init offset = -1

screen say(who, what):
  style_prefix "say"

  window:
    id "window"

    if who is not None:
      window:
        id "namebox"
        style "namebox"
        text who id "who"

    text what id "what"
    add SideImage() xalign 0.0 yalign 1.0

screen nvl(dialogue, items=None):
  window:
    style "nvl_window"
    if in_simulation:
      ypos 20
    if in_epilogue:
      ypos 20
      xpos 320
      xsize 400
      xpadding 0
    vbox:
      style "nvl_window_vbox"
      use nvl_dialogue(dialogue)

    for i in items:
      textbutton i.caption:
        action i.action
        style "nvl_button"

screen nvl_dialogue(dialogue):
  for d in dialogue:
    window:
      id d.window_id

      fixed:
        style "nvl_entry_fixed"
        if d.who is not None:
          text d.who:
            id d.who_id

        text d.what:
          id d.what_id
          if in_simulation or in_darkness:
            color white
          else:
            outlines [ (absolute(3), white, absolute(0), absolute(0)) ]

screen skip_indicator():
  zorder 100
  style_prefix "skip"

  frame:
    hbox:
      spacing 4

      add "gui/ctc.png" zoom 0.5 at delayed_blink(0.0, 1.0)
      add "gui/ctc.png" zoom 0.5 at delayed_blink(0.2, 1.0)
      add "gui/ctc.png" zoom 0.5 at delayed_blink(0.4, 1.0)

style skip_frame is empty
style skip_hbox is empty

style skip_frame:
  background white
  ysize 24
  xfill True
  ypos 0

style skip_hbox:
  xalign 1.0
  yalign 0.5
  xoffset -16

init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label

style centered_text:
  size 30
  color white

style nvl_window is empty
style nvl_window_vbox is empty
style nvl_entry is empty
style nvl_entry_fixed is empty
style nvl_label is empty
style nvl_dialogue is empty
style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
  ypos 200
  xpadding 100
  ypadding 20
  background None

style nvl_window_vbox:
  spacing 20

style nvl_entry:
  xfill True

style nvl_entry_fixed:
  yfit True

style nvl_dialogue:
  size 24
  color black
