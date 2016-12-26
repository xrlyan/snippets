#include<stdio.h>
#include<iostream>
using namespace std;

class base{
	int a;
	public:
	       //  void fun(){ // could run through
	       virtual void fun(){ // segfault error
		 printf("base fun and a = %d, \n");
		}
};


int main(){
	    base *b=NULL;
	    b->fun();
}
