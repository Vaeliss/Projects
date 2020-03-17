#include <stdio.h>


void solve_hanoi(int from,int to,int temp,int dim){
	if (dim>0) {
		solve_hanoi(from,temp,to,dim-1);
		printf("Move from T%d to T%d\n",from,to);
		solve_hanoi(temp,to,from,dim-1);
	}
}

int main(void){
	solve_hanoi(1,2,3,5);
	return 0;
}
