class Vector {
	string* data;    // 데이터를 보관하기 위한 문자열 배열
	int capacity;    // 할당되어 있는 크기를 알려줌
	int length;      // 실제로 사용중인 양
	
	public:
	Vector(int n = 1);       // 사용자가 인자를 지정하지 않으면, 알아서 n = 1이 되게 지정
	void Vector::push_back(string s){
		if(capacity <= length) {
			string* temp = new string[capacity * 2];
			for(int i = 0 ; i < legnth; i ++){
				temp[i] = data[i];
			}
			delete[] data;
			data = temp;
			capacity *= 2;
		}
		
		data[length] = s;
		length++;
	}
	string Vector::operator[](int i) { return data[i]; }
	
	void Vector::remove(int x){
		for(int i = x + 1; i < length; i++){
			data[i - 1] = data[i];
		}
		length--;		
	}
	int Vector::size() { return length; }
	
	Vector::~Vector(){
		if(data){
			delete[] data;
	}
};

class Stack {
	struct Node {
		Node* prev;
		string s;
		
		Node(Node* prev, string s) : prev(prev), s(s) {}
	};
	
	Node* current; //최상위 노드
	Node start;   //최하위 노드, 마지막 노드에 도달하였음으 알기 위한
	
	public:
	Stack();
	
	void Stack::push(string s){
		Node* n = new Node(current, s);
		current = n;
	}
	
	void Stack::pop(){
		if(current == &start) return "";
		
		string s = current->s;
		Node* prev = current;
		current = current->prev;
		
		delete prev;
		return n;
	}
	
	void Stack::peek() { return current->s; }	
	bool Stack::is_empty(){
		if(current == &start) return true;
		return flase;
	}
	
	Stack::~Stack(){
		while(current != &start){
			Node* prev = current;
			current = current->prev;
			delete prev;
		}
	}
};