init offset = -1

screen game_menu(*args, **kwargs):
  style_prefix "game_menu"
  tag menu

  add black
  add "gui/title.png" yalign 1.0 xalign 1.0 alt "the sound of rain."

  frame:
    vbox:
      use game_menu_button(_("Options"), action = ShowMenu("preferences"), default_focus = True)
      use game_menu_button(_("To title"), action = MainMenu())
      use game_menu_button(_("Return"), action = Return())

screen game_menu_button(title, **properties):
  button:
    properties properties
    style_prefix "game_menu_button"
    has frame
    text title

style game_menu_frame is main_menu_frame
style game_menu_vbox is main_menu_vbox
style game_menu_button_button is main_menu_button_button
style game_menu_button_text is main_menu_button_text
style game_menu_button_frame is main_menu_button_frame
