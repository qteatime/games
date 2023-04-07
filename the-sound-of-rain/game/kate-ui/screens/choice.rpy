init python:
  def first_choice(*choices):
    for choice in choices:
      if choice.visible:
        return choice
    return None

  class ChoiceItem(object):
    def __init__(self, title, action, visible = True):
      self.title = title
      self.action = lambda _: action
      self.visible = visible

  class ChoiceTree(object):
    def __init__(self, title, left = None, up = None, right = None, visible = True, **kwargs):
      self.title = title
      self.prefix = kwargs.get("prefix", title + "...")
      self.left = left
      self.up = up
      self.right = right
      self.visible = visible and [x for x in [left, up, right] if x is not None and x.visible]

    def action(self, back):
      return [Hide("choice"), ShowChoices(self, back)]

  class ShowChoices(object):
    def __init__(self, items, back):
      self.items = items
      self.back = back
    
    def __call__(self):
      renpy.show_screen("choice", self.items, self.back)

  class RestartInteraction(object):
    def __call__(self):
      renpy.restart_interaction()

screen choice(items, back = None):
  zorder 300
  modal True
  style_prefix "choice"
  $ current = ShowChoices(items, back)

  fixed:
    add "gui/choice-circle.png" at show_choice_circle
    text items.prefix style "choice_prefix"

    frame:
      style_prefix "choice_status"
      hbox:
        key "kate_l" action Rollback()
        button:
          style_prefix "choice_status_button"
          hbox:
            add kate_l_dark zoom 0.065 yalign 0.5
            text _("ROLLBACK")

        if back is not None:
          key "kate_x" action [Hide("choice"), back]
          button:
            style_prefix "choice_status_button"
            hbox:
              add kate_cancel_dark zoom 0.065 yalign 0.5
              text _("PREVIOUS")
        else:
          key "kate_x" action NullAction()
    
    if items.left is not None and items.left.visible:
      use choice_entry((48, 48, 0.2), icon = kate_left, title = items.left.title, action = items.left.action(current))
      key "kate_left" action [items.left.action(current)]
      null alt _("Press LEFT: {}".format(items.left.title))

    if items.up is not None and items.up.visible:
      use choice_entry((272, -64, 0.4), icon = kate_up, title = items.up.title, action = items.up.action(current))
      key "kate_up" action [items.up.action(current)]
      null alt _("Press UP: {}".format(items.up.title))

    if items.right is not None and items.right.visible:
      use choice_entry((500, 48, 0.6), icon = kate_right, title = items.right.title, action = items.right.action(current))
      key "kate_right" action [items.right.action(current)]
      null alt _("Press RIGHT: {}".format(items.right.title))

screen choice_entry(pos, icon, title, action):
  $ (x, y, delay) = pos
  fixed at show_choice_entry(x, y, delay):
    style_prefix "choice_entry"
    add "gui/choice-line.png" at show_choice_line(0.2)
    button action action:
      hbox:
        add icon zoom 0.08
        text title


style choice_fixed is empty
style choice_entry is empty
style choice_prefix is small_gui_text
style choice_entry_button is empty
style choice_entry_text is small_gui_text
style choice_entry_hbox is empty

style choice_fixed:
  xfill True
  yfill False
  ysize 256
  yalign 1.0
  yoffset 120

style choice_prefix:
  xalign 0.5
  ypos 70
  size 20
  color "#dadada"

style choice_entry:
  xfill False
  yfill False
  xsize 256
  ysize 64
  background "#f00"

style choice_entry_button:
  xsize 256

style choice_entry_text:
  color white
  xalign 0.5
  size 20

style choice_entry_hbox:
  spacing 10
  xalign 0.5

style chioce_status_frame is empty
style choice_status_hbox is empty
style choice_status_button_hbox is empty
style choice_status_button_button is empty
style choice_status_button_text is gui_small_text

style choice_status_frame:
  xfill True
  ysize 24
  yoffset 112
  background white

style choice_status_hbox:
  xalign 1.0
  yalign 0.5
  xoffset -16
  spacing 20

style choice_status_button_text:
  color black
  size 14

style choice_status_button_hbox:
  spacing 5
  yalign 0.5

transform show_choice_circle:
  transform_anchor True
  xalign 0.5
  yanchor 0.5
  yoffset 128
  zoom 0.1
  alpha 0.0

  easeout 0.25 zoom 1.0 alpha 1.0

transform show_choice_entry(x, y, time):
  xoffset x
  yoffset y
  alpha 0.0
  linear time alpha 0.0
  linear 0.2 alpha 1.0

transform show_choice_line(delay):
  xzoom 0.0
  alpha 0.0
  yoffset 32
  
  linear delay alpha 0.0
  easeout 0.2 xzoom 1.0 alpha 1.0