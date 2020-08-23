#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(void){
	vector<pair<int, string>> v;
	v.push_back(pair<int,string>(90,"A"));
	v.push_back(pair<int,string>(85,"B"));
	v.push_back(pair<int,string>(82,"C"));
	v.push_back(pair<int,string>(98,"D"));
	v.push_back(pair<int,string>(79,"E"));

	sort(v.begin(), v.end());
	for(int i = 0; i < v.size(); i++){
		cout << v[i].second << ' ';
	}
	return 0;
}
