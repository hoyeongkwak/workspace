#include <stdio.h>

int number = 4;
int INF = 1000000;

//자료 배열을 초기화
int a[4][4] = {
	{0, 5, INF, 8},
	{7, 0, 9, INF},
	{2, INF, 0, 4},
	{INF, INF, 3, 0}
};

void floydWarshall(){
	//결과 그래프 초기화
	int d[number][number];

	//결과 그래프 초기화
	for(int i = 0; i < number; i++){
		for(int j = 0; j < number; j++){
			d[i][j] = a[i][j];
		}
	}

	//k = 거쳐가는 노드 
	for(int k = 0; k < number; k++){
		// i = 출발 노드
		for(int i = 0; i < number; i++){
			// j = 도착 노드
			for( int j = 0; j < number; j++){
				if(d[i][k] + d[k][j] < d[i][j]){
					d[i][j] = d[i][k] + d[k][j];
				}
			}
		}
	}

	//결과 출력
	for(int i = 0; i < number; i++){
		for(int j = 0; j < number; j++){
			printf("%3d ", d[i][j]);
		}
		printf("\n");
	}
}

int main(void){
	floydWarshall();
}
