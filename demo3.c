#include "prosystem.h"


#define multisprite_color(color) ((color >= 0xf0)?(0x20 + (color & 0x0f)):((color)))


holeydma reversed scattered(16,4) char tiles[64] = {
	0x55, 0x55, 0xaa, 0xaa, 0x55, 0x55, 0xaa, 0xaa, 0x55, 0x55, 0xaa, 0xaa, 0x55, 0x55, 0xaa, 0xaa,
	0x55, 0x55, 0xaa, 0xaa, 0x55, 0x55, 0xaa, 0xaa, 0x55, 0x55, 0xaa, 0xaa, 0x55, 0x55, 0xaa, 0xaa,
	0x55, 0x55, 0xaa, 0xaa, 0x55, 0x55, 0xaa, 0xaa, 0x55, 0x55, 0xaa, 0xaa, 0x55, 0x55, 0xaa, 0xaa,
	0x55, 0x55, 0xaa, 0xaa, 0x55, 0x55, 0xaa, 0xaa, 0x55, 0x55, 0xaa, 0xaa, 0x00, 0x00, 0x00, 0x00
};
holeydma reversed scattered(16,4) char tiles_gen[64] = {
	0x55, 0x55, 0xaa, 0xaa, 0x55, 0x55, 0xaa, 0xaa, 0x55, 0x55, 0xaa, 0xaa, 0x54, 0x10, 0x22, 0x8a,
	0x51, 0x51, 0xa0, 0x8a, 0x51, 0x10, 0xa0, 0x0a, 0x51, 0x11, 0xa2, 0x0a, 0x54, 0x10, 0x22, 0x8a,
	0x55, 0x55, 0xaa, 0xaa, 0x45, 0x11, 0x82, 0x0a, 0x40, 0x11, 0x2a, 0x22, 0x40, 0x11, 0x2a, 0x0a,
	0x45, 0x11, 0x2a, 0x22, 0x45, 0x11, 0x82, 0x22, 0x55, 0x55, 0xaa, 0xaa, 0x00, 0x00, 0x00, 0x00
};

const char tilemap1[40] = {
	0, 2, 4, 6, 0, 2, 4, 6, 0, 2, 4, 6, 0, 2, 4, 6, 0, 2, 4, 6,	0, 2, 4, 6, 0, 2, 4, 6, 0, 2, 4, 6, 0, 2, 4, 6, 0, 2, 4, 6
};
const char tilemap2[40] = {
	8,10,12,14, 8,10,12,14, 8,10,12,14, 8,10,12,14, 8,10,12,14, 8,10,12,14, 8,10,12,14, 8,10,12,14, 8,10,12,14, 8,10,12,14
};

#define DLL_ARRAY_SIZE 16
#define ROW_SIZE 8
ramchip unsigned char dll[64];
ramchip unsigned char dl0[192];
ramchip unsigned char dl_empty[2];

#include "joystick.h"

unsigned char tanx, tany, tmp, tmp2, delay, row, col, i, pos;
signed char tandx, tandy;
char sprite_x[DLL_ARRAY_SIZE], sprite_y;
unsigned char *tilemap_ptr, *ptr, mask_ptr;
unsigned char row_tilemap[DLL_ARRAY_SIZE];
unsigned char row_x[DLL_ARRAY_SIZE];
unsigned char col_x[DLL_ARRAY_SIZE];

unsigned char color;

void interrupt dli() {
	X = color;
    *P0C1 = X++;
    *P0C2 = X++;
    *P1C1 = X++;
    *P1C2 = X++;
    *P2C1 = X++;
    *P2C2 = X++;
    *P3C1 = X++;
    *P3C2 = X++;
    *P4C1 = X++;
    *P4C2 = X++;
    *P5C1 = X++;
    *P5C2 = X++;
    *P6C1 = X++;
    *P6C2 = X++;
    *P7C1 = X++;
    *P7C2 = X++;
	color += 16;
}

void init_dll() {
	tmp = 0;
	for (i=0; i<1; i++) {
		dll[tmp++] = 0x47;
		dll[tmp++] = dl_empty >> 8;
		dll[tmp++] = dl_empty;
	}
	tilemap_ptr = dl0;
	for (i=0; i<DLL_ARRAY_SIZE; i++) {
		dll[tmp++] = 0xCD;
		dll[tmp++] = tilemap_ptr >> 8;
		dll[tmp++] = tilemap_ptr;
	}
	for (i=0; i<2; i++) {
		dll[tmp++] = 0x4F;
		dll[tmp++] = dl_empty >> 8;
		dll[tmp++] = dl_empty;
	}
	dll[tmp++] = 0;
	dll[tmp++] = 0;
	dll[tmp++] = 0;
	dll[tmp++] = 0;
	dll[tmp++] = 0;
	dll[tmp++] = 0;

	tmp = 0;
	pos = 16;
	tmp2 = 0x1C;
	tilemap_ptr = tilemap1;
	for (i=0; i<ROW_SIZE; i++) {
		dl0[tmp++] = tiles;
		dl0[tmp++] = tmp2; //0x1C | (i << 5);
		dl0[tmp++] = tiles >> 8;
		dl0[tmp++] = pos;
		tmp2 += 32;
		pos += 16;
	}
	dl0[tmp++] = 0;	// End of DL
	dl0[tmp++] = 0;

	dl_empty[0] = 0;
	dl_empty[1] = 0;
	tilemap_ptr = tilemap1;

	color = 0;
	ptr = 0xFFFA;
	*ptr = dli;
	ptr = 0xFFFB;
	*ptr = dli >> 8;
}

void main()
{
	color = 0;
	init_dll();
	joystick_init();
    while (!(*MSTAT < 0)); // Wait for VBLANK
    while (*MSTAT < 0); // Wait for end of VBLANK

    X = 0;
    do {
        strobe(WSYNC);
        strobe(WSYNC);
        X++;
    } while (!(*MSTAT & 0x80));

ptr = 0xFFFA;
	*ptr = dli;
	ptr = 0xFFFB;
	*ptr = dli >> 8;

   	// Background palette
    *BACKGRND = 0x00;					// Tiles
    *P0C1 = 241;
    *P0C2 = 242;
    *P0C3 = 243;

    *P1C1 = 242;
    *P1C2 = 243;
    *P1C3 = 6;

    *P2C1 = 243;
    *P2C2 = 244;
    *P2C3 = 7;

    *P3C1 = 244;
    *P3C2 = 246;
    *P3C3 = 8;

    *P4C1 = 246;
    *P4C2 = 248;
    *P4C3 = 9;

    *P5C1 = 248;
    *P5C2 = 250;
    *P5C3 = 10;

    *P6C1 = 250;
    *P6C2 = 252;
    *P6C3 = 11;

    *P7C1 = 252;
    *P7C2 = 254;
    *P7C3 = 12;


	*CHARBASE = (tiles) >> 8;
	*DPPH = dll >> 8; // 1 the current displayed buffer
	*DPPL = dll;
	*CTRL = 0x50;

    delay = 0;
	row = 0;
	col = 0;

    // Main loop
    do {
		while (!(*MSTAT < 0));
		color = 0;
        joystick_update();
		if (joystick[0] & JOYSTICK_BUTTON1) {
			tmp = 0;
			for (i=0; i<ROW_SIZE; i++) {
				dl0[tmp] = tiles_gen;
				tmp += 4;
			}
		} else {
			tmp = 0;
			for (i=0; i<ROW_SIZE; i++) {
				dl0[tmp] = tiles;
				tmp += 4;
			}
		}

    } while(1);
}
