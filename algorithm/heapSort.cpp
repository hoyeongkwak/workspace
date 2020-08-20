#include <stdio.h>

int number = 9;
int heap[9] = {7, 6, 5, 8, 3, 5, 9, 1, 6};

int main(void){
	//Heap 구성
	for(int i = 1; i < number; i++){
		int c = 1;
		do{
			int root = (c - 1) / 2;
			if(heap[root] < heap[c]){
				int temp = heap[root];
				heap[root] = heap[c];
				heap[c] = temp;
			}
			c = root;
//			printf("[first] c : %d\n", c);
//			printf("[first] heap[root] : %d\n", heap[root]);
//			printf("[first] heap[c] : %d\n", heap[c]);

		}while(c != 0);
	}
	// 크기를 줄여가며 반복적으로 힙을 구성
	for(int i = number -1; i >= 0; i--){
		int temp = heap[0];
		heap[0] = heap[i];
		heap[i] = temp;
		int root = 0;
		int c = 1;
		do{
			c = 2 * root + 1;
			//자식 중에 더 큰 값을 찾기
			if(c < i - 1 && heap[c] < heap[c + 1]){
				c++;
			}
			if(c < i && heap[root] < heap[c]){
				temp = heap[root];
				heap[root] = heap[c];
				heap[c] = temp;
			}
			root = c;
//			printf("[second] c : %d\n", c);
//			printf("[second] heap[root]; %d\n", heap[root]);
//			printf("[second] heap[c] : %d\n", heap[c]);
		}while(c < i);
	}
	//결과 출력
	for(int i = 0; i < number; i++){
		printf("%d", heap[i]);
	}
	printf("\n");
}

		
