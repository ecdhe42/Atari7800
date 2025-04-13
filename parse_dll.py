import os
import sys
from PIL import Image

if len(sys.argv) < 2:
    print("Syntax:",sys.argv[0],"<dump file>")
    quit()

filename = sys.argv[1]

with open(filename, "rb") as f:
    m = f.read()

game_name = filename.replace("_dump", "")

img = Image.new("RGB", (320,240), (0,0,0))
img_id = 0

colors = [
    [0x37, 0x1c, 0x0f],
    [0x84, 0x34, 0xac],
    [0x04, 0x08, 0x0c],
    [0xd0, 0x87, 0xd1],
    [0x3c, 0x39, 0x36],
    [0x24, 0x22, 0x0e],
    [0x0a, 0x04, 0x02],
    [0xc9, 0xc6, 0x0c]
#    [0x12, 0x14, 0x16],
#    [0x84, 0x87, 0xac],
#    [0x34, 0x38, 0x3c],
#    [0x04, 0x08, 0x0c]
]


colors_7800 = [(0, 0, 0), (13, 13, 13), (40, 40, 40), (62, 62, 62), (82, 82, 82), (101, 101, 101), (119, 119, 119), (136, 136, 136), (152, 152, 152), (168, 168, 168), (183, 183, 183), (198, 198, 198), (213, 213, 213), (227, 227, 227), (241, 241, 241), (255, 255, 255), (89, 38, 0), (105, 58, 0), (121, 77, 0), (137, 94, 0), (151, 110, 0), (166, 126, 0), (180, 141, 0), (193, 156, 0), (207, 170, 0), (220, 184, 0), (233, 197, 0), (245, 211, 0), (255, 224, 0), (255, 236, 0), (255, 249, 30), (255, 255, 52), (135, 0, 0), (150, 30, 0), (164, 51, 0), (178, 70, 0), (192, 88, 0), (205, 105, 0), (218, 121, 0), (231, 136, 0), (244, 151, 0), (255, 165, 0), (255, 179, 0), (255, 193, 25), (255, 206, 47), (255, 219, 67), (255, 232, 85), (255, 245, 101), (159, 0, 0), (173, 0, 0), (187, 25, 0), (200, 48, 0), (213, 67, 0), (226, 85, 0), (239, 102, 28), (252, 118, 50), (255, 133, 69), (255, 148, 87), (255, 162, 104), (255, 177, 120), (255, 190, 135), (255, 204, 150), (255, 217, 164), (255, 230, 178), (158, 0, 37), (172, 0, 58), (186, 3, 76), (199, 32, 93), (213, 53, 110), (226, 72, 125), (238, 89, 141), (251, 106, 155), (255, 122, 169), (255, 137, 183), (255, 152, 197), (255, 166, 210), (255, 180, 223), (255, 194, 236), (255, 207, 249), (255, 220, 255), (133, 0, 145), (148, 0, 159), (163, 0, 173), (177, 28, 187), (190, 50, 201), (204, 69, 214), (217, 87, 227), (230, 103, 240), (243, 119, 252), (255, 135, 255), (255, 149, 255), (255, 164, 255), (255, 178, 255), (255, 192, 255), (255, 205, 255), (255, 218, 255), (86, 0, 212), (103, 0, 225), (119, 13, 238), (134, 38, 250), (149, 59, 255), (163, 77, 255), (177, 94, 255), (191, 111, 255), (204, 126, 255), (218, 141, 255), (230, 156, 255), (243, 170, 255), (255, 184, 255), (255, 198, 255), (255, 211, 255), (255, 224, 255), (10, 0, 242), (36, 13, 255), (57, 38, 255), (75, 58, 255), (93, 77, 255), (109, 94, 255), (125, 110, 255), (140, 126, 255), (155, 141, 255), (169, 156, 255), (183, 170, 255), (196, 184, 255), (210, 197, 255), (223, 211, 255), (235, 224, 255), (248, 237, 255), (0, 21, 235), (0, 44, 247), (0, 64, 255), (0, 82, 255), (24, 99, 255), (47, 115, 255), (66, 130, 255), (84, 145, 255), (101, 160, 255), (117, 174, 255), (133, 188, 255), (148, 201, 255), (162, 214, 255), (176, 227, 255), (190, 240, 255), (203, 253, 255), (0, 51, 189), (0, 70, 203), (0, 88, 216), (0, 104, 229), (0, 120, 242), (0, 135, 254), (6, 150, 255), (33, 165, 255), (54, 179, 255), (73, 192, 255), (91, 206, 255), (107, 219, 255), (123, 232, 255), (138, 244, 255), (153, 255, 255), (167, 255, 255), (0, 72, 108), (0, 89, 124), (0, 106, 139), (0, 122, 153), (0, 137, 168), (0, 151, 182), (0, 166, 195), (0, 180, 209), (28, 193, 222), (50, 207, 234), (69, 220, 247), (87, 233, 255), (104, 245, 255), (120, 255, 255), (135, 255, 255), (150, 255, 255), (0, 82, 0), (0, 99, 0), (0, 115, 22), (0, 131, 45), (0, 146, 65), (0, 160, 83), (0, 174, 100), (14, 188, 116), (39, 202, 131), (59, 215, 146), (78, 228, 161), (95, 241, 175), (111, 253, 189), (127, 255, 202), (142, 255, 215), (157, 255, 228), (0, 82, 0), (0, 99, 0), (0, 115, 0), (0, 131, 0), (0, 146, 0), (16, 160, 0), (40, 174, 0), (60, 188, 0), (79, 202, 21), (96, 215, 44), (112, 228, 64), (128, 241, 82), (143, 253, 99), (157, 255, 115), (171, 255, 131), (185, 255, 146), (0, 72, 0), (0, 89, 0), (21, 106, 0), (44, 122, 0), (64, 137, 0), (82, 152, 0), (99, 166, 0), (115, 180, 0), (130, 194, 0), (145, 207, 0), (160, 220, 0), (174, 233, 0), (188, 246, 13), (201, 255, 38), (214, 255, 58), (227, 255, 77), (57, 51, 0), (76, 70, 0), (93, 88, 0), (109, 105, 0), (125, 120, 0), (140, 136, 0), (155, 151, 0), (169, 165, 0), (183, 179, 0), (197, 193, 0), (210, 206, 0), (223, 219, 0), (236, 232, 0), (248, 245, 0), (255, 255, 23), (255, 255, 45), (115, 21, 0), (130, 44, 0), (145, 64, 0), (160, 82, 0), (174, 99, 0), (188, 115, 0), (201, 131, 0), (214, 146, 0), (227, 160, 0), (240, 174, 0), (253, 188, 0), (255, 202, 0), (255, 215, 2), (255, 228, 31), (255, 240, 53), (255, 253, 72)]

