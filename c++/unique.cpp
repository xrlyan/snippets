#include  <iostream>
#include <string>
#include <map>
#include <algorithm>
using namespace std;

bool isunique(string);

void sort(string);

int main( int argc,char* argv[] )
{
  cout << "There is total " << argc << " arguments "<<endl;
  cout << argv[0] << endl;
  
  char line[] = "this is a test line for string";
  string stringline2("this is a test line for string");
  string stringline(line);
  cout << line << sizeof(line)  << endl;
  cout << stringline << stringline.size() << endl;
  //cout << stringline2[0] << stringline2.size() << endl;

  if(isunique(stringline))
    	cout << "This is  a unique string!"<<endl;
  else
    	cout << "This is not a unique string!"<<endl;

  sort(stringline);

  return 0;
}

bool isunique1(string stringline)
{
  cout << stringline << endl;
  bool unique = true;
  int stringsize = stringline.size();
  for(int i=0;i< stringsize;i++)
    for(int j=i;j<stringsize;j++){
      if(stringline[i] == stringline[j]){
	unique = false;
	break;
      }
    }
  return unique;
}


void sort(string stringline)
{
  sort(stringline.begin(),stringline.end());
  cout << stringline<< endl;
}

bool isunique(string stringline)
{
  bool unique = true;
  cout << stringline << endl;
  int stringsize = stringline.size();
  map<char,int>container;
  for(int i=0;i<stringsize;i++){
    if(container[stringline[i]])
      unique = false;
    else
      container[stringline[i]]+=1;
  }
  
  return unique;

}
