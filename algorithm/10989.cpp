#include <iostream>

using namespace std;

int n, m;
int a[10001];

int main(void){
	scanf("%d", &n);
	for(int i = 0; i < n; i++)
	{
		scanf("%d", &m);
		a[m]++;
	}
	for(int i = 0; i < 10001; i++)
	{
		while(a[i] != 0){
			printf("%d\n", i);
			a[i]--;
		}
	}
}
