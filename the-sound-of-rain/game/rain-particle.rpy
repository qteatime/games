init offset = -2

init python:
  class RainSprite(object):
    def __init__(self, sprite, scale):
      self.sprite = sprite
      self.vx = 4.0
      self.vy = 9.0 + renpy.random.random() * 25.0 * scale
      self.scale = scale

    def update(self, lag):
      self.sprite.x -= self.vx * lag
      self.sprite.y += self.vy * lag

  class RainParticle(object):
    def __init__(self, count = 20, width = 800, height = 480):
      self.manager = SpriteManager(update = self.update)
      self.sprites = []
      self.images = [
        im.FactorScale("gui/rain.png", 0.1),
        im.FactorScale("gui/rain.png", 0.3),
        im.FactorScale("gui/rain.png", 0.5),
        im.FactorScale("gui/rain.png", 0.7),
        im.FactorScale("gui/rain.png", 0.9),
        Image("gui/rain.png")
      ]
      self.width = width
      self.height = height
      self.st = None

      for i in range(count):
        scale = renpy.random.randint(0, len(self.images) - 1)
        vscale = 0.1 + scale / len(self.images)
        sprite = self.manager.create(self.images[scale])
        self.sprites.append(RainSprite(sprite, vscale))

      for i in self.sprites:
        self.randomize(i)

    def displayable(self):
      return self.manager

    def randomize(self, i):
        i.sprite.x = renpy.random.randint(0, self.width + self.width / 2)
        i.sprite.y = -renpy.random.randint(0, self.height * 2)

    def update(self, st):
      if self.st is None:
        self.st = st
      delta = 1.0 + (st - self.st) / 30.0
      for i in self.sprites:
        i.update(delta)
        if i.sprite.x < 0 or i.sprite.y > self.height:
          self.randomize(i)
      return 0
