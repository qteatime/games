define ctc_image = ConditionSwitch(
  "in_simulation or in_darkness", kate_down,
  "True", kate_down_dark
)
define page_ctc_image = ConditionSwitch(
  "in_simulation or in_darkness", kate_right,
  "True", kate_right_dark
)
define ctc = At(ctc_image, animate_ctc)
define config.nvl_page_ctc = At(page_ctc_image, animate_page_ctc)

define show_quick_menu = False
define in_simulation = False
define in_darkness = False
define in_epilogue = False
define narrator = Character(None, kind = nvl, ctc = ctc, ctc_position = "nestled-close")
define menu = nvl_menu

image cg1_bg = "cg/cg1-bg.png"
image cg1 = "cg/cg1.png"
image cg2_bg = "cg/cg2-bg.png"
image cg2 = "cg/cg2.png"
image cg3_bg = "cg/cg3-bg.png"
image cg3 = "cg/cg3.png"

label content_warning:
  scene black
  show screen content_warning()
  with dissolve
  pause
  hide screen content_warning
  scene black
  with dissolve
  with Pause(0.5)
  return

label start:
  $ show_quick_menu = False
  $ reset_state()
  scene black

  call content_warning

  $ renpy.suspend_rollback(True)

  centered "{cps=15}Sis always told me that ghosts aren't real.{w=3.0}{nw}"
  centered "{cps=15}That when we die we just disappear.{w=3.0}{nw}"
  centered "{cps=5}Forever.{w=3.0}{nw}"
  $ renpy.suspend_rollback(False)
  stop music fadeout 1.0

  $ show_quick_menu = True

  scene expression Solid(white) with dissolve
  pause 1.0

  show cg1_bg with dissolve
  show cg1 with dissolve

  "The rain falls relentlessly outside."
  
  "Spring will soon be upon us. And perhaps bring with it more stable weather; more vibrant colours."

  nvl clear

  "From the veranda I watch the rain drops fall on the garden.{w=0.5} Listen to the clinking sound they make when they hit the roof tiles.{w=0.5} Hum to the melody of their drumming."

  "Aunt Nada was late, again."

  nvl clear

  scene black with dissolve
  $ in_darkness = True

  "Sighing, I turn on my heels and walk down the hallway."
  
  "I pass by a couple of gas lamps, hanging unlit from the walls, and head upstairs."

  nvl clear

  $ in_darkness = False

  scene expression Solid(white) with dissolve
  show cg2_bg with dissolve
  show cg2 with dissolve

  "Sunlight still shines outside, with its orange light filtering through the window at the end of the corridor. A hint of red and purple taking over it."

  "Night falls quicker than you'd expect here, around this time. I make a mental note to light the lamps later."

  nvl clear

  "Aunt Nada doesn’t like when I leave the lamps burning for long, but I enjoy their bright and warm company."

  nvl clear

  "Turning around, I take a moment to survey the rooms in the house."
  
  "Aunt Nada’s is closed, like usual."
  
  "Mine, across it, has its door ajar. The messy bed fairly visible from where I stand."

  nvl clear

  "And Sis’ room, right beside mine, is...{w=1.0} shut."
  
  "The old wooden sign with her name, lovingly carved by Aunt Nada, still hangs from the door."
  
  "The same way it did this morning."

  nvl clear

  "In the past I’d feel so alone in this place.{w=1.0} Suffocated by my own presence."
  
  "I’d knock on Sis’ door and sit there, with my back pressed against it."

  "And we’d talk for hours."

  nvl clear

  "Sometimes I’d fall asleep right there. And would open my half-awake eyes to the sight of Aunt Nada carrying me to bed."
  
  "She’d smile, apologetically, and say, “My, now. Forgive me, child. I did not mean to wake you up.”"

  nvl clear

  "Like a caring old woman."
  
  "Though her years still counted in the forties."

  nvl clear

  "Time pressed on like this."
  
  "Springs came and went.{w=0.5} Winters gave way to summers.{w=0.5} And summers dissolved into autumns."
  
  "Until I realised I wasn’t alone anymore."

  nvl clear

  "Not in this house."

  nvl clear

  scene black with dissolve
  $ in_darkness = True

  "I bring down the stairs that lead to the attic, and slowly climb up."

  stop music fadeout 1.0

  "The hatch opens with some effort and I pull myself towards the dimly lit space."

  nvl clear

  "I’m still holding the hatch, while standing on my knees, when I hear something scuttle behind my back."
  
  "I turn around, pointing the lamp in the direction of the sound."

  nvl clear

  "As I let go of it, the hatch closes with a loud thump. I’m left to the slow, sinking realisation that I forgot to bring a lamp upstairs."
  
  "My hand lingers there for a moment more, holding nothing in particular, as darkness surrounds me."

  nvl clear

  "I pull on the hatch, but it’s no use. It hasn’t been used in a long time.{w=1.0} And every time Aunt Nada asked me to check up on it I’d come up with a different excuse to avoid coming here."

  "Now it came back to haunt me."

  nvl clear

  "The scuttle sounds around me sometimes feel distant. And sometimes too close for comfort."
  
  "Rats...?{w=1.0} Roaches...?{w=1.0} I wouldn’t be surprised."

  "But what if..."

  nvl clear

  "\n\nWhat if they were not just... little creatures?"

  nvl clear

  "Mother often told me what happened to exiled witches.{w=1.0} Witches who failed to fill their Role."

  "Tales that I was once sure were only meant to scare children into doing her bidding."

  "Tales that fill my mind even now."

  nvl clear

  "There's that growing sense of uneasiness I'm too familiar with, crawling at my chest."
  
  "It's how it starts."
  
  "I can't stay here. Not for long."

  nvl clear

  "Aunt Nada put so many old things up in the attic that there must be something I can use to open this hatch."

  nvl clear

  jump simulation

