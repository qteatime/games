init offset = -1

define text_preview = RestartableText(gui.text_preview, slow = True)


init python:
  class PreferencesChangeTab(Action):
    def __init__(self, index, old, tabs):
      self.index = index
      self.old = old
      self.tabs = tabs

    def __call__(self):
      index = self.index
      if index != self.old:
        renpy.display.tts.speak(self.tabs[index])
        renpy.show_screen("preferences", current = index)
        renpy.restart_interaction()
        renpy.display.focus.clear_focus()
        focus_first()

  def focus_first():
    # lifted from renpy.display.focus
    renpy.display.focus.focus_nearest(0.1, 0.9, 0.9, 0.9,
                                      0.1, 0.1, 0.9, 0.1,
                                      renpy.display.focus.horiz_line_dist,
                                      lambda old, new : old.y + old.h <= new.y,
                                      0, -1, 0, 0)

screen preferences(current = 0):
  tag menu
  style_prefix "options_menu"

  $ tabs = [
    _("TEXT"),
    _("AUDIO"),
    _("ACCESSIBILITY")
  ]

  python:
    def on_cps_changed():
      text_preview.update()
      renpy.restart_interaction()

    def make_pct(name):
      pct = [(0.0, _("Mute"))] + [(x / 10.0, "{}%".format(x * 10)) for x in range(1, 11)]
      return [
        {
          "value": v,
          "display": d,
          "action": SetMixer(name, v)
        } for (v, d) in pct
      ]

  add black

  frame:
    style_prefix "options_menu_header"

    $ cur_tab = tabs[current]
    text _("Options") style "options_menu_title" alt _("{} options").format(cur_tab)

    hbox:
      style_prefix "options_menu_tabs"

      key ["kate_r"] action PreferencesChangeTab(min(current + 1, len(tabs) - 1), current, tabs)
      key ["kate_l"] action PreferencesChangeTab(max(current - 1, 0), current, tabs)

      if current > 0:
        $ prev_tab = tabs[current - 1]
        add kate_l_dark zoom 0.1 yalign 1.0 alt _("Press L for {} options").format(prev_tab)
      else:
        add kate_l_dark zoom 0.1 yalign 1.0

      for (index, tab) in enumerate(tabs):
        frame:
          style_prefix "options_menu_tab"

          fixed:
            textbutton tab:
              action ShowMenu("preferences", index)
              selected (index == current)
              keyboard_focus False
            
            if index == current:
              add "gui/tab-indicator.png" xalign 0.5 yoffset 28

      if current < len(tabs) - 1:
        $ next_tab = tabs[current + 1]
        add kate_r_dark zoom 0.1 yalign 1.0 alt _("Press R for {} options").format(next_tab)
      else:
        add kate_r_dark zoom 0.1 yalign 1.0

  fixed:
    style_prefix "options_menu_content"

    vbox:
      style_prefix "options_menu_list"

      if current == 0:
        select [
          {
            "value": False,
            "display": _("SEEN DIALOGUE"),
            "action": SetField(_preferences, "skip_unseen", False),
            "tooltip": _("Skip only previously seen dialogue.")
          },
          {
            "value": True,
            "display": _("ALL DIALOGUE"),
            "action": SetField(_preferences, "skip_unseen", True),
            "tooltip": _("Skip all dialogue.")
          }
        ]:
          label _("SKIP")
          value preferences.skip_unseen
          style_prefix "options_select"

        select [
          {
            "value": True,
            "display": _("KEEP SKIPPING"),
            "action": SetField(_preferences, "skip_after_choices", True),
            "tooltip": _("Continue skipping after hitting a choice")
          },
          {
            "value": False,
            "display": _("STOP SKIPPING"),
            "action": SetField(_preferences, "skip_after_choices", False),
            "tooltip": _("Stop skipping after hitting a choice")
          }
        ]:
          label _("AFTER CHOICES")
          value preferences.skip_after_choices
          style_prefix "options_select"

        $ cps_ranges = [(5, _("VERY SLOW")), (15, _("SLOW")), (30, _("AVERAGE")), (50, _("FAST")), (100, _("VERY FAST")), (0, _("INSTANT"))]
        select [
          {
            "value": v,
            "display": d,
            "action": SetField(_preferences, "text_cps", v)
          } for (v, d) in cps_ranges
        ]:
          label _("TEXT SPEED")
          value preferences.text_cps
          tooltip _("How fast should text be displayed?")
          on_change on_cps_changed
          style_prefix "options_select"


        $ afm_ranges = [(0, _("NEVER")), (30, _("30 SECONDS")), (15, _("10 SECONDS")), (5, _("5 SECONDS"))]
        select [
          {
            "value": v,
            "display": d,
            "action": SetField(_preferences, "afm_time", v)
          } for (v, d) in afm_ranges
        ]:
          label _("AUTO-FORWARD AFTER")
          value preferences.afm_time
          tooltip _("How soon should we advance to the next dialogue?")
          on_change on_cps_changed
          style_prefix "options_select"

        null height 16

        frame:
          style "text_speed_test_container"

          use text_speed_test(text_preview)

      if current == 1:
        select make_pct("music"):
          label _("MUSIC VOLUME")
          value preferences.get_volume("music")
          tooltip _("Volume of the background music channel")

        select make_pct("sfx"):
          label _("SOUND EFFECT VOLUME")
          value preferences.get_volume("sfx")
          tooltip _("Volume of the sound effects channel")

        if config.has_voice:
          select make_pct("voice"):
            label _("VOICE VOLUME")
            value preferences.get_volume("voice")
            tooltip _("Volume of the voice channel")

      if current == 2:
        select [
          {
            "value": 2,
            "display": _("ENABLED"),
            "action": SetField(_preferences, "transitions", 2),
            "tooltip": _("Enable all transitions and animations")
          },
          {
            "value": 0,
            "display": _("DISABLED"),
            "action": SetField(_preferences, "transitions", 0),
            "tooltip": _("Disable all transitions and animations")
          }
        ]:
          label _("TRANSITIONS")
          value preferences.transitions

        select [
          {
            "value": True,
            "display": _("ENABLED"),
            "action": SetField(_preferences, "self_voicing", True),
            "tooltip": _("Enable text-to-speech")
          },
          {
            "value": False,
            "display": _("DISABLED"),
            "action": SetField(_preferences, "self_voicing", False),
            "tooltip": _("Disable text-to-speech")
          }
        ]:
          label _("SELF-VOICING")
          value preferences.self_voicing

        select [
          {
            "value": None,
            "display": _("ORIGINAL FONTS"),
            "action": Preference("font transform", None),
            "tooltip": _("Use the original fonts for all text in the game")
          },
          {
            "value": "opendyslexic",
            "display": _("OPEN DYSLEXIC"),
            "action": Preference("font transform", "opendyslexic"),
            "tooltip": _("Use OpenDyslexic for all text in the game")
          }
        ]:
          label _("TEXT FONT")
          value preferences.font_transform

        $ font_sizes = [(0.8, _("SMALLER")), (1.0, _("ORIGINAL")), (1.2, _("LARGER"))]
        select  [
          {
            "value": v,
            "display": d,
            "action": [SetField(_preferences, "font_size", v), _DisplayReset()]
          } for (v, d) in font_sizes
        ]:
          label _("FONT SIZE")
          value preferences.font_size
          tooltip _("Scale the font sizes of all text in the game")


        select [
          {
            "value": True,
            "display": _("ENABLED"),
            "action": Preference("high contrast text", "enable"),
            "tooltip": "Favour contrast over the game's colours"
          },
          {
            "value": False,
            "display": _("DISABLED"),
            "action": Preference("high contrast text", "disable"),
            "tooltip": "Use the original text colours"
          }
        ]:
          label _("HIGH-CONTRAST TEXT")
          value preferences.high_contrast

  frame:
    style_prefix "options_menu_status"

    hbox:
      style_prefix "options_menu_status_left"

      $ tooltip = GetTooltip()
      if tooltip is not None:
        text tooltip

    hbox:
      style_prefix "options_menu_status_right"
      spacing 5

      add kate_cancel_dark zoom 0.07 alt "Press CANCEL to return."
      if main_menu:
        textbutton _("BACK") alt "" action ShowMenu("main_menu")
        key ["kate_x"] action ShowMenu("main_menu")
      else:
        textbutton _("BACK") alt "" action ShowMenu("game_menu")
        key ["kate_x"] action ShowMenu("game_menu")


