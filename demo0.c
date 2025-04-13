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

reversed scattered(16,2) char head[32] = {
	0x05, 0x40, 0x15, 0x50,
	0x15, 0x50, 0x15, 0x50,
	0x2b, 0xa0, 0xbe, 0xf8,
	0xbb, 0xb8, 0xbb, 0xb8,
	0x2b, 0xa0, 0x3f, 0xf0,
	0x3e, 0xf0, 0x15, 0x50,
	0x1b, 0x90, 0x1e, 0xd0,
	0x1f, 0xd0, 0x05, 0x40
};

const char tilemap1[40] = {
	0, 2, 4, 6, 0, 2, 4, 6, 0, 2, 4, 6, 0, 2, 4, 6, 0, 2, 4, 6,	0, 2, 4, 6, 0, 2, 4, 6, 0, 2, 4, 6, 0, 2, 4, 6, 0, 2, 4, 6
};
const char tilemap2[40] = {
	8,10,12,14, 8,10,12,14, 8,10,12,14, 8,10,12,14, 8,10,12,14, 8,10,12,14, 8,10,12,14, 8,10,12,14, 8,10,12,14, 8,10,12,14
};

#define DLL_ARRAY_SIZE 14
#define DL_NUM_SPRITES 15
ramchip unsigned char dll[64];
ramchip unsigned char dl0[2048];
ramchip unsigned char dl_empty[2];

#define MOVE_SPRITE(tmp) dl0[5 + 3+tmp]++; dl0[5 + DL_NUM_SPRITES * 4 + 2 + 5 + 3+tmp]++; dl0[(5 + DL_NUM_SPRITES * 4 + 2)*2 + 5 + 3+tmp]++; dl0[(5 + DL_NUM_SPRITES * 4 + 2)*3 + 5 + 3+tmp]++; dl0[(5 + DL_NUM_SPRITES * 4 + 2)*4 + 5 + 3+tmp]++; dl0[(5 + DL_NUM_SPRITES * 4 + 2)*5 + 5 + 3+tmp]++; dl0[(5 + DL_NUM_SPRITES * 4 + 2)*6 + 5 + 3+tmp]++; dl0[(5 + DL_NUM_SPRITES * 4 + 2)*7 + 5 + 3+tmp]++; dl0[(5 + DL_NUM_SPRITES * 4 + 2)*8 + 5 + 3+tmp]++; dl0[(5 + DL_NUM_SPRITES * 4 + 2)*9 + 5 + 3+tmp]++; dl0[(5 + DL_NUM_SPRITES * 4 + 2)*10 + 5 + 3+tmp]++; dl0[(5 + DL_NUM_SPRITES * 4 + 2)*11 + 5 + 3+tmp]++; dl0[(5 + DL_NUM_SPRITES * 4 + 2)*12 + 5 + 3+tmp]++; dl0[(5 + DL_NUM_SPRITES * 4 + 2)*13 +  5 + 3 +tmp]++;

#include "joystick.h"

unsigned char tanx, tany, tmp, tmp2, delay, row, col, i, j, counter1, counter2, counter3, counter4, counter5;
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

		tmp2 = 0;
		if (i & 1) {
			tilemap_ptr[tmp2++] = tilemap1;
			tilemap_ptr[tmp2++] = 0x60;
			tilemap_ptr[tmp2++] = tilemap1 >> 8;
		} else {
			tilemap_ptr[tmp2++] = tilemap2;
			tilemap_ptr[tmp2++] = 0x60;
			tilemap_ptr[tmp2++] = tilemap2 >> 8;
		}
		tilemap_ptr[tmp2++] = 11 | ((i >> 1) << 5);
		tilemap_ptr[tmp2++] = 0;
		for (j=0; j<DL_NUM_SPRITES; j++) {
			tilemap_ptr[tmp2++] = head;
			tilemap_ptr[tmp2++] = 0xFE;
			tilemap_ptr[tmp2++] = head >> 8;
			tilemap_ptr[tmp2++] = (j << 3) + i;
		}
		tilemap_ptr[tmp2++] = 0;
		tilemap_ptr[tmp2++] = 0;

		tilemap_ptr += 5 + DL_NUM_SPRITES * 4 + 2;
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

    *P7C1 = multisprite_color(30);	// Francois
    *P7C2 = multisprite_color(0x00);
    *P7C3 = multisprite_color(0x3c);

	*CHARBASE = (tiles) >> 8;
	*DPPH = dll >> 8; // 1 the current displayed buffer
	*DPPL = dll;
	*CTRL = 0x50;

//	while (!(*MSTAT < 0));


    delay = 0;
	row = 0;
	col = 0;
	counter1 = 0;
	counter2 = 0;
	counter3 = 0;
	counter4 = 0;

    // Main loop
    do {
		while (!(*MSTAT < 0));
		while (*MSTAT < 0); // Wait for end of VBLANK
        joystick_update();

		if (delay != 16) {
			delay++;
		}

		tmp = 0;

		delay = 0;

		if (joystick[0] & JOYSTICK_BUTTON1) {
			MOVE_SPRITE(0);
			MOVE_SPRITE(4);
			MOVE_SPRITE(8);
			MOVE_SPRITE(12);
			MOVE_SPRITE(16);
			MOVE_SPRITE(20);
			MOVE_SPRITE(24);
			MOVE_SPRITE(28);
			MOVE_SPRITE(32);
			MOVE_SPRITE(36);
			MOVE_SPRITE(40);
			MOVE_SPRITE(44);
			MOVE_SPRITE(48);
			MOVE_SPRITE(52);
			MOVE_SPRITE(56);
		}
    } while(1);
}
