#include <iostream>
#include <string>

int main() {
	std::string s = "abc";
	std::string t = "def";
	std::string s2 = s;

	std::cout << s << " length : " << s.length() << std::endl;
	std::cout << s << "back " << t << " paste : " << s + t << std::endl;

	if(s == s2)
	{
		std::cout << s << " and " << s2 << " same " << std::endl;
	}
	if(s != t)
	{
		std::cout << s << " and " << t << " different" << std::endl;
	}
	return 0;
}
