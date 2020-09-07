#include <iostream>
#include <stdio.h>
#include <vector>
using namespace std;

int findString(string parent, string pattern){
	int parentSize = parent.size();
	int patternSize = pattern.size();
	for(int i = 0; i <= parentSize - patternSize; i++){
		bool finded = true;
		for(int j = 0 ; j < patternSize; j++){
			if(parent[i + j] != pattern[j]){
				finded = false;
				break;
			}
		}
		if(finded){
			return i;
		}
	}
	return -1;
}

vector<int> makeTable(string pattern){
	int patternSize = pattern.size();
	vector<int> table(patternSize, 0);
	int j = 0;
	for(int i = 1; i < patternSize; i++){
		while(j > 0 && pattern[i] != pattern[j]){
			j = table[j - 1];
		}

		if(pattern[i] == pattern[j]){
			table[i] = ++j;
		}
	}
	return table;
}


int main(void){
/*
	string parent = "Hello World";
	string pattern = "llo W";
	int result = findString(parent, pattern);
	if(result == -1){
		printf("찾을 수 없습니다.");
	}else{
		printf("%d번째에서 찾았습니다.", result + 1);
	}
	return 0;
*/
	string pattern = "abacaaba";
	vector<int> table = makeTable(pattern);
	for(int i = 0; i < table.size(); i++){
		printf("%d ", table[i]);
	}
	return 0;
}