# R-Type
colors_rtype = [
    [0x37, 0x1c, 0x0f],
    [0x84, 0x34, 0xac],
    [0x04, 0x08, 0x0c],
    [0xd0, 0x87, 0xd1],
    [0x3c, 0x39, 0x36],
    [0x24, 0x22, 0x0e],
    [0x0a, 0x04, 0x02],
    [0xc9, 0xc6, 0x0c]
#    [0x12, 0x14, 0x16],
#    [0x84, 0x87, 0xac],
#    [0x34, 0x38, 0x3c],
#    [0x04, 0x08, 0x0c]
]

colors_bentley1 = [
    [0x42, 0x44, 0x46],
    [0x13, 0x18, 0x2d],
    [0xc4, 0xc7, 0x1c],
    [0x61, 0x0f, 0x00],
    [0x02, 0x08, 0x0a],
    [0x02, 0x08, 0x0a],
    [0,0,0],
    [0,0,0]
]

colors_bentley2 = [
    [0x42, 0x44, 0x46],
    [0x13, 0x18, 0x2d],
    [0xc4, 0xc7, 0x1c],
    [0x61, 0x0f, 0x00],
    [0xda, 0xd8, 0x24],
    [0xda, 0xd8, 0x24],
    [0,0,0],
    [0,0,0]
]

colors_bentley3 = [
    [0x42, 0x44, 0x46],
    [0x13, 0x18, 0x2d],
    [0xc4, 0xc7, 0x1c],
    [0x61, 0x0f, 0x00],
    [0x02, 0x04, 0x06],
    [0xda, 0xd8, 0x24],
    [0,0,0],
    [0,0,0]
]

colors_TAN = [
    [(0x00, 0x00, 0x00), (0xcc, 0x34, 0x80), (0x66, 0x66, 0x66), (0xff, 0x00, 0x00)],
    [None, (0x37, 0x30, 0x4f), (0x85, 0xc9, 0xea), (0xff, 0xff, 0xff)],
    [None, (0x37, 0x30, 0x4f), (0x85, 0xc9, 0xea), (0xff, 0xff, 0xff)],
    [None, (0x37, 0x30, 0x4f), (0x85, 0xc9, 0xea), (0xff, 0xff, 0xff)],
    [None, (0x37, 0x30, 0x4f), (0x85, 0xc9, 0xea), (0xff, 0xff, 0xff)],
    [None, (0x37, 0x30, 0x4f), (0x85, 0xc9, 0xea), (0xff, 0xff, 0xff)],
    [None, (0x37, 0x30, 0x4f), (0x85, 0xc9, 0xea), (0xff, 0xff, 0xff)],
    [None, (0xff, 0xff, 0xff), (0, 0, 0), (0xf8, 0xaa, 0x71)]
]

colors_rtype1 = [
    [0x37, 0x1c, 0x0f],
    [0x84, 0x34, 0xac],
    [0x04, 0x08, 0x0c],
    [0xd0, 0x87, 0xd1],
    [0x12, 0x14, 0x16],
    [0x84, 0x87, 0xac],
    [0x34, 0x38, 0x3c],
    [0x04, 0x08, 0x0c]
]

