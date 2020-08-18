#include <iostream>
#include <fstream>
#include <string>

int main()
{
	std::ofstream out("test.txt", std::ios::app);
	std::ofstream out2("test2.txt", std::ios::ate);

	out.seekp(3, std::ios::beg);
	out2.seekp(3, std::ios::beg);

	out << "add";
	out2 << "add";
	
	return 0;
}
