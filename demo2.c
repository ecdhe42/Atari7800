#include "prosystem.h"

#define multisprite_color(color) ((color >= 0xf0)?(0x20 + (color & 0x0f)):((color)))


reversed scattered(16,16) char tiles[256] = {
	0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55,
	0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55,
	0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55,
	0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55,
	0x55, 0x55, 0x55, 0x41, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x41, 0x55, 0x55, 0x55, 0x55,
	0x55, 0x55, 0x50, 0x28, 0x15, 0x55, 0x55, 0x55, 0x55, 0x55, 0x50, 0x14, 0x15, 0x55, 0x55, 0x55,
	0x55, 0x55, 0x4a, 0xaa, 0x85, 0x55, 0x55, 0x55, 0x55, 0x55, 0x45, 0x55, 0x45, 0x55, 0x55, 0x55,
	0x55, 0x50, 0x2a, 0xaa, 0xa1, 0x55, 0x55, 0x55, 0x55, 0x50, 0x15, 0x55, 0x51, 0x55, 0x55, 0x55,
	0x55, 0x0a, 0xaa, 0xaa, 0xa8, 0x15, 0x55, 0x55, 0x55, 0x05, 0x55, 0x55, 0x54, 0x15, 0x55, 0x55,
	0x50, 0xaa, 0xaa, 0xaa, 0xaa, 0x80, 0x15, 0x50, 0x50, 0x55, 0x55, 0x55, 0x55, 0x40, 0x15, 0x50,
	0x0a, 0xaa, 0xaa, 0xaa, 0xaa, 0xaa, 0x80, 0x0a, 0x05, 0x55, 0x55, 0x55, 0x55, 0x55, 0x40, 0x05,
	0xaa, 0xaa, 0xaa, 0xaa, 0xaa, 0xaa, 0xaa, 0xaa, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55,
	0xaa, 0xaa, 0xaa, 0xaa, 0xaa, 0xaa, 0xaa, 0xaa, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55,
	0xaa, 0xaa, 0xaa, 0xaa, 0xaa, 0xaa, 0xaa, 0xaa, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55,
	0xaa, 0xaa, 0xaa, 0xaa, 0xaa, 0xaa, 0xaa, 0xaa, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55,
	0xaa, 0xaa, 0xaa, 0xaa, 0xaa, 0xaa, 0xaa, 0xaa, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55
};

const char tilemap1[40] = {
	0, 2, 4, 6, 0, 2, 4, 6, 0, 2, 4, 6, 0, 2, 4, 6, 0, 2, 4, 6,	0, 2, 4, 6, 0, 2, 4, 6, 0, 2, 4, 6, 0, 2, 4, 6, 0, 2, 4, 6
};
const char tilemap2[40] = {
	8,10,12,14, 8,10,12,14, 8,10,12,14, 8,10,12,14, 8,10,12,14, 8,10,12,14, 8,10,12,14, 8,10,12,14, 8,10,12,14, 8,10,12,14
};

#define DLL_ARRAY_SIZE 14
ramchip unsigned char dll[64];
ramchip unsigned char dl0[192];
ramchip unsigned char dl_empty[2];

#include "joystick.h"

unsigned char tanx, tany, tmp, tmp2, delay, row, col, i;
signed char tandx, tandy;
char sprite_x[DLL_ARRAY_SIZE], sprite_y;
unsigned char *tilemap_ptr, *ptr, mask_ptr;
unsigned char row_tilemap[DLL_ARRAY_SIZE];
unsigned char row_x[DLL_ARRAY_SIZE];
unsigned char col_x[DLL_ARRAY_SIZE];

void init_dll() {
	tmp = 0;
	for (i=0; i<1; i++) {
		dll[tmp++] = 0x47;
		dll[tmp++] = dl_empty >> 8;
		dll[tmp++] = dl_empty;
	}
	tilemap_ptr = dl0;
	for (i=0; i<DLL_ARRAY_SIZE; i++) {
		dll[tmp++] = 0x4F;
		dll[tmp++] = tilemap_ptr >> 8;
		dll[tmp++] = tilemap_ptr;
		tilemap_ptr += 7;
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
	tilemap_ptr = tilemap1;
	for (i=0; i<DLL_ARRAY_SIZE; i++) {
		if (i & 1) {
		dl0[tmp++] = tilemap1;
		dl0[tmp++] = 0x60;
		dl0[tmp++] = tilemap1 >> 8;
		} else {
		dl0[tmp++] = tilemap2;
		dl0[tmp++] = 0x60;
		dl0[tmp++] = tilemap2 >> 8;
		}
		dl0[tmp++] = 11 | ((i >> 1) << 5);
		dl0[tmp++] = 0;

		dl0[tmp++] = 0;	// End of DL
		dl0[tmp++] = 0;
		if (i & 1) {
			tmp2 = tilemap1;
		} else {
			tmp2 = tilemap2;
		}
		row_tilemap[i] = tmp2;
		row_x[i] = 0;
		col_x[i] = 0;
		sprite_x[i] = 0;
	}

	dl_empty[0] = 0;
	dl_empty[1] = 0;
	tilemap_ptr = tilemap1;
}

void main()
{
	init_dll();
    while (!(*MSTAT < 0)); // Wait for VBLANK
    while (*MSTAT < 0); // Wait for end of VBLANK

    X = 0;
    do {
        strobe(WSYNC);
        strobe(WSYNC);
        X++;
    } while (!(*MSTAT & 0x80));


   	// Background palette
    *BACKGRND = 0x00;					// Tiles
    *P0C1 = 241;
    *P0C2 = 242;
    *P0C3 = 0;

    *P1C1 = 242;
    *P1C2 = 243;
    *P1C3 = 0;

    *P2C1 = 243;
    *P2C2 = 244;
    *P2C3 = 0;

    *P3C1 = 244;
    *P3C2 = 246;
    *P3C3 = 0;

    *P4C1 = 246;
    *P4C2 = 248;
    *P4C3 = 0;

    *P5C1 = 248;
    *P5C2 = 250;
    *P5C3 = 0;

    *P6C1 = 250;
    *P6C2 = 252;
    *P6C3 = 0;

    *P7C1 = 252;
    *P7C2 = 254;
    *P7C3 = 0;


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
        joystick_update();

		if (delay != 16) {
			delay++;
		}

		delay = 0;

		tmp = 0;
		for (i=0; i<DLL_ARRAY_SIZE; i++) {
			row_x[i] += (i+1);
			tmp2 = row_x[i];
			if (tmp2 >= 16) {
				row_x[i] -= 16;
				tmp2 = sprite_x[i];
				if (tmp2 != -7) {
					tmp2--;
            	    sprite_x[i] = tmp2;
					tmp += 4;
					dl0[tmp] = tmp2;
					tmp+=3;
	            } else {
					sprite_x[i] = 0;
					tmp2 = col_x[i];
					tmp2++;
					if (tmp2 == 4) {
						col_x[i] = 0;
						if (i & 1) {
							dl0[tmp] = tilemap1;
						} else {
							dl0[tmp] = tilemap2;
						}
					} else {
						col_x[i] = tmp2;
						dl0[tmp] += 1;
					}
					tmp += 4;
					dl0[tmp] = 0;
					tmp+=3;
				}
			} else {
				tmp += 7;
			}
		}
    } while(1);
}
