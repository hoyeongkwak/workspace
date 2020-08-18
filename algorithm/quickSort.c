//Time Complex O(N * logN)
#include <stdio.h>

int number = 10;
int data[] = {1, 10, 5, 8, 7, 6, 4, 3, 2, 9};

void quickSort(int* data, int start, int end){
	if( start >= end){
		return;
	}

	int key = start;
	int i = start + 1;
	int j = end;
	int temp;

	while(i <= j) { //cross roof
		while(data[i] <= data[key] && i <= end){
			i++;
		}
		while(data[j] >= data[key] && j > start){
			j--;
		}
		if(i > j){
			temp = data[j];
			data[j] = data[key];
			data[key] = temp;
		}else{
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