label simulation:
  scene black

  $ in_darkness = True
  $ in_simulation = True
  call search_tutorial
  $ in_simulation = False
  
  nvl clear

  "That there are so many boxes in this attic isn't very surprising. Aunt Nada rarely parts with things."
  
  "That's why I came here."

  "But that doesn't matter now.{w=0.5} The thing I wanted to show Sis will have to wait;{w=1.0} I can feel it in my chest."

  nvl clear

  stop music fadeout 5.0

  "I take a deep breath."

  "And another.{w=1.0} And another.{w=1.0} And another."

  "Like Aunt Nada taught me."
  
  "It's not like Mother's magic, but sometimes it works.{w=1.0} Sometimes it's all I have."

  nvl clear

  stop music
  
  "The scuttling seems to be gone now."

  "For now."
  
  "I don't know when it'll be back, but I think I could take my time looking around."

  nvl clear

  "...unless Mother was right."
  
  "About this."
  
  "About me."

  nvl clear

  "I sigh."

  "There's no point dwelling in that."
  
  "It's in the past now."
  
  "Mother is not here anymore."

  nvl clear

  $ in_simulation = True
  call search_simulation
  $ in_simulation = False

  stop music fadeout 1.0

  jump epilogue

label epilogue:
  $ in_darkness = False
  $ in_epilogue = True

  scene black
  with dissolve
  scene expression Solid(white)
  with dissolve
  pause 1.0
  show cg3_bg with dissolve
  show cg3 with dissolve

  "I leave the attic and make my way to the veranda, holding the old photo album against my chest."
  
  "Wishing these memories would fill my heart in some way."

  nvl clear

  "Has it been two years already?"

  "I’ve watched Sis’ illness worsen."
  
  "Watched her lose hope in her research."
  
  "Watched her move to the city under Mother’s pressure."

  nvl clear

  "I couldn’t say anything right to her back then."
  
  "No matter how much I asked."

  "No matter how much I said I was there for her."
  
  "It always went the same way."

  nvl clear

  "She’d force a smile."
  
  "Tell me that “ghosts aren’t real.”"
  
  "That her research wasn’t getting anywhere, anyway."
  
  nvl clear

  "By the time she moved she had gotten so good at saying these little lines. It almost came as second nature to her."
  
  "No more pauses."

  nvl clear

  "But when I look at her in these photos, her eyes are sparkling."

  "So much that I have to wonder what took her life away first."
  
  "The illness, slowly eating at her."
  
  "Or the traditions, gradually pushing her away."

  nvl clear

  "I don’t think Mother and I mourned the same person."

  "There was a witch who excelled at what Mother had divined, yes."

  "But there was also a kid who always chased after what she believed in.{w=1.0} Regardless of what those around her would think."

  nvl clear

  "The friend who was there for me whenever I needed a hug."

  "Whose smile could make anyone's day's brighter."

  "Whose enthusiasm could have you happily sit through hours of stories about one specific rock."

  nvl clear

  "The person who was, sometimes, selfless to a fault."

  "Who wouldn't hesitate to reach out her hand; yet wouldn't allow herself the same vulnerability."

  "Who loved our traditions; yet found no love in them."

  nvl clear
  
  "Flipping the pages of the album we filled together over the years, I can’t help but remember all these facets of her."

  "And though I'll always miss her dearly, I don't feel so alone anymore."

  "Not in this house."
  
  nvl clear

  "In the end, she was wrong about one thing."

  "You didn’t just disappear, Sis."
  
  "All of these memories—all of you—they still live here."
  
  "Within me."

  "And they always will."

  nvl clear

  jump end_credits