colors_rtype2 =[
    [0x37, 0x1c, 0x0f],
    [0x84, 0x34, 0xac],
    [0x04, 0x08, 0x0c],
    [0xd0, 0x87, 0xd1],
    [0x3c, 0x39, 0x36],
    [0x24, 0x22, 0x0e],
    [0x0a, 0x04, 0x02],
    [0xc9, 0xc6, 0x0c]
]

dli_table_bentley = [
    {
        "DLL": 0x2100,
        "GRAPHIC_MODE": "320",
        "CHARBASE": 0xC000,
        "colors": [
            [0x42, 0x44, 0x46],
            [0x13, 0x18, 0x2d],
            [0xc4, 0xc7, 0x1c],
            [0x61, 0x0f, 0x00],
            [0x02, 0x08, 0x0a],
            [0x02, 0x08, 0x0a],
            [0,0,0],
            [0,0,0]
        ]
    },
    {},
    {
        "GRAPHIC_MODE": "160",
        "CHARBASE": 0x8000,
        "colors": [
            [0x42, 0x44, 0x46],
            [0x13, 0x18, 0x2d],
            [0xc4, 0xc7, 0x1c],
            [0x61, 0x0f, 0x00],
            [0xd7, 0xd8, 0xd9],
            [0xd7, 0xd8, 0xd9],
            [0,0,0],
            [0,0,0]
        ]
    },
    {},
    {
        "colors": [
            [0x42, 0x44, 0x46],
            [0x13, 0x18, 0x2d],
            [0xc4, 0xc7, 0x1c],
            [0x61, 0x0f, 0x00],
            [0xd7, 0x02, 0xf5],
            [0xd7, 0x02, 0xf5],
            [0,0,0],
            [0,0,0]
        ]
    },
    {},
    {},
    {},
    {},
    {},
    {
        "colors": [
            [0x42, 0x44, 0x46],
            [0x13, 0x18, 0x2d],
            [0xc4, 0xc7, 0x1c],
            [0x61, 0x0f, 0x00],
            [0xd2, 0x02, 0xf5],
            [0xd2, 0x02, 0xf5],
            [0,0,0],
            [0,0,0]
        ]
    },
    {
        "colors": [
            [0x42, 0x44, 0x46],
            [0x13, 0x18, 0x2d],
            [0xc4, 0xc7, 0x1c],
            [0x61, 0x0f, 0x00],
            [0xda, 0xd8, 0x24],
            [0xda, 0xd8, 0x24],
            [0,0,0],
            [0,0,0]
        ]
    },
]

dli_table_rtype1 = [
    {
        "DLL": 0x24a0,
        "GRAPHIC_MODE": "160",
        "CHARBASE": 0x8000,
        "colors": colors_rtype1
    },
    {
        "GRAPHIC_MODE": "320",
        "CHARBASE": 0xB000
    }
]

dli_table_rtype2 = [
    {
        "DLL": 0x24a0,
        "GRAPHIC_MODE": "160",
        "CHARBASE": 0x8000,
        "colors": colors_rtype1
    },
    {
        "colors": colors_rtype2
    },
    {
        "colors": colors_rtype1
    },
    {
        "GRAPHIC_MODE": "320"
    }
]

dli_table_fatalrun = [
    {
        "DLL": 0x1F33,
        "CHARBASE": 0x4000,
        "BACKGROUND": 0x73,
        "colors": [
        [0x03, 0x03, 0x08],
        [0x09, 0x04, 0x33],
        [0x0A, 0x08, 0x04],
        [0xF2, 0xE2, 0xD2],
        [0x00, 0x00, 0x00],
        [0x00, 0x73, 0x76],
        [0x0a, 0x0a, 0x0a],
        [0x00, 0x17, 0x1a]
#        [0x83, 0x86, 0x8a],
#        [0xc3, 0xc6, 0xca],
#        [0x13, 0x16, 0x1a],
#        [0x43, 0x46, 0x4a],
#        [0x03, 0x06, 0x0a],
#        [0x00, 0x00, 0x00],
#        [0x0a, 0x05, 0x00],
#        [0x03, 0x06, 0x00]
        ]
    },
    {},
    {},
    {
        "BACKGROUND": 0x73,
        "colors": [
        [0x03, 0x03, 0x08],
        [0x09, 0x04, 0x33],
        [0x00, 0x33, 0x36],
        [0x00, 0x00, 0x00],
        [0x00, 0x00, 0x00],
        [0x00, 0x73, 0x76],
        [0x0a, 0x0a, 0x0a],
        [0x00, 0x17, 0x1a]
        ]
    },
    {
        "CHARBASE": 0x4000
    }
]

