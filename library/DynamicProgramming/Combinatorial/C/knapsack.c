#include <stdio.h>



int solve(int number , int weight , int items[][2]){

	return 0;
}


int main(){
	
	int n,w;
	scanf("%d %d" , &n,&w);
	int items[n][2];

	for(int i = 0; i < n; i++){
			scanf("%d %d" , &items[i][0] , &items[i][1]);
	}
	
	printf("%d\n",solve(n,w,items));

	return 0;
}
