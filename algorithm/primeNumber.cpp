#include <stdio.h>
#include <math.h>

bool isPrimeNumber(int x){
	int end = (int) sqrt(x);
	for(int i = 2; i <= end; i++){
		if(x % i == 0) return false;
	}
	return true;
}

int number = 100000;
int a[100001];

void PrimeNumberSieve(){
	for(int i = 2; i <= number; i++){
		a[i] = i;
	}
	for(int i = 2; i<= number; i++){
		if(a[i] == 0) continue;
		for(int j = i + i; j <= number; j += i){
			a[j] = 0;
		}
	}
	for(int i = 2; i <= number; i++){
		if(a[i] != 0)
			printf("%d ", a[i]);
	}
}

int main(void)
{
	//printf("%d", isPrimeNumber(97));
	PrimeNumberSieve();
	return 0;
}
