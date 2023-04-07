init python:
  def maybe_pickup():
    renpy.choice_for_skipping()
    return renpy.call_screen("choice", ChoiceTree(
      "I...",
      up = ChoiceItem("Take it", Return(True)),
    ))

  def maybe_open():
    renpy.choice_for_skipping()
    return renpy.call_screen("choice", ChoiceTree(
      "I...",
      up = ChoiceItem("Open the box", Return(True)),
      left = ChoiceItem("Try something else", Return(False))
    ))

  def reset_state():
    store.box_left = Box("left", "To my left", on_top = umbrella, inside = [crowbar])
    store.box_up = Box("up", "In front of me", on_top = cat_figure, inside = [broken_camera, photo_album])
    store.box_right = Box("right", "To my right", inside = [necklace, journals, bag_of_gems])
    store.inventory = []
    store.hatch_is_open = False
    store.left_attic = False
    store.boxes_inspected = 0

  class Box(object):
    def __init__(self, name, location, on_top = None, inside = [], known = False, is_open = False):
      self.known = known
      self.name = name
      self.open = is_open
      self.location = location
      self.on_top = on_top
      self.inside = [x for x in inside]

    def __eq__(self, that):
      if not isinstance(that, Box):
        return False
      return self.name == That.name and self.known == That.known and self.on_top == That.on_top and self.inside == That.inside

    def __ne__(self, that):
      return not self.__eq__(that)

    def update(self, **props):
      return Box(
        self.name,
        self.location,
        on_top = props.get("on_top", self.on_top),
        inside = props.get("inside", self.inside),
        known = props.get("known", self.known),
        is_open = props.get("open", self.open)
      )

    def top_item(self):
      if self.on_top is not None:
        return self.on_top
      elif self.inside:
        return self.inside[0]
      else:
        return None

    def remove(self, item):
      if self.on_top == item:
        return self.update(on_top = None)
      else:
        return self.update(inside = [x for x in self.inside if x != item])

    def to_search_choice(self):
      return ChoiceItem(
        self.location,
        action = Return("search_box_{}".format(self.name)),
        visible = not self.known
      )

    def to_inspect_choice(self):
      return ChoiceItem(
        self.location,
        action = Return("inspect_box_{}".format(self.name)),
        visible = self.on_top is not None or self.inside
      )


  class Thing(object):
    def __init__(self, name):
      self.name = name

    def __eq__(self, that):
      return isinstance(that, Thing) and self.name == that.name

    def __ne__(self, that):
      return not self.__eq__(that)

define inventory = []
define hatch_is_open = False
define left_attic = False
define boxes_inspected = 0

define necklace = Thing("necklace")
define journals = Thing("journals")
define bag_of_gems = Thing("bag_of_gems")
define cat_figure = Thing("cat_figure")
define broken_camera = Thing("broken_camera")
define photo_album = Thing("photo_album")
define umbrella = Thing("umbrella")
define crowbar = Thing("crowbar")

define box_left = Box("left", "To my left")
define box_up = Box("up", "In front of me")
define box_right = Box("right", "To my right")

init python:
  reset_state()

label search_tutorial:
  "Let's see...{nw}"
  $ renpy.choice_for_skipping()
  $ chosen = renpy.call_screen("choice", ChoiceTree(
      "I...",
      up = ChoiceTree(
        "Search",
        prefix = "I search...",
        left = box_left.to_search_choice(),
        up = box_up.to_search_choice(),
        right = box_right.to_search_choice()
      )
    ))
  call expression chosen
  if box_left.known and box_up.known and box_right.known:
    return
  else:
    jump search_tutorial

label search_simulation:
  $ renpy.choice_for_skipping()
  $ chosen = renpy.call_screen("choice", ChoiceTree(
      "I...",
      up = ChoiceTree(
        "Inspect",
        prefix = "I inspect...",
        left = box_left.to_inspect_choice(),
        up = box_up.to_inspect_choice(),
        right = box_right.to_inspect_choice()
      ),
      left = first_choice(
        ChoiceItem(
          "Leave the attic",
          Return("leave_attic"),
          visible = hatch_is_open
        ),
        ChoiceTree(
          "Force the hatch",
          prefix = "I force it...",
          left = ChoiceItem("With the crowbar", Return("force_with_crowbar"), visible = crowbar in inventory),
          right = ChoiceItem("With the umbrella", Return("force_with_umbrella"), visible = umbrella in inventory),
          visible = crowbar in inventory or umbrella in inventory
        )
      )
    ))
  nvl clear
  call expression chosen
  nvl clear
  if left_attic:
    return
  else:
    "What else now?"
    jump search_simulation

