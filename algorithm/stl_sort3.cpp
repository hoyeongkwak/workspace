#include <iostream>
#include <algorithm>

using namespace std;

class Student{
	public:
		string name;
		int score;
		Student(string name, int score){
			this->name = name;
			this->score = score;
		}
		bool operator < (Student &student){
			return this->score < student.score;
		}
};

bool compare(int a, int b){
	return a > b;
}

int main(void){
	Student students[] = {
		Student("A", 90),
		Student("B", 92),
		Student("C", 99),
		Student("D", 70),
		Student("E", 88)
	};
	sort(students, students+5);
	for(int i = 0; i < 5; i++){
		cout << students[i].name << ' ';
	}
	cout << endl;
}
