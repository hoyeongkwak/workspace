#include <iostream>
#include <fstream>
#include <string>

int main() {
	std::ifstream in("test.txt");
	std::string s;

	if(in.is_open()) 
	{
		in >> s;
		std::cout << "input string : " << s << std::endl;
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
