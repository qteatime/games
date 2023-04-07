init offset = -2

init python:
  gui.init(800, 480)

define black = "#2f2f2f"
define white = "#fafafa"

define _game_menu_screen = "game_menu"

define gui.game_menu_background = "#fafafa"
define gui.accent_color = '#236E95'

define gui.has_save_states = False

define gui.text_preview = "The rain falls relentlessly outside. Spring will soon be upon us, and mayhap bring with it more stable weather and more vibrant colours."

style default:
  color black
  language "unicode"

style text is empty:
  size 24

style small_gui_text is text:
  color black
  size 18

style gui_preference_text is small_gui_text:
  color "#fafafa"
  hover_color "#2f2f2f"

style button_text is gui_text:
  yalign 0.5