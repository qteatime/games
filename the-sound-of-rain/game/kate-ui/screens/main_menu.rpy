init offset = -1

screen main_menu():
  style_prefix "main_menu"
  tag menu
  add black
  add "gui/title.png" yalign 1.0 xalign 1.0 alt "the sound of rain."

  frame:
    vbox:
      use main_menu_button(_("Start"), action = Start(), default_focus = True)
      use main_menu_button(_("Options"), action = ShowMenu("preferences"))

screen main_menu_button(title, **properties):
  button:
    properties properties
    style_prefix "main_menu_button"
    has frame
    text title

style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_button_button is empty
style main_menu_button_text is small_gui_text
style main_menu_button_frame is empty

style main_menu_frame:
  yalign 0.4
  xfill True

style main_menu_vbox:
  xfill True
  spacing 10

style main_menu_button_button:
  ysize 50
  xfill True
  hover_background "gui/line.png"

style main_menu_button_frame:
  xpadding 20
  xalign 0.5
  background black

style main_menu_button_text:
  size 40
  xalign 0.5
  yalign 0.5
  color "#7f7f7f"
  hover_color "#fafafa"