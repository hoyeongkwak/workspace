#include <iostream>
#include <fstream>
#include <string>

int main(){
	std::ifstream in("test.txt");
	char buf[100];

	if(!in.is_open()){
		std::cout << "file not found" << std::endl;
		return 0;
	}
	std::string s;
	while(in){
//		in.getline(buf, 100);
		getline(in, s);
		std::cout << buf << std::endl;
	}

	return 0;
}
