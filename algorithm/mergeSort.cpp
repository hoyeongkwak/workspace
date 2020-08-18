/*
 MergeSort는 quickSort보다 더 빠른것은 아니지만, O(N*logN)의 시간복잡도를 보장해준다(최악일때에도)
 하지만 기존의 데이터를 담을 추가적인 배열 공간이 필요하다는 점에서 메모리 활용이 비효율적이다
*/
#include <stdio.h>
const int number = 8;

int size;
int sorted[8]; // 정렬 배열은 반드시 전역 변수로 선언
int count = 0;

void merge(int a[], int m, int middle, int n){
	int i = m;
	int j = middle + 1;
	int k = m;
	int t;
	//작은 순서대로 배열에 삽입
	while(i <= middle && j <= n){
		if(a[i] <= a[j]){
			sorted[k] = a[i];
			i++;
		}else{
			sorted[k] = a[j];
			j++;
		}
		k++;
	}
	//남은 데이터도 삽입
	if(i > middle){
		for(t = j; t <= n; t++){
			sorted[k] = a[t];
			k++;
		}
	}else{
		for(t = i; t <= middle; t++){
			sorted[k] = a[t];
			k++;
		}
	}
	//정렬된 배열을 삽입
	for(t = m; t <= n; t++){
		a[t] = sorted[t];
	}	
}

void mergeSort(int a[], int m, int n){
	// 이외의 경우는 크기가 1개인 경우
	if(m < n){
		int middle = (m + n) / 2;
		mergeSort(a, m, middle);
		mergeSort(a, middle + 1, n);
		merge(a, m, middle, n);
	}
}

int main(void){
	int i;
	int array[number] = {7, 6, 5, 8, 3, 5, 9 ,1};
	mergeSort(array, 0, number -1);
	for(i = 0; i < number; i++){
		printf("%d ", array[i]);
	}
	printf("\n");
}