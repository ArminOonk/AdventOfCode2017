// Thanks peasant-trip
// https://www.reddit.com/r/adventofcode/comments/7lms6p/2017_day_23_solutions/drnl3gg/

#include <stdio.h>
#include <stdbool.h>
void main() {
	int a = 1;
	int b = 0;
	int c = 0;
	int d = 0;
	int e = 0;
	int f = 0;
	int g = 0;
	int h = 0;
	
	
	b = 65;
	c = b;
	if (a != 0) {
		b = 100 * b + 100000;
		c = b + 17000;
	}

	while (true) {
		f = 1;
		d = 2;
		do {
			e = 2;
			
			/*do {
				if (d * e == b) {
					f = 0;
				}
				e++;
			} while (e != b);*/
			
			if( b%d == 0) {
				f = 0;
			}
			e = b;
			
			d++;
		} while (d != b);
		
		if (f == 0) {
			h++;
		}
		
		if (b == c) {
			break;
		}
		b += 17;
	}
	
	printf("a %d\n", a);
	printf("b %d\n", b);
	printf("c %d\n", c);
	printf("d %d\n", e);
	printf("e %d\n", e);
	printf("f %d\n", f);
	printf("g %d\n", g);
	printf("h %d\n", h);

}