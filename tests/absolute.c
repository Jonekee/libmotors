#include <motors/driver.h>
#include <stdio.h>
#include <robotutils.h>

void cb2() {
	printf("finished path\n");
}

void cb1p5() {
	printf("reached point\n");
}

void cb1() {
	printf("follow path ...\n");
	addPointInPath(0, 200, -1, cb1p5);
	addPointInPath(-200, 0, -1, cb1p5);
	addPointInPath(0, 0, 0, cb2);
}

int main() {
	printf("go to (200, 200)\n");
	setPosition(0, 0);
	setHeading(0);
	moveTo(200, 200, -1, cb1);

	while(1) {
		printf("position [%d,%d], heading >%d°<\n", getPosX(), getPosY(), getHeading());
		waitFor(100);
	}
	return 0;
}