dli_table_commando = [
    {
        "DLL": 0x1800,
        "CHARBASE": 0x8000,
        "colors_old": [
            [0x10, 0x6a, 0x15],
            [0xb0, 0x0f, 0x15],
            [0x00, 0x24, 0xea],
            [0x00, 0x27, 0xea],
            [0xb0, 0x02, 0xb5],
            [0x06, 0x85, 0x0c],
            [0xba, 0xb4, 0x0c],
            [0xe1, 0xb1, 0xf9]
        ],
        "colors": [
            [0xb0, 0xb3, 0x15],
            [0x10, 0x12, 0x15],
            [0x00, 0x84, 0xea],
            [0x00, 0x04, 0xea],
            [0xb0, 0xb1, 0xb5],
            [0x06, 0x00, 0x0c],
            [0x10, 0x39, 0x00],
            [0xe1, 0x10, 0xf9]
        ]
    },
    {
        "CHARBASE": 0x8000,
        "colors": [
            [0xb0, 0xb3, 0x15],
            [0x10, 0x12, 0x15],
            [0x00, 0x84, 0xea],
            [0x00, 0x04, 0xea],
            [0xb0, 0xb1, 0xb5],
            [0x06, 0x00, 0x0c],
            [0x10, 0x39, 0x00],
            [0xe1, 0x10, 0xf9]
        ]
    }
]

dli_index = 0
GRAPHIC_MODE = "160"
CHARBASE = 0x8000
BACKGROUND = 0
CTRL = 0x10     # Character width = double byte characters

dli_table = []
if game_name == "rtype1":
    dli_table = dli_table_rtype1
elif game_name == "rtype2":
    dli_table = dli_table_rtype2
elif game_name == "bentley":
    dli_table = dli_table_bentley
elif game_name.startswith("basketbrawl"):
    DLL = 0x1800
    colors = [
        [0x84, 0x00, 0x05],
        [0x32, 0x00, 0x05],
        [0x0f, 0x00, 0x37],
        [0x54, 0x00, 0x37],
        [0x19, 0x00, 0x27],
        [0x19, 0x00, 0x37],
        [0x54, 0x00, 0x22],
        [0x35, 0x31, 0x20]
    ]
    colors = [
        [0x0d, 0x08, 0x05],
        [0x1a, 0x17, 0x05],
        [0x0f, 0x00, 0x37],
        [0x54, 0x00, 0x37],
        [0x19, 0x00, 0x22],
        [0x19, 0x00, 0x37],
        [0x54, 0x00, 0x22],
        [0x59, 0x56, 0x20]
    ]
    colors = [
        [0x64, 0x00, 0x05],
        [0x32, 0x00, 0x05],
        [0x0f, 0x00, 0x37],
        [0x54, 0x00, 0x37],
        [0x19, 0x00, 0x22],
        [0x19, 0x00, 0x37],
        [0x54, 0x00, 0x22],
        [0x35, 0x31, 0x20]
    ]
elif game_name == "poleposition2":
    DLL = 0x2200
elif game_name == "ballblazer":
    dli_table = [
        {
            "DLL": 0x23BC,
            "CHARBASE": 0xA800,
            "CTRL": 0,
            "colors": [
                [0xcc, 0xc4, 0xc8],
                [0x04, 0x09, 0x08],
                [0x54, 0x56, 0x58],
                [0x34, 0x36, 0x38],
                [0x53, 0x57, 0x5a],
                [0xca, 0xc6, 0xc8],
                [0x56, 0x56, 0x58],
                [0x51, 0x56, 0x58]
            ]
        },
        {},
        {},
        {
            "CHARBASE": 0xA000
        }
    ]
elif game_name.startswith("fatalrun"):
    dli_table = dli_table_fatalrun
elif game_name == "alien_brigade":
    DLL = 0x1A34
    CHARBASE = 0x8000
    colors = [
        [0x02, 0x04, 0x00],
        [0x22, 0x26, 0x18],
        [0x00, 0x04, 0x0f],
        [0x00, 0xc4, 0x19],
        [0x00, 0xc4, 0xba],
        [0x00, 0xc6, 0x18],
        [0x00, 0xc4, 0x30],
        [0x30, 0x1f, 0x00]
    ]
elif game_name.startswith("commando"):
    dli_table = dli_table_commando
elif game_name.startswith("circus"):
    DLL = 0x01E00
    CHARBASE = 0xC000
    colors = [
        [0x34, 0x30, 0x0E],
        [0x86, 0x34, 0x0E],
        [0x15, 0x34, 0x0E],
        [0x00, 0x0E, 0x00],
        [0x00, 0x0E, 0x00],
        [0x0E, 0xA8, 0x3A],
        [0x1E, 0x14, 0x0E],
        [0x86, 0x82, 0x0E]
    ]    
elif game_name.startswith("rogue"):
    DLL = 0x180E
    CHARBASE = 0xC000
    colors = []
elif game_name == "genmicros" or game_name == "shotgun":
    DLL = 0x2496
    CHARBASE = 0xE000
    colors = [
        [0x04, 0x0d, 0x32],
        [0x1e, 0x00, 0x3c],
        [0x0f, 0x35, 0x2f],
        [0x0f, 0x2f, 0x35],
        [0xa1, 0xa2, 0x44],
        [0xa3, 0x35, 0xa4],
        [0x36, 0xa5, 0x37],
        [0x38, 0x39, 0x3a]
    ]
