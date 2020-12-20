#include <iostream>
#include <vector>
#include <string>
#include <bitset>
using namespace std;

bool isUniqueChars(const string &str){
	if(str.length() > 128){
		return false;
	}
	vector<bool> char_set(128);

	for(int i = 0 ; i < str.length(); i++){
		int val = str[i];
		if(char_set[val]){
			return false;
		}
		char_set[val] = true;
	}
	return true;
}

bool isUniqueChars_bitvector(const string &str){
	bitset<256> bits(0);
	for(int i = 0; i < str.length(); i++){
		int val = str[i];
		if(bits.test(val) > 0){
			return false;
		}
		bits.set(val);
	}
	return true;
}

bool isUniqueChars_noDS(const string &str){
	for(int i = 0; i < str.length()-1; i++){
		for(int j = i+1; j < str.length(); i++){
			if(str[i] == str[j]){
				return false;
			}
		}
	}
	return true;
}

int main(void){
	
	vector<string> word_list = {"abcde", "hello", "apple", "kite", "padle"};
	
	for(auto word : word_list)
	{
		cout << word << string(": ") << boolalpha << isUniqueChars(word) << endl;
	}
	cout << endl << "Using bit vector" << endl;
	for(auto word : word_list)
	{
		cout << word << string(": ") << boolalpha << isUniqueChars_bitvector(word) << endl;
	}
	
	cout << endl << "Using no Data Structures" << endl;

	for(auto word : word_list)
	{
		cout << word << string(": ") << boolalpha << isUniqueChars_noDS(word) << endl;
	}

	return 0;
}
