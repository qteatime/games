init offset = -1

screen quick_menu():
  zorder 100
  if show_quick_menu:
    window:
      style_prefix "quick"
      hbox:
        use quick_menu_button(kate_l_dark, _("ROLLBACK"), action = Rollback())
        key ["kate_l"] action Rollback()
        use quick_menu_button(kate_r_dark, _("SKIP"), action = Skip(), alternate = Skip(fast = True, confirm = True))
        key ["kate_r"] action Skip()
        use quick_menu_button(kate_cancel_dark, _("AUTO-FORWARD"), action = Preference("auto-forward", "toggle"))
        key ["kate_x"] action Preference("auto-forward", "toggle")
        use quick_menu_button(kate_menu_dark, _("MENU"), action = ShowMenu("game_menu"))


screen quick_menu_button(icon, title, **properties):
  button:
    properties properties
    style_prefix "quick_button"

    hbox:
      add icon zoom 0.065 yalign 0.5
      text title

init python:
  config.overlay_screens.append("quick_menu")

style quick_window is empty
style quick_hbox is empty
style quick_button_button is empty
style quick_button_hbox is empty
style quick_button_text is small_gui_text

style quick_window:
  yalign 1.0
  xfill True
  ysize 24
  background white

style quick_hbox:
  xalign 1.0
  xoffset -16
  spacing 15

style quick_button_button:
  yoffset 3

style quick_button_hbox:
  spacing 5

style quick_button_text:
  yalign 0.5
  size 14
  color black
  selected_color gui.accent_color