elif game_name == "demo" or game_name == "simple":
    DLL = 0x1800
    CHARBASE = 0xE000
elif game_name == "1942":
    DLL = 0x1800
    CHARBASE = 0xD000
else:
    CHARBASE = 0xC000
    DLL = 0x2496        # TAN demo
    colors = [
        [0x50, 0x02, 0x32],
        [0x35, 0x0F, 0x2f],
        [0x0f, 0x35, 0x2f],
        [0x0f, 0x2f, 0x35],
        [0x95, 0x3c, 0x3c],
        [0x25, 0x28, 0x2e],
        [0xc7, 0x2d, 0x2e],
        [0x0f, 0x00, 0x3c]
    ]


def save_tileset():
    tileset = m[0x8000:0xA000]
    img_tm = Image.new("L", (256,128))
    for tile in range(128):
        tile_x = tile % 16
        tile_y = int(tile/16)
        offset = tile*2
        x = tile_x*16
        for y in range(tile_y*16+15, tile_y*16-1,-1):
            byte = tileset[offset]
            img_tm.putpixel((x, y), (byte & 0xC0))
            img_tm.putpixel((x+1, y), (byte & 0xC0))
            img_tm.putpixel((x+2, y), (byte & 0x30) << 2)
            img_tm.putpixel((x+3, y), (byte & 0x30) << 2)
            img_tm.putpixel((x+4, y), (byte & 0xC) << 4)
            img_tm.putpixel((x+5, y), (byte & 0xC) << 4)
            img_tm.putpixel((x+6, y), (byte & 0x3) << 6)
            img_tm.putpixel((x+7, y), (byte & 0x3) << 6)
            byte = tileset[offset+1]
            img_tm.putpixel((x+8, y), (byte & 0xC0))
            img_tm.putpixel((x+9, y), (byte & 0xC0))
            img_tm.putpixel((x+10, y), (byte & 0x30) << 2)
            img_tm.putpixel((x+11, y), (byte & 0x30) << 2)
            img_tm.putpixel((x+12, y), (byte & 0x0C) << 4)
            img_tm.putpixel((x+13, y), (byte & 0x0C) << 4)
            img_tm.putpixel((x+14, y), (byte & 0x03) << 6)
            img_tm.putpixel((x+15, y), (byte & 0x03) << 6)
            offset += 256

    img_tm.show()
#    img_tm.save("tileset_commando.png")

def show_assets(graphic_mode):
    y = 255
    for offset in range(0, 65536, 256):
        x = 0
        for i in range(256):
            byte = m[offset + i]
            if graphic_mode == "160B":
                pixels = [(byte >> 6) | ((byte) & 12), ((byte << 2) & 12) | ((byte >> 4) & 3)]
                for pixel in pixels:
                    if pixel in [0, 4, 8, 12]:
                        clr = None
                    else:
                        clr = pixel - 1
                    if clr is not None:
                        color = clr << 4
                        img_assets.putpixel((x, y), (color, color, color))
                        img_assets.putpixel((x+1, y), (color, color, color))
                    x += 2
            else:
                color = (byte & 0xC0)
                img_assets.putpixel((x, y), (color, color, color))
                img_assets.putpixel((x+1, y), (color, color, color))
                color = (byte & 0x30) << 2
                img_assets.putpixel((x+2, y), (color, color, color))
                img_assets.putpixel((x+3, y), (color, color, color))
                color = (byte & 0xC) << 4
                img_assets.putpixel((x+4, y), (color, color, color))
                img_assets.putpixel((x+5, y), (color, color, color))
                color = (byte & 0x3) << 6
                img_assets.putpixel((x+6, y), (color, color, color))
                img_assets.putpixel((x+7, y), (color, color, color))
                x += 8
        y -= 1

#    img_assets.show()
#    img_assets.save("assets_basketbrawl.png")

def save_tilemap():
    with open("commando_tilemap2.tmx", "w") as f:
        f.write("""<?xml version="1.0" encoding="UTF-8"?>
<map version="1.10" tiledversion="1.10.2" orientation="orthogonal" renderorder="right-down" width="20" height="100" tilewidth="16" tileheight="16" infinite="0" nextlayerid="2" nextobjectid="1">
 <tileset firstgid="1" source="commando_tiles.tsx"/>
 <layer id="1" name="Tile Layer 1" width="20" height="100">
  <data encoding="csv">
""")
        offset = 0x9000
        offset = 0x2700
        for y in range(100):
            row = ",".join([str((byte >> 1)+1) for byte in m[offset:offset+20]])
            if y < 99:
                row = row + ","
            f.write(row + "\n")
            offset += 20
        f.write("""
</data>
</layer>
</map>""")

