init offset = -1

python early:
  (
    renpy.register_sl_statement("select", children=0, screen="inline_select")
      .add_positional("options")
      .add_property("label")
      .add_property("value")
      .add_property("tooltip")
      .add_property("default_focus")
      .add_property("on_change")
      .add_property("style_prefix")
  )

  def inline_select_current_index(choices, value, default=0):
    for (index, choice) in enumerate(choices):
      if choice.value == value:
        return index
    return default

  def inline_select_action(choices, index):
    if (index < 0) or (index >= len(choices)):
      return NullAction()
    else:
      return choices[index].action

  def inline_select_text(choices, index):
    if (index < 0) or (index >= len(choices)):
      return ""
    else:
      return choices[index].display

  def inline_select_tooltip(choices, index, default):
    if (index < 0) or (index >= len(choices)):
      return default
    else:
      if choices[index].tooltip is None:
        return default
      else:
        return choices[index].tooltip

  class InlineSelectValue(renpy.object.Object):
    def __init__(self, value, display = None, action = None, tooltip = None):
      self.value = value

      if display is None:
        self.display = "NO"
      else:
        self.display = display

      if action is None:
        self.action = NullAction()
      else:
        self.action = action

      self.tooltip = tooltip

  def inline_select_to_choice(x):
    if isinstance(x, InlineSelectValue):
      return x
    else:
      return InlineSelectValue(
        x["value"],
        display = x.get("display", None),
        action = x.get("action", NullAction),
        tooltip = x.get("tooltip", None)
      )

screen inline_select(options, label = None, value = None, tooltip = None, on_change = lambda: None, default_focus = False, style_prefix = "options_select"):
  $ choices = [inline_select_to_choice(x) for x in options]
  $ current_index = inline_select_current_index(choices, value)
  $ previous_action = inline_select_action(choices, current_index - 1)
  $ next_action = inline_select_action(choices, current_index + 1)
  $ cycle_action = choices[(current_index + 1) % len(choices)].action
  
  button:
    action cycle_action, on_change
    style_prefix style_prefix
    tooltip inline_select_tooltip(choices, current_index, tooltip)
    default_focus default_focus
    
    hbox:
      if label is not None:
        frame:
          style_prefix style_prefix + "_label"
          text label

      frame:
        style style_prefix + "_left_thumb"

      frame:
        style_prefix style_prefix + "_value"
      
        vbox:
          style_prefix style_prefix + "_choice"
          text inline_select_text(choices, current_index)

          hbox:
            style_prefix style_prefix + "_bullet"

            for (i, _) in enumerate(choices):
              if i == current_index:
                add "gui/select-on.png"
              else:
                add "gui/select-off.png"

      frame:
        style style_prefix + "_right_thumb"

      key "kate_left" action [previous_action, on_change] capture True
      key "kate_right" action [next_action, on_change] capture True

