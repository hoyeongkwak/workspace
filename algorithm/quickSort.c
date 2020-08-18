//Time Complex O(N * logN)
#include <stdio.h>

int number = 10;
int data[] = {1, 10, 5, 8, 7, 6, 4, 3, 2, 9};

void quickSort(int* data, int start, int end){
	//원소가 1개인 경우에는 그대로 둔다
	if( start >= end){
		return;
	}

	int key = start;   // Key는 첫 번째 원소
	int i = start + 1;
	int j = end;
	int temp;

	while(i <= j) { //엇갈릴 때까지 반복
		while(data[i] <= data[key] && i <= end){  // 키 값보다 큰값을 만날때까지
			i++;
		}
		while(data[j] >= data[key] && j > start){ // 키 값보다 작은값을 만날때까지
			j--;
		}
		
		if(i > j){					// 현재 엇갈린 상태면 키 값과 교체
			temp = data[j];
			data[j] = data[key];
			data[key] = temp;
		}else{						// 엇갈리지 않았다면 i와 j를 교체
			temp = data[i];
			data[i] = data[j];
			data[j] = temp;
		}
	}
	quickSort(data, start, j -1 );
	quickSort(data, j + 1, end);
}

int main(void){
	quickSort(data, 0, number - 1);
	for(int i = 0; i < number; i++){
		printf("%d ", data[i]);
	}
	printf("\n");
	return 0;
}