def scan_images():
    global m
    lines = [
        (0x5E00, 1),
        (0x5E01, 1),
        (0x5E02, 2),
        (0x5E04, 2),
        (0x5E06, 3),
        (0x5E09, 3),
        (0x5E0C, 3),
        (0x5E0F, 4),
        (0x5E13, 4),
        (0x5E17, 5),
        (0x5E1C, 5),
        (0x5E21, 6),
        (0x5E27, 6),
        (0x5E2D, 7),
        (0x5E34, 7),
        (0x5E3B, 8),
        (0x5E43, 8),
        (0x5E4B, 9),
        (0x5E54, 9),
        (0x5E5D, 10),
        (0x5E67, 10),
        (0x5E71, 11),
        (0x5E7C, 11),
        (0x5E87, 11),
        (0x5E92, 12),
        (0x5E9E, 12),
        (0x5EAA, 13),
        (0x5EB7, 13),
        (0x5EC4, 14),
        (0x5ED2, 14),
        (0x5EE0, 15),
        (0x5EEF, 15),
        (0x5C00, 16),
        (0x5C10, 16),
        (0x5C20, 17),
        (0x5C31, 17),
        (0x5C42, 18),
        (0x5C54, 18),
        (0x5C66, 19),
        (0x5C79, 19),
        (0x5C8C, 20),
        (0x5CA0, 20),
        (0x5CB4, 20),
        (0x5CC8, 21),
        (0x5CDD, 21),
        (0x5A00, 22),
        (0x5A16, 22),
        (0x5A2C, 23),
        (0x5A43, 23),
        (0x5A5A, 24),
        (0x5A72, 24),
        (0x5A8A, 25),
        (0x5AA3, 25),
        (0x5ABC, 26),
        (0x5AD6, 26),
        (0x5800, 27),
        (0x581B, 27),
        (0x5836, 28),
        (0x5852, 28),
        (0x586E, 28),
        (0x588A, 29),
        (0x58A7, 29)
    ]

    img_tm = Image.new("L", (232,len(lines*2)))
    y = 0
    next_addr = 0x5E00
    for addr, width in lines:
        if next_addr != addr:
            print(hex(next_addr), next_addr - addr)
        x = 0
        for offset in range(addr, addr+width):
            byte = m[offset+256]
            img_tm.putpixel((x, y+1), (byte & 0xC0))
            img_tm.putpixel((x+1, y+1), (byte & 0xC0))
            img_tm.putpixel((x+2, y+1), (byte & 0x30) << 2)
            img_tm.putpixel((x+3, y+1), (byte & 0x30) << 2)
            img_tm.putpixel((x+4, y+1), (byte & 0xC) << 4)
            img_tm.putpixel((x+5, y+1), (byte & 0xC) << 4)
            img_tm.putpixel((x+6, y+1), (byte & 0x3) << 6)
            img_tm.putpixel((x+7, y+1), (byte & 0x3) << 6)
            byte = m[offset+256]
            img_tm.putpixel((x, y), (byte & 0xC0))
            img_tm.putpixel((x+1, y), (byte & 0xC0))
            img_tm.putpixel((x+2, y), (byte & 0x30) << 2)
            img_tm.putpixel((x+3, y), (byte & 0x30) << 2)
            img_tm.putpixel((x+4, y), (byte & 0xC) << 4)
            img_tm.putpixel((x+5, y), (byte & 0xC) << 4)
            img_tm.putpixel((x+6, y), (byte & 0x3) << 6)
            img_tm.putpixel((x+7, y), (byte & 0x3) << 6)
            x += 8
        y += 2
        next_addr = addr + width

    img_tm.show()
#    img_tm.save("fatalrun_road.png")

#scan_images()
#quit()
#save_tileset()

def execute_dli():
    global dli_index, GRAPHIC_MODE, CHARBASE
    if len(dli_table) <= dli_index:
        return
    dli_entry = dli_table[dli_index]
    for entry in dli_entry.items():
        print(entry[0], "=", entry[1])
        globals()[entry[0]] = entry[1]
    dli_index += 1

def twos(val):
    val_str = bin(val)[2:]
    val_str = '0'*(5-len(val_str)) + val_str
    flip = False
    res = ''
    for i in range(4, -1, -1):
        bit = val_str[i]
        if flip:
            if bit == '1':
                res = '0' + res
            else:
                res = '1' + res
        else:
            res = bit + res
            if bit == '1':
                flip = True
    return int(res, 2)