label search_box(box = None):
  if boxes_inspected == 0:
    $ boxes_inspected += 1
    "I feel the space [box.location!l]. My hands hit what feels like a cardboard box."

    "As I tap it in the dark, I feel my throat constrict. I cough, and before my reaction can make matters worse, cover my mouth and nose to avoid upsetting more of the dust around here."

    nvl clear

    "I will need to be more careful with how I move, the place really shows its age."
    return
  elif boxes_inspected == 1:
    $ boxes_inspected += 1
    "I feel the space [box.location!l], more careful not to raise any of the dust this time. My hands hit another cardboard box."
    return
  elif boxes_inspected == 2:
    "I feel the space [box.location!l], with the same care as before. It seems that there's another box in that direction."
    return

label search_box_right:
  $ box_right = box_right.update(known = True)
  call search_box(box_right)
  nvl clear
  return

label search_box_up:
  $ box_up = box_up.update(known = True)
  call search_box(box_up)
  "On top of it lays something colder. Perhaps made out of wood?"
  nvl clear
  return

label search_box_left:
  $ box_left = box_left.update(known = True)
  call search_box(box_left)
  "On top of it there's something cold. Some kind of metal...?"
  nvl clear
  return

label inspect_box_right:
  "If I remember correctly, there was nothing on top of this box."

  "I lightly tap around and over it...{w=1.0} Nothing.{w=0.5} But the box is closed."

  call open_box("box_right")
  return

label inspect_box_up:
  "I believe there was something made of wood on top of this box."
  
  "Or, well, at least it felt like wood.{w=1.0} I take my hand to the box again and carefully feel around."

  call inspect_cat_figure
  call open_box("box_up")
  return

label inspect_box_left:
  "I lightly tap the box to my left, my hands soon hit a small rod of metal."
  
  "Something soft is wrapped around it...{w=1.0} This might be the old umbrella Aunt Nada used when Sis and I were kids."

  call inspect_umbrella
  call open_box("box_left")
  return

label open_box(box_name = None):
  $ box = store.__getattribute__(box_name)

  if box.open:
    call inspect_box(box)
    return
  else:
    if maybe_open():
      nvl clear
      $ store.__setattr__(box_name, box.update(open = True))
      "I take out my pocket knife and carefully trace over where the two flaps meet. The box opens easily."
      call inspect_box_loop(box_name)
      return
    else:
      nvl clear
      return

label inspect_box_loop(box_name = None):
  $ box = store.__getattribute__(box_name)
  while box.inside:
    call expression "inspect_{}".format(box.top_item().name)
    nvl clear
    "There might be more things here..."
    $ renpy.choice_for_skipping()
    call screen choice(ChoiceTree(
      "I...",
      up = ChoiceItem("Reach deeper", Return(None))
    ))
    nvl clear
    $ box = store.__getattribute__(box_name)

  "Looks like that was all for this box."
  nvl clear
  return

