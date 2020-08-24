#include <iostream>

using namespace std;

int number = 15;

// 하나의 노드 정보를 선언한다.
typedef struct node *treePointer;
typedef struct node {
	int data;
	treePointer leftChild, rightChild;
}node;

//전위 순회
void preorder(treePointer ptr){
	if(ptr){
		cout << ptr->data << ' ';
		preorder(ptr->leftChild);
		preorder(ptr->rightChild);
	}
}

//중위 순회
void inorder(treePointer ptr){
	if(ptr){
		preorder(ptr->leftChild);
		cout << ptr->data << ' ';
		preorder(ptr->rightChild);
	}
}

//후위 순회
void postorder(treePointer ptr){
	if(ptr){
		preorder(ptr->leftChild);		
		preorder(ptr->rightChild);
		cout << ptr->data << ' ';
	}
}

int main(void){
	node nodes[number + 1];
	for(int i = 1; i <= number; i++){
		nodes[i].data = 1;
		  nodes[i].leftChild = NULL;
		  nodes[i].rightChild = NULL;
	}
	for(int i = 1; i <= number; i++){
		if(i % 2 == 0)
			nodes[i / 2].leftChild = &nodes[i];
		else
			nodes[i / 2].rightChild = &nodes[i];
	}
	preorder(&nodes[1]);
	return 0;
}