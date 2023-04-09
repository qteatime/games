# the sound of rain.

This is a stripped down version of [the sound of rain.](https://qteatime.itch.io/the-sound-of-rain-remake) including only assets created by me. If you want to play the game, I'd recommend playing it from the Itch.io link there.

The code hasn't really been cleaned up, so it might not be the prettiest or easiest thing to follow. There are a few custom changes to the generated Ren'Py Web index.html that likewise do not feature here.


## Building

Ren'Py doesn't have a non-interactive way of building distributions, so the building process is a bit involved:

  - [Download Ren'Py 7.5.3](https://www.renpy.org/);
  - Put this directory on your games folder, or change `Preferences -> Projects directory` to the folder containing this one;
  - Click `Web (Beta)`, then `Build Web Application` in the launcher. Ren'Py will create a `rain-1.0-dists` folder above this one;
  - Move `rain-1.0-dists/rain-1.0-web` to this folder under the name `web`;
  - Run `kart kate.json --output the-sound-of-rain.kart` in this folder.

If all incantations pass without trouble, you should have a Kate cartridge that you can load in the emulator now. Note that this version will have no sounds, and will use the default fonts.


## Licence

Made by Q., code is released under MIT, images the `game/images` folder under [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/), and images under the `game/kate-ui` folder under [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/). Other images are part of the Ren'Py distribution and not distributed under a CC licence..