label inspect_necklace:
  "Sticking my hand inside, the first thing I notice is...{w=1.0} cold.{w=0.5} A rock...?{w=0.5} Something metallic seems to be attached to it."

  nvl clear

  "I pick it up and run my fingers through it. The bumps in the metallic appendage are easily recognisable.{w=0.5} A small chain.{w=0.5} It connects to the rock with a metallic arc, perhaps gold, which in turn extends to enclose the rock entirely."

  "Or should I say gem?"
  
  "It has been carefully polished.{w=0.5} Rather than perfectly smooth, there are several flat facets making out its droplet-like shape.{w=0.5} The edges are pronounced, but not in a way that would hurt you."

  nvl clear

  "As I run my fingers through it I can almost hear Sis’ voice behind me."
  
  "“What a loathsome green!”"

  "And I can picture Aunt Nada standing there, feeling astonished and rejected, as she held her gift in her open hands."
  
  "Perhaps because Aunt Nada looked like she was about to cry, Sis decided to accept the necklace anyway."

  nvl clear

  "I don’t think Aunt Nada would hold any ill bearings towards Sis.{w=0.5} She would have first blamed herself for making a mistake with the gift."
  
  "But it was a time of change for all of us."

  "Sis, who loved gems more than anything since having her Role divined as a gemologist."
  
  "Aunt Nada and I, who had been exiled for failing to live up to ours."

  nvl clear

  "That was the first time we had met in years.{w=0.5} Both Aunt Nada and I wanted nothing more than to make Sis happy;{w=0.5} to see that bright smile she always had when working with stones."

  "I think, some other time, the birthstone pendant would have brought her so much joy.{w=1.0} But our mistiming caused her grief.{w=1.0} Guilt."

  nvl clear

  "We happened to meet later in another occasion.{w=0.5} She was wearing the necklace then, but her eyes had grown distant."
  
  "When I called out to her she greeted me with a smile, then gaily joined her hands with mine."

  "But her smile didn’t reach her eyes."
  
  "There, in the city, she looked like a shadow of the Sis I once knew.{w=0.5} And she made much effort to keep me from prying any further."

  nvl clear

  "Was her face ever that thin?{w=1.0} Her bones that pronounced?{w=1.0} Her skin that pale?"
  
  "I wanted to tell her that I was there for her,{w=0.5} that she could rely on me...{w=1.0} The words never left my throat."

  if maybe_pickup():
    $ box_right = box_right.remove(necklace)
    $ inventory += [necklace]

    nvl clear
    
    "After that, Sis and I exchanged letters occasionally, with mostly me writing to her."
    
    "She mentioned how writing had become harder for her in the later years, and I didn’t want to impose."

    "But every little letter I received from her made me happy.{w=0.5} Whether it was just describing her daily life, or gushing about some of her newfound obsessions."

    nvl clear

    "She sent a painting of the birthstone necklace once, surrounded by pressed flowers."
    
    "There were no notes accompanying it, and I never had the courage to ask, but I always wondered if that was her way of saying she kept us close still."

    "If it helps me to remember her, I wish to keep this necklace by my side, too."

    nvl clear
    return
  else:
    $ box_right = box_right.remove(necklace)
    return

label inspect_journals:
  "I stick my hand in the box again, this time I’m greeted by the familiar texture of paper."
  
  "Running my fingers through them, it feels like many pieces, bound together by strings."

  "Are these…{w=1.0} Sis’ research journals?{w=0.5} So this is where Aunt Nada stashed them away."

  nvl clear

  "Back when Sis was still studying the different planes, she’d fill these at a frightening pace."
  
  "I even asked to borrow one of them once, but, as a child, much of it just flew right over my head."

  "Ligia is a region shrouded in so many traditions and folktales surrounding death. The idea that rites of passing helped the ones we’ve lost find their way to the next plane always fascinated her."

  nvl clear

  "How the soul was gently carried by the wind."
  
  "How gemstones acted as a guide, keeping souls from being lost to the whims of Nature."
  
  "How witches dealt with stray souls."

  "She earnestly dove into all those questions. And then..."

  "“Ghosts aren’t real. After we die there is… nothing.”"

  nvl clear

  "That was the conclusion of her research."
  
  "It was the last thing she wrote before she stuck them in her chiffonier’s drawer.{w=1.0} Locked it away."

  "And it was the first time she spoke of death with me. An uncharacteristic gloom in her eyes."

  if maybe_pickup():
    nvl clear
    $ box_right = box_right.remove(journals)
    $ inventory += [journals]

    "I wish I could extend my hand towards her now.{w=1.0} Wrap my arms around her."

    "I wish I could’ve done so many things.{w=0.5} To have been beside her for longer."

    "But came dawn, Mother ordered me away from the House.{w=0.5} Sis’ days grew harsher."
    
    "When she couldn’t perform her Role any longer, I’m told, Mother sent her to the city."

    nvl clear

    "“They said her health was in decline; that she was to live with an herbologist Mother was acquainted with,” Aunt Nada said."

    "When we later visited her there, Sis wouldn’t say anything about her research.{w=0.5} But those same words would always leave her lips."

    "“Ghosts aren’t real.”"

    "As if a curse,{w=0.5} meant to haunt us both."

    nvl clear
    return
  else:
    $ box_right = box_right.remove(journals)
    return


