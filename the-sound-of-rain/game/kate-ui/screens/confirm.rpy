init offset = -1

screen confirm(message, yes_action, no_action):
  modal True
  zorder 400
  style_prefix "confirm"

  add "#2f2f2fcc"

  frame:
    vbox:
      label _(message):
        style "confirm_prompt"
    
      hbox:
        textbutton _("YES") action yes_action 
        textbutton _("NO") action no_action

  key "game_menu" action no_action

style confirm_frame is empty
style confirm_prompt is empty
style confirm_vbox is empty
style confirm_hbox is empty
style confirm_prompt_text is small_gui_text
style confirm_button is empty
style confirm_button_text is small_gui_text

style confirm_frame:
  background Frame("gui/white-frame.png", Borders(10, 10, 10, 10), tile = True)
  xpadding 20
  ypadding 20
  xsize 600
  yfill False
  xalign 0.5
  yalign 0.5

style confirm_vbox:
  spacing 40

style confirm_prompt:
  xfill True

style confirm_prompt_text:
  xalign 0.5
  text_align 0.5
  size 24

style confirm_hbox:
  spacing 50
  xalign 0.5
  
style confirm_button_text:
  size 20
  color "#9f9f9f"
  hover_color gui.accent_color