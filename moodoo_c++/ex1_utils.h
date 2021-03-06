#ifndef UTILS_H
#define UTILS_H

#include <string>
#include <cstdlib>
#include <algorithm>
#include <fstream>
using std::string;
using std::max;

namespace MyExcel{
	class Vector{
		string* data;
		int capacity;
		int length;
		
		public:
			Vector(int n = 1);
			void push_back(string s);
			string operator[] (int i );
			void remove(int x);
			int size();
			~Vector();
	};
	class Stack{
		struct Node {
			Node* prev;
			string s;
			
			Node(Node* prev, string s) : prev(prev), s(s) {}
		};
		
		Node* current;
		Node start;
		
		public:
			Stack();			
			void push(string s);
			string pop();
			string peek();
			bool is_empty();
			~Stack();
	};
	class NumStack{
		struct Node{
			Node* prev;
			double s;
			
			Node(Node* prev, double s) : prev(prev), s(s) {}
		};
		
		Node* current;
		Node start;
		
		public:
			NumStack();
			void push(double s);
			double pop();
			double peak();
			bool is_empty();
			
			~NumStack();
	};
	class Cell;
	class Table {
		protected:
			int max_row_size, max_col_size;
			Cell*** data_table;
			
		public:
			Table(int max_row_size, int max_col_size);
			~Table();

			void reg_cell(Cell* c, int row, int col);
			
			//select cell value return
			int to_numeric(const string& s);
			
			// select row and col number return
			int to_numeric(int row, int col);

			string stringify(const string& s);
			string stringify(int row, int col);

			virtual string print_table() = 0;
	};
	class Cell {
       protected:
           int x, y;
           Table* table;
  
           string data;
  
       public:
           virtual string stringify();
           virtual int to_numeric();
  
           Cell(string data, int x, int y, Table* table);
   };
	
	class TxtTable : public Table {
		string repeat_char(int n, char c);
		
		string col_num_to_str(int n);
		
		public:
		TxtTable(int row, int col);
		string print_table();
	};
}
#endif