label inspect_bag_of_gems:
  "I continue fumbling through the contents of the box when my hands catch something with a distinct leathery feel.{w=1.0} A bag of sorts, carrying what feels like many small round-ish items."

  "Perhaps...{w=1.0} going from the other items Aunt Nada placed here, this must be Sis’ old bag of gems."
  
  "She always had it on her while doing fieldwork around the forest."
  
  nvl clear

  "Though she would invite me to join her outings, I had my own problems to deal with back then."
  
  "I’d tell her “maybe some other time.”"
  
  "That other time never came.{w=1.0} I never saw Sis perform any magic."

  nvl clear

  "But I vividly remember how her eyes sparkled as she told me of her discoveries."
  
  "One day she rushed towards me and opened her hands.{w=0.5} There was a joyful look on her face as she showed me a cluster of tiny berries."

  if maybe_pickup():
    $ box_right = box_right.remove(bag_of_gems)
    $ inventory += [bag_of_gems]

    nvl clear
    
    "I reached out to them almost instinctively.{w=1.0} Then my hands stopped mid-air."
    
    "“Are these...{w=1.0} rocks?”"

    "She laughed, “Yeah, yeah. Aren’t they, like, super pretty?”"

    nvl clear

    "They truly were."
    
    "Perhaps dozens of little, round, blue berry-coloured rocks.{w=0.5} Clustered together just like the real food."
    
    "Sis excitedly told me all about their properties and how they were formed, doing her best to match my rock-vocabulary."

    "But not much registered."
    
    "What I remember from that time is her excitement, and how happy I was that she’d choose to share it."

    nvl clear
    return
  else:
    $ box_right = box_right.remove(bag_of_gems)
    return


label inspect_cat_figure:
  "As I touch the thing on the top of the box I notice more of its shape and its imperfections. This might be the cat figurine that Aunt Nada carved when she was younger."

  nvl clear

  "It’s one of the first items she’s carved, too.{w=0.5} The shape is very roughly defined."
  
  "When she showed it to Sis and I, we both exchanged glances and asked, “Is that a person?”"

  nvl clear

  "She looked a bit crestfallen after that."
  
  "We apologised."
  
  "Still, she could never part with it.{w=1.0} To her, that was an important step in her artistic journey."

  if maybe_pickup():
    $ box_up = box_up.remove(cat_figure)
    $ inventory += [cat_figure]
    
    nvl clear
    "Aunt Nada never really tried to become an expert at carving, but she enjoyed it a great deal, and kept the occasional pieces she made after this one."

    "Once she brought me a small bust figure." 
    
    "I was pleasantly surprised with how much she had improved.{w=0.5} Not that she had mastered the art, but her pieces conveyed better what she wanted to say."

    "That was how I looked like in her eyes."

    nvl clear

    "Aunt Nada was uncharacteristically hesitant then."
    
    "“I hope you find it agreeable, my dear. If I am to be honest, this was not the first one, and I wavered a bit in whether I should present it to you.”"
    
    "She brightened up when I accepted her gift.{w=1.0} When I wrapped my arms around her, in a tight hug, she felt warmer than usual."

    "I still have her figure sitting on top of the chiffonier in my room.{w=1.0} Looking at it reminds me of the long journey we both took to find ourselves."

    nvl clear
    return
  else:
    $ box_front = box_front.remove(cat_figure)
    return

label inspect_broken_camera:
  "Sticking my hand inside, the first thing I notice is...{w=1.0} hard.{w=0.5} Box-shaped."

  "As I tap around more its distinct features are easily recognisable."
  
  "The little telescope viewfinder sits on top, with the aperture switcher beside it, and the shutter lever a little further, sticking from the side of the box."

  nvl clear

  "The old folding camera was the first one I had, gifted to me by the very own Aunt Nada when I was a kid."
  
  "It was the last push I needed to accept myself, rather than who Mother wished for me to be."

  nvl clear

  "Eventually I used it so much that it broke."
  
  "I never managed to get it fixed.{w=1.0} But it held too many feelings for me to simply throw it away."
  
  "It’s been sitting here ever since."

  if maybe_pickup():
    $ box_up = box_up.remove(broken_camera)
    $ inventory += [broken_camera]

    nvl clear

    "It’s strange to think about those times nowadays."
    
    "I was trying so hard to fit my Role as a herbologist, like Mother had divined."
    
    "And I was failing at every step of it."

    nvl clear

    "I liked plants well enough, and I applied myself to my utmost.{w=1.0} I gave it everything I could."
    
    "But Mother was never satisfied with it."
    
    "Soon any enjoyment I took from the practice turned into anxiety."
    
    "Anxiety turned into panic."
    
    "I went from learning the craft to wondering what was broken in me."

    nvl clear

    "Sis was the first one to notice."
    
    "She offered to talk to Mother on my behalf.{w=0.5} I declined."
    
    "I could never risk having her go through the same things I did."
    
    nvl clear

    "In the end, it was Aunt Nada who saved me.{w=0.5} The one I let save me."

    "Aunt Nada didn’t do anything special."
    
    "She was just...{w=1.0} there."
    
    "She asked what I wanted to do.{w=0.5} She gave me options.{w=0.5} Allowed me to fail."

    "It was such a simple thing that I wonder if I’d have loved herbology more if Mother hadn’t{w=0.5}.{w=0.5}.{w=0.5}."

    nvl clear
    return
  else:
    $ box_up = box_up.remove(broken_camera)
    return

