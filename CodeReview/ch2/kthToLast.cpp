#include <iostream>
using namespace std; 

struct Node{
	int data;
	Node * next;
	Node(int d) : data{ d }, next{nullptr}{ }
};

void insert(Node * &head, int data){
	Node * newNode = new Node(data);
	newNode->next = head;
	head = newNode;
}

void deleteList(Node * &head){
	Node * nextNode;
	while(head){
		 nextNode = head->next;
		 delete(head);
		 head = nextNode;
	}
}

void printList(Node * head){
	while(head){
		cout << head->data << "-->";
		head = head->next;
	}
	cout << "null" << endl;
}

Node * kthToLastHelper(Node * head, int k, int & i){
	if(head == nullptr){
		return nullptr;
	}

	Node * node = kthToLastHelper(head->next, k, i);
	i = i + 1;
	if(i == k){
		return head;
	}
	return node;
}

Node * kthToLastRecursive(Node * head, int k){
	int i = 0;
	return kthToLastHelper(head, k, i);
}

Node * kthToLastIterative(Node * head, int k){
	if(head == nullptr){
		return head;
	}

	Node * ptr1 = head;
	Node * ptr2 = head;

	int i = 0;
	while(i < k && ptr1){
		ptr1 = ptr1->next;
		++i;
	}

	if(i < k){
		return nullptr;
	}

	while(ptr1 != nullptr){
		ptr1 = ptr1->next;
		ptr2 = ptr2->next;
	}

	return ptr2;
}

int main(){
	Node * head = nullptr;
	for(int i = 7; i > 0; i--){
		insert(head, i);
	}

	cout << "List: ";
	printList(head);

	cout << "4th ndoe from last (Recursive) : ";
	Node *node4 = kthToLastRecursive(head, 4);
	if(node4 != nullptr){
		cout << node4->data << endl;
	}else{
		cout << "NULL MODE\n";
	}

	cout << "4th node from last (Iterative) : ";
	node4 = kthToLastIterative(head, 4);
	if(node4 != nullptr){
		cout << node4->data << endl;
	}else{
		cout << "NULL MODE\n";
	}

	deleteList(head);

	return 0;
}


