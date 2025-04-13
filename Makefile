all: demo0.a78 demo1.a78 demo2.a78 demo3.a78

demo0.a78: demo0.c
	cc7800 -I../../../Atari7800/cc7800/headers demo0.c -o $@

demo1.a78: demo1.c
	cc7800 -I../../../Atari7800/cc7800/headers demo1.c -o $@

demo2.a78: demo2.c
	cc7800 -I../../../Atari7800/cc7800/headers demo2.c -o $@

demo3.a78: demo3.c
	cc7800 -I../../../Atari7800/cc7800/headers demo3.c -o $@

0: demo0.a78
	a7800 a7800 -cart demo0.a78

1: demo1.a78
	a7800 a7800 -cart demo1.a78

2: demo2.a78
	a7800 a7800 -cart demo2.a78

3: demo3.a78
	a7800 a7800 -cart demo3.a78

clean:
	rm demo0.tan demo1.a78 demo2.a78 demo3.a78