style options_menu_header_frame is empty
style options_menu_title is empty
style options_menu_tabs_hbox is empty
style options_menu_tab_frame is empty
style options_menu_tab_fixed is empty
style options_menu_tab_button is empty
style options_menu_tab_text is empty

style options_menu_header_frame:
  ysize 64
  background white
  xpos 0
  ypos 0

style options_menu_title:
  xpos 16
  yalign 1.0
  yoffset 12
  size 40
  color black
  outlines [ (absolute(2), white, absolute(0), absolute(0)) ]

style options_menu_tabs_hbox:
  xalign 1.0
  yalign 1.0
  xoffset -15
  spacing 10

style options_menu_tab_fixed:
  xfit True
  xfill False
  fit_first "width"
  xmaximum 200
  ysize 64
  yoffset 32

style options_menu_tab_button:
  ysize 32
  xpadding 5

style options_menu_tab_button_text:
  size 20
  color "#9f9f9f"
  selected_color black
  yoffset 2


style options_menu_status_text is small_gui_text
style options_menu_status_frame is empty
style options_menu_status_left_hbox is empty
style options_menu_status_left_text is options_menu_status_text
style options_menu_status_right_hbox is empty
style options_menu_status_right_button_text is options_menu_status_text

style options_menu_status_frame:
  yalign 1.0
  ysize 32
  background white