def display_sprite320(x, y, width, height, gfx, palette, holey_dma, graphic_mode, img2, direct):
    something_drawn = False
    img_y = y+height-1
    gfx_offset = gfx
    palette_bit = palette & 4
    for j in range(height):
        gfx_offset_line = gfx_offset
        skip = False
        if img_y >= 240:
            skip = True
        if holey_dma == 'on':
            address_hex = hex(gfx_offset)[2]
            if address_hex in ['9', 'b', 'd', 'f']:
                skip = True

        if not skip:
            img_x = x*2
            for i in range(width):
                byte = m[gfx_offset]
                gfx_offset += 1
                if graphic_mode == "320A":
                    pixels = [byte & 0x80, byte & 0x40, byte & 0x20, byte & 0x10,
                            byte & 0x08, byte & 0x04, byte & 0x02, byte & 0x01]
                    for pixel in pixels:
                        clr = colors_7800[colors[palette][1]] if pixel else None
                        if clr and img_x < 320:
                            img.putpixel((img_x, img_y), clr)
                            img2.putpixel((img_x, img_y), clr)
                            something_drawn = True
                        img_x += 1
                elif graphic_mode == "320B":
                    pixels = [((byte >> 6) & 2) | ((byte >> 3) & 1),
                              ((byte >> 5) & 2) | ((byte >> 2) & 1),
                              ((byte >> 4) & 2) | ((byte >> 1) & 1),
                              ((byte >> 3) & 2) | ((byte) & 1)]
                    for pixel in pixels:
                        clr = colors_7800[colors[palette][pixel-1]] if pixel else None
                        if clr and img_x < 320:
                            img.putpixel((img_x, img_y), clr)
                            img2.putpixel((img_x, img_y), clr)
                            something_drawn = True
                        img_x += 1
                elif graphic_mode == "320C":
                    pixels = [((byte & 0x80), (palette_bit | ((byte >> 2) & 3))),
                            ((byte & 0x40), (palette_bit | ((byte >> 2) & 3))),
                            ((byte & 0x20), (palette_bit | (byte & 3))),
                            ((byte & 0x10), (palette_bit | (byte & 3)))]
                    for pixel, palette in pixels:
                        clr = colors_7800[colors[palette][1]] if pixel else None
                        if clr and img_x < 320:
                            img.putpixel((img_x, img_y), clr)
                            img2.putpixel((img_x, img_y), clr)
                            something_drawn = True
                        img_x += 1
                else:
                    print("ERROR: unknown graphic mode", graphic_mode)
        img_y -= 1
        gfx_offset = gfx_offset_line + 256
    return something_drawn

def display_sprite160(x, y, width, height, gfx, palette, holey_dma, graphic_mode, img2, direct):
    global img_assets
    something_drawn = False
    img_y = y+height-1
    gfx_offset = gfx
    palette_bit = palette & 4
    for j in range(height):
        gfx_offset_line = gfx_offset
        skip = False
        if img_y >= 240:
            skip = True
        address_hex = hex(gfx_offset)[2]
        if holey_dma == '8':
#            address_hex = hex(gfx_offset)[2]
            if height == 8:
                if address_hex in ['a', 'b', 'e', 'f']:
                    skip = True
        elif holey_dma == '16':
            if address_hex in ['9', 'b', 'd', 'f']:
                skip = True

        if not skip:
            img_x = x*2
            for i in range(width):
                byte = m[gfx_offset]
                asset_x = gfx_offset % 256
                asset_y = 255 - int(gfx_offset/256)
                gfx_offset += 1
                if graphic_mode == "160A":
                    pixels = [byte >> 6, (byte >> 4) & 3, (byte >> 2) & 3, byte & 3]
                    asset_x *= 8
                elif graphic_mode == "160B":
                    pixels = [(byte >> 6) | ((byte) & 12), ((byte << 2) & 12) | ((byte >> 4) & 3)]
                    asset_x *= 2
                else:
                    print("ERROR: mode", graphic_mode, "not supported")
                    pixels = []
                for idx, pixel in enumerate(pixels):
                    if graphic_mode == "160A":
                        clr = colors_7800[colors[palette][pixel-1]] if pixel else None
#                        if not direct and clr is None:
#                            print("COLOR TRANSPARENT?", palette, pixel, colors[palette], colors[palette][pixel-1])
                    elif graphic_mode == "160B":
                        if pixel in [0, 4, 8, 12]:
                            clr = None
                        else:
                            clr = colors_7800[colors[int((pixel-1)/4)+palette_bit][(pixel-1) % 4]]
                    img_x = img_x % 512
                    if clr is not None and img_x >= 0 and img_x < 320:
                        img.putpixel((img_x, img_y), clr)
                        img.putpixel((img_x+1, img_y), clr)
                        img2.putpixel((img_x, img_y), clr)
                        img2.putpixel((img_x+1, img_y), clr)
                        if img_assets:
                            img_assets.putpixel((asset_x+idx*2, asset_y), clr)
                            img_assets.putpixel((asset_x+idx*2+1, asset_y), clr)
                        something_drawn = True
                    else:
                        if not direct and gfx != 0x5000:
                            pass
#                            print("Not displayed, clr=", clr, "x=", img_x, "graphic_mode=", graphic_mode)
                    img_x += 2
            else:
                if not direct and gfx != 0x5000:
                    pass
#                    print("Line skipped")
        img_y -= 1
        gfx_offset = gfx_offset_line + 256
    return something_drawn

