# Atari 7800 Samples

The following are examples of Atari 7800 samples:

- Demo 0: example of displaying 210 sprites (press the button to move them)
- Demo 1: bi-directional scrolling
- Demo 2: parallax scrolling
- Demo 3: use of interrupts to display all 256 colors (press the button to show)

These sample were build using the [cc7800](https://github.com/steux/cc7800) C SDK. However, instead of using the sprite capabilities available in this SDK, the samples are managing the 7800 Display List List (DLL) directly.

To understand how the DLL works in detail, it is recommended to look at the [7800 Software Guide](https://7800.8bitdev.org/index.php/7800_Software_Guide#Display) Display section.

# DLL Parse

The `parse_dll.py` is a Python script that can parse the DLL from a 7800 game memory dump and generates a description of the DLL, as well as generates an image for each sprite. It is NOT a ready-to-go product as you need to enter manually many details such as the DLL address for any new game. So you need to add a section for the desired game in the code (look for example for `elif game_name == "alien_brigade":`)

To gather that data:

- Run a7800 a7800 -debug -cart [name of the .a78]
- Stop whenever desired
- Type `save <gamename>_dump,0,100000` to generate the memory dump (it needs to end up `_dump`)
- Go to Debug / Memory Window
- In the menu on that window, you can go to:
  - `Atari MARIA/:maria/0/m_dpp`: this is the address of the DLL and the only required value to capture. Add `DLL=<address>` in the script
  - `Atari MARIA/:maria/0/m_charbase`: this is the address of the tileset. Add `CHARBASE=<address>` in the script
  - `Atari MARIA/:maria/0/m_maria_palette`: this is the color palette. Add `colors=[...]` in the script

For some games, the system properties are modified mid-screen (colors, tileset, etc.). So it's useful to capture those values at different times (Run / Run into next Interrupt on current CPU) and capture the values. Create a `dli_table` instead (see the `dli_table_bentley` example)

```
> python parse_dll.py bentley_dump
DLL = 8448
GRAPHIC_MODE = 320
CHARBASE = 49152
colors = [[66, 68, 70], [19, 24, 45], [196, 199, 28], [97, 15, 0], [2, 8, 10], [2, 8, 10], [0, 0, 0], [0, 0, 0]]
[0F 27 AB] height=16 (y=  0), HoleyDMA=off, DL=0x27AB
[07 27 AB] height= 8 (y= 16), HoleyDMA=off, DL=0x27AB
[C6 27 70] height= 7 (y= 24), HoleyDMA=16, DL=0x2770 DLI
                                        [2770 - D8 60 27 66 00] X=  0, GFX=0x27D8, width=26, palette=3, mode=indirect, graph mode=320A
                                        [2775 - F2 60 27 1D 68] X=104, GFX=0x27F2, width= 3, palette=0, mode=indirect, graph mode=320A
                                        [277A - F5 60 27 3D 74] X=116, GFX=0x27F5, width= 3, palette=1, mode=indirect, graph mode=320A
                                        [277F - F8 60 27 58 80] X=128, GFX=0x27F8, width= 8, palette=2, mode=indirect, graph mode=320A
[07 27 90] height= 8 (y= 31), HoleyDMA=off, DL=0x2790
                                        [2790 - B0 60 27 60 00] X=  0, GFX=0x27B0, width=32, palette=3, mode=indirect, graph mode=320A
                                        [2795 - D0 60 27 78 80] X=128, GFX=0x27D0, width= 8, palette=3, mode=indirect, graph mode=320A
[01 27 AB] height= 2 (y= 39), HoleyDMA=off, DL=0x27AB
[CF 23 00] height=16 (y= 41), HoleyDMA=16, DL=0x2300 DLI
GRAPHIC_MODE = 160
CHARBASE = 32768
colors = [[66, 68, 70], [19, 24, 45], [196, 199, 28], [97, 15, 0], [215, 216, 217], [215, 216, 217], [0, 0, 0], [0, 0, 0]]
                                        [2300 - 1E 60 18 8B 00] X=  0, GFX=0x181E, width=21, palette=4, mode=indirect, graph mode=160A
                                        [2305 - 00 C0 50 1F C8] X=200, GFX=0x5000, width= 1, palette=0, mode=direct, graph mode=160B
                                        [230A - 00 1C 50 C8   ] X=200, GFX=0x5000, width= 4, palette=0, mode=direct, graph mode=160A
                                        [230E - 00 1E 50 C8   ] X=200, GFX=0x5000, width= 2, palette=0, mode=direct, graph mode=160A
                                        [2312 - 00 1E 50 C8   ] X=200, GFX=0x5000, width= 2, palette=0, mode=direct, graph mode=160A
                                        [2316 - C0 1C 40 C8   ] X=200, GFX=0x40C0, width= 4, palette=0, mode=direct, graph mode=160A
                                        [231A - 00 1C 50 C8   ] X=200, GFX=0x5000, width= 4, palette=0, mode=direct, graph mode=160A
                                        [231E - 00 1C 50 C8   ] X=200, GFX=0x5000, width= 4, palette=0, mode=direct, graph mode=160A
                                        [2322 - 00 1C 50 C8   ] X=200, GFX=0x5000, width= 4, palette=0, mode=direct, graph mode=160A
                                        [2326 - 00 1C 50 C8   ] X=200, GFX=0x5000, width= 4, palette=0, mode=direct, graph mode=160A
[CF 23 35] height=16 (y= 57), HoleyDMA=16, DL=0x2335 DLI
                                        [2335 - DE 60 18 AB 00] X=  0, GFX=0x18DE, width=21, palette=5, mode=indirect, graph mode=160A
                                        [233A - 00 C0 50 1F C8] X=200, GFX=0x5000, width= 1, palette=0, mode=direct, graph mode=160B
                                        [233F - 00 1C 50 C8   ] X=200, GFX=0x5000, width= 4, palette=0, mode=direct, graph mode=160A
                                        [2343 - 00 1E 50 C8   ] X=200, GFX=0x5000, width= 2, palette=0, mode=direct, graph mode=160A
                                        [2347 - 00 1E 50 C8   ] X=200, GFX=0x5000, width= 2, palette=0, mode=direct, graph mode=160A
                                        [234B - C0 1C 40 C8   ] X=200, GFX=0x40C0, width= 4, palette=0, mode=direct, graph mode=160A
                                        [234F - 00 1C 50 C8   ] X=200, GFX=0x5000, width= 4, palette=0, mode=direct, graph mode=160A
                                        [2353 - 00 1C 50 C8   ] X=200, GFX=0x5000, width= 4, palette=0, mode=direct, graph mode=160A
                                        [2357 - 00 1C 50 C8   ] X=200, GFX=0x5000, width= 4, palette=0, mode=direct, graph mode=160A
                                        [235B - 00 1C 50 C8   ] X=200, GFX=0x5000, width= 4, palette=0, mode=direct, graph mode=160A
...
```