label inspect_photo_album:
  $ box_up = box_up.remove(photo_album)
  $ inventory += [photo_album]

  "I feel the contents of the box again, trying to see if anything interesting comes up."
  
  "As I do I feel embossed letters engraved on thick paper.{w=0.5} This is what I came here for today."

  "Not hesitating for a second, I take the book from the box and hold it close to my chest, letting the memories float back."

  nvl clear

  "Sis and I filled this little photo album when we were kids."
  
  "To be fair, they are mostly photos I’ve taken of Sis."
  
  "She would always ask me to snap a picture, too.{w=0.5} Her enthusiasm made it hard to refuse."

  "Not like I wanted to refuse, in any case.{w=0.5} She was such a lively subject that taking photos of her brought me immense joy."

  nvl clear

  "I remember the first time I taught Sis how to use the camera."
  
  "Though an older model, it didn’t take much for her to learn.{w=1.0} The telescope viewfinder was certainly easier to get used to than the brilliant ones."

  nvl clear

  "“May... I take your picture?”"

  "She asked me hesitantly back then, and was visibly sad when I rejected."
  
  "I was so worried about being seen as a failed herbologist that I couldn't think of anything else."
  
  "Now I regret never getting to see what I looked like through Sis’ eyes."

  nvl clear
  return

label inspect_umbrella:
  nvl clear

  "It still seems to be in very good shape."
  
  "I don’t notice any holes in it.{w=0.5} And I imagine it’s quite usable."
  
  "Like anything else Aunt Nada owned, she kept it in good care even after she stopped using it."

  if maybe_pickup():
    $ box_left = box_left.remove(umbrella)
    $ inventory += [umbrella]

    nvl clear

    "I think Aunt Nada and I both walked under this umbrella a long, long time ago."

    "It was during that unstable time where the weather can’t decide if it wants to be winter or spring,{w=0.5} alternating between rain and snow."

    "A season that some perceive, but yet have no name for."

    "A season which is there, but isn’t."

    nvl clear

    "After a discussion with Mother, I was out in the forest, sitting alone under this same rain."

    "Crying."

    "When Aunt Nada found me she had this umbrella with her."
    
    "I had already rehearsed how to tell off whoever came to find me; was not going home that day."

    nvl clear

    "But she caught me off-guard.{w=1.0} Sat down with me, holding the umbrella over us."

    "My mouth closed.{w=0.5} My face nestled within my legs, sobs muffled by my skirt."

    "“You don’t have to be an herbologist, if you don’t want to.”"
    
    "Of all the one-sided conversations Aunt Nada had with me that day, that’s the line that stuck with me."

    nvl clear

    "She didn’t say I had to be something else."
    
    "She didn’t even suggest anything else."

    "When we arrived home, later, we both got an earful from Mother."
    
    "Was there concern in her voice?{w=1.0} Worry on her face?{w=1.0} Or was it my mind filling the gaps with what I wished to see there?"
    
    nvl clear
    return
  else:
    $ box_left = box_left.remove(umbrella)
    return

label inspect_crowbar:
  $ box_left = box_left.remove(crowbar)
  $ inventory += [crowbar]

  "As I reach deeper into the box my hand touches something cold.{w=0.5} Metallic."
  
  "Feeling around a bit more, I'm pretty sure it's a crowbar.{w=1.0} A quite sturdy one at that."

  "I don’t remember anyone ever using it, but it should come in handy with the hatch."

  return

label force_with_crowbar:
  $ hatch_is_open = True
  "The hatch opens easily. I make sure to leave it open for now."

  nvl clear
  return

label force_with_umbrella:
  $ hatch_is_open = True
  "Using the umbrella as a lever works better than I expected."
  
  "The hatch is open now.{w=0.5} But, as I run my fingers through the umbrella's bent handle, I can’t help but feel sad for it."

  "Aunt Nada had always taken such great care of everything.{w=1.0} As if they were special to her."
  
  "And yet, here am I, doing the only thing I’m good at.{w=1.0} Destroying things."

  nvl clear

  "I’ll apologise once she’s back from her travels."

  nvl clear
  return

label leave_attic:
  if photo_album in inventory:
    $ left_attic = True
    return
  else:
    "There’s still something I came up here for. It should be around here, somewhere. I should search a bit more."
    nvl clear
    return