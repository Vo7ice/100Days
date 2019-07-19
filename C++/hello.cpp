#include <iostream>
#include <stdlib.h>
#include <string.h>
using namespace std;

int main() {
    cout<<"Hello World!"<<endl;

    /* string s1, s2;
    cin >> s1 >> s2;
    cout << s1 << s2 << endl;

    string line; */

    /* while (getline(cin, line))
    {
        if (line.empty())
        {
            cout << "This is empty!" << endl;
            break;
        }
        else
        {
            cout << line << endl;
        }
        
    } */
    
    int i = 42;
    int *pi = &i;
    *pi = *pi * *pi;
    cout << *pi << endl;

    // i = 42;
    int &r1 = i;
    const int &r2 = i;// r2 point to the address for i;
    cout << &r2 << endl;
    cout << r2 <<endl;

    system("pause");
    return 0;
}