transform enter_fg:
  ysize 2 xsize 800 xpos -800 ypos 115
  ease 0.5 xpos 0
  ease 0.5 ysize 192 ypos 20

transform animate_ctc:
  yoffset 5
  xoffset 10
  zoom 0.08

  block:
    ease 0.25 yoffset 10
    ease 0.25 yoffset 5
    pause 0.5
    repeat

transform animate_page_ctc:
  yoffset 7
  xoffset 10
  zoom 0.08

  block:
    ease 0.25 xoffset 15
    ease 0.25 xoffset 10
    pause 0.5
    repeat

transform delayed_blink(delay, cycle):
  alpha .5
  pause delay

  block:
    linear .2 alpha 1.0
    pause .2
    linear .2 alpha 0.5
    pause (cycle - .4)
    repeat