def display_direct(x, y, width, height, gfx, palette, holey_dma, graphic_mode):
#    print("DIRECT", x, y, width, height, gfx)
    global img_id
    img2 = Image.new("RGBA", (320,240), colors_7800[BACKGROUND] + (0,))
    if graphic_mode[:3] == "320":
        ret = display_sprite320(x, y, width, height, gfx, palette, holey_dma, graphic_mode, img2, True)
    else:
        ret = display_sprite160(x, y, width, height, gfx, palette, holey_dma, graphic_mode, img2, True)
    if ret:
        img2.save("%s/%s_line_%03d_%04d.png" % (game_name, game_name, y, img_id))
        img_id += 1
    return ret

def display_indirect(x, y, nb_tiles, height, gfx, palette, holey_dma, graphic_mode):
#    print("INDIRECT", x, y, nb_tiles, height, gfx)
    global img_id
    img2 = Image.new("RGBA", (320,240), (0,0,0,0))
    ret = False
    for i in range(nb_tiles):
        tile_id = m[gfx+i]
        if graphic_mode[:3] == "320":
            ret = display_sprite320(x+4*i, y, 1, height, CHARBASE+tile_id, palette, holey_dma, graphic_mode, img2, False) or ret
        else:
            byte_per_sprite = 2 if CTRL & 0x10 else 1
            ret = display_sprite160(x+4*byte_per_sprite*i, y, byte_per_sprite, height, CHARBASE+tile_id, palette, holey_dma, graphic_mode, img2, False) or ret
    if ret:
        img2.save("%s/%s_line_%03d_%04d_tiles.png" % (game_name, game_name, y, img_id))
        img_id += 1
    return ret

def read_dl(dl, y, height, holey_dma):
    global GRAPHIC_MODE

    width = m[dl+1] & 0x1F
    mode = "indirect" if m[dl+1] == 0x60 else "direct"

    if m[dl+1] == 0:
        next_dl = 0
    else:
        next_dl = dl+5 if width == 0 else dl+4

    if m[dl+1] == 0:
        return (next_dl, False)

    gfx = m[dl] + m[dl+2]*256

    # Indirect
    if width == 0:
        x = m[dl+4]
        if x > 200:
            x -= 256
        palette = m[dl+3] >> 5
        width = twos(m[dl+3] & 0x1F)
        GRAPHIC_MODE = GRAPHIC_MODE[:3] + ("A" if m[dl+1] & 0x80 == 0 else "B")
        if width == 0:
            width = 32
        if mode == "direct":
            ret = display_direct(x, y, width, height, gfx, palette, holey_dma, GRAPHIC_MODE)
        else:
            ret = display_indirect(x, y, width, height, gfx, palette, holey_dma, GRAPHIC_MODE)
        dump = "%02X %02X %02X %02X %02X" % (m[dl], m[dl+1], m[dl+2], m[dl+3], m[dl+4])
    else:
        x = m[dl+3]
        if x > 200:
            x -= 256
        palette = m[dl+1] >> 5
        width = twos(m[dl+1] & 0x1F)
        GRAPHIC_MODE = GRAPHIC_MODE[:3] + "A"
        ret = display_direct(x, y, width, height, gfx, palette, holey_dma, GRAPHIC_MODE)
        dump = "%02X %02X %02X %02X   " % (m[dl], m[dl+1], m[dl+2], m[dl+3])

    print("                                        [%X - %s] X=%3d, GFX=0x%X, width=%2d, palette=%d, mode=%s, graph mode=%s" % (dl, dump, x, gfx, width, palette, mode, GRAPHIC_MODE))
    return (next_dl, ret)

def read_dll(dll):
    try:
        os.mkdir(game_name)
    except:
        for f in os.listdir(game_name):
            if f.startswith(game_name + "_line_") and f.endswith(".png"):
                os.remove(game_name + "/" + f)
    
    y = 0
    use_when_not_displayed = True
    while True:
        b1 = m[dll]
        b2 = m[dll+1]
        b3 = m[dll+2]
        dl = b2 * 256 + b3
        height = (b1 & 15) + 1
        if b1 & 0x20:
            holey_dma = "8"
        elif b1 & 0x40:
            holey_dma = "16"
        else:
            holey_dma = "off"
#        if height == 8:
#            holey_dma = "on" if b1 & 0x20 else "off"
#        else:
#            holey_dma = "on" if b1 & 0x40 else "off"
        dli = " DLI" if b1 & 0x80 else ""
        print("[%02X %02X %02X] height=%2d (y=%3d), HoleyDMA=%s, DL=0x%X%s" % (b1, b2, b3, height, y, holey_dma, dl, dli))
        displayed = False
        if dli:
            execute_dli()
        while dl != 0:
            dl, ret = read_dl(dl, y, height, holey_dma)
            displayed = displayed or ret
        if displayed or use_when_not_displayed:
            y += height
            use_when_not_displayed = True
        dll += 3
        if m[dll] == 0:
            break

#save_tileset()
#save_tilemap()
img_assets = None
img_assets = Image.new("RGB", (2048,256))
show_assets("160A")
execute_dli()
read_dll(DLL)

img.show()
img_assets.save("assets_" + game_name + ".png")
img_assets.show()