label end_credits:
  $ show_quick_menu = False
  scene
  show expression Solid(white)
  with dissolve

  show screen credits_one_column("Made by", [
    ("Q.", None)
  ], title_meta = "(ILLUSTRATION, WRITING, PROGRAMMING)")
  with dissolve
  pause 2.0
  hide screen credits
  with dissolve

  show screen credits_one_column("Background Music", [
    ("Dimitri Kovalchuk", "@ PIXABAY"),
    ("rosko vair", "@ ITCH.IO")
  ], title_meta = "(ASSETS FOR)")
  with dissolve
  pause 4.0
  hide screen credits
  with dissolve

  show screen credits_two_columns("Sound Effects", [
    [
      ("25347980", None),
      ("Universfield", None),
      ("Rickmk2", None)
    ],
    [
      ("ProdMultimediasHQI", None),
      ("FocusBay", None),
      ("sagetyrtle", None)
    ]
  ], title_meta = "(ASSETS FROM PIXABAY FOR)")
  with dissolve
  pause 4.0
  hide screen credits
  with dissolve

  show screen credits_one_column("Sound Effects", [
    ("SamuelGremaud", None),
    ("straget", None),
    ("szczur_banshee", None)
  ], title_meta = "(ASSETS FROM FREESOUND FOR)")
  with dissolve
  pause 4.0
  hide screen credits
  with dissolve

  show screen credits_one_column("Made With", [
    ("Ren'Py", None)
  ])
  with dissolve
  pause 2.0
  hide screen credits
  with dissolve

  show screen credits_one_column("Special Thanks", [
    ("Flickers", None)
  ])
  with dissolve
  pause 2.0
  hide screen credits
  with dissolve

  show screen credits_fin()
  with dissolve
  pause
  hide screen credits_fin
  scene black
  with dissolve

  return

screen credits_one_column(title, entries, title_meta = None):
  tag credits
  vbox:
    style "credits_window"

    if title_meta is not None:
      text title_meta style "credits_title_meta"
    text title style "credits_title"

    null height 50

    vbox:
      style "credits_one_vbox"
      for (name, meta) in entries:
        hbox:
          style "credits_entry"
          text name style "credits_entry_name"
          if meta is not None:
            text meta style "credits_entry_meta"


screen credits_two_columns(title, columns, title_meta = None):
  tag credits
  vbox:
    style "credits_window"

    if title_meta is not None:
      text title_meta style "credits_title_meta"
    text title style "credits_title"

    null height 50

    hbox:
      style "credits_columns"

      for entries in columns:
        vbox:
          style "credits_two_vbox"
          for (name, meta) in entries:
            hbox:
              style "credits_entry"
              text name style "credits_entry_name"
              if meta is not None:
                text meta style "credits_entry_meta"

screen credits_fin():
  tag credits
  vbox:
    style "credits_window"
    text _("Thank you for reading.") style "credits_title"

  text "fin." style "credits_fin"


style credits_window is empty
style credits_title_meta is empty
style credits_title is empty
style credits_columns is empty
style credits_one_vbox is empty
style credits_two_vbox is credits_one_vbox
style credits_entry is empty
style credits_entry_name is text
style credits_entry_meta is text
style credits_fin is text

style credits_window:
  xalign 0.5
  yalign 0.5
  xfill False
  yfill False

style credits_title:
  xalign 0.5
  size 48
  bold True
  color black

style credits_title_meta:
  xalign 0.5
  size 16
  color "#5f5f5f"

style credits_one_vbox:
  spacing 16
  xalign 0.5

style credits_columns:
  spacing 50
  xalign 0.5

style credits_two_vbox:
  xsize 300

style credits_entry:
  spacing 10
  xalign 0.5

style credits_entry_name:
  size 32
  color black

style credits_entry_meta:
  yalign 0.8
  size 16
  color "#5f5f5f"

style credits_fin:
  yalign 1.0
  xalign 1.0
  yoffset -32
  xoffset -32
  size 36
  color "#5f5f5f"


screen content_warning():
  window:
    style "content_warning_window"

    add Solid(white) ysize 1 ypos 206

    vbox:
      style "content_warning_vbox"

      text _("Content Warning") style "content_warning_title"
      text _("This game discusses loss, abuse, anxiety, and trauma.{p} Please take care when playing.") style "content_warning_description"

    hbox:
      style "content_warning_ctc"

      add kate_ok zoom 0.1 yalign 0.5 alt "Press OK to continue"
      text _("Continue") yalign 0.5 color "#ffffff" alt ""

style content_warning_window is empty
style content_warning_vbox is empty
style content_warning_title is empty
style content_warning_description is empty
style content_warning_ctc is empty

style content_warning_window:
  background black
  xfill True
  yfill True

style content_warning_vbox:
  xalign 0.5
  yalign 0.5
  spacing 30

style content_warning_title:
  xalign 0.5
  size 50
  color white

style content_warning_description:
  xalign 0.5
  text_align 0.5
  size 28
  color white

style content_warning_ctc:
  yalign 1.0
  xalign 1.0
  xoffset -15
  yoffset -15
  spacing 10