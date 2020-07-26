#include <iostream>
#include <fstream>
#include <string>

int main() {
	std::ifstream in("test.txt", std::ios::binary);
	std::string s;

	int x;
	if(in.is_open()) 
	{
		in.read((char*)(&x), 4);
		std::cout << std::hex << x << std::endl;
	} 
	else 
	{
		std::cout << "file not found" << std::endl;
	}

	in.close();
	in.open("other.txt");

	if(in.is_open()) {
		in >> s;
		std::cout << "input string : " << s << std::endl;
	}
	else
	{
		std::cout << "file not found" << std::endl;
	}

	return 0;
}