style options_menu_status_left_hbox:
  yalign 0.5
  xfill False
  xoffset 16

style options_menu_status_right_hbox:
  yalign 0.5
  xalign 1.0
  xfill False
  xoffset -16

style options_menu_status_text:
  size 16
  color black


style options_menu_content_fixed is empty
style options_menu_list_vbox is empty

style options_menu_content_fixed:
  xsize 500
  ysize 320
  xalign 0.5
  yoffset 100

style options_menu_list_vbox:
  spacing 5


style preference_item_frame is empty
style preference_item_label is small_gui_text

style preference_item_frame:
  xsize 250
  yalign 0.5

style preference_item_label:
  size 20


style options_select_button is empty
style options_select_hbox is empty
style options_select_text is small_gui_text
style options_select_label_frame is empty
style options_select_label_text is options_select_text
style options_select_thumb is empty
style options_select_left_thumb is options_select_thumb
style options_select_right_thumb is options_select_thumb
style options_select_value_frame is empty
style options_select_choice_vbox is empty
style options_select_choice_text is options_select_text
style options_select_bullet_hbox is empty

style options_select_button:
  xsize 500
  ysize 40
  xpadding 10
  hover_background white

style options_select_text:
  color "#dadada"
  hover_color black

style options_select_label_frame:
  yalign 0.5
  yoffset 4
  xsize 200

style options_select_label_text:
  size 16

style options_select_hbox:
  spacing 10

style options_select_thumb:
  xsize 32
  ysize 32
  yalign 0.5
  yoffset 8

style options_select_left_thumb:
  hover_background im.FactorScale("gui/left-on.png", 0.6)

style options_select_right_thumb:
  hover_background im.FactorScale("gui/right-on.png", 0.6)

style options_select_value_frame:
  yalign 0.5
  xsize 200
  yoffset 4

style options_select_choice_vbox:
  xalign 0.5
  spacing 2

style options_select_choice_text:
  xalign 0.5
  hover_color gui.accent_color
  bold True

style options_select_bullet_hbox:
  xalign 0.5
  spacing 5


style text_speed_test_container is empty

style text_speed_test_container:
  xsize 500
  xpadding 16
  ypadding 16
  background "gui/text-frame.png"
