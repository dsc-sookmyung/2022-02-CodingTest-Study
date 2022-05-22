#include <iostream>
#include <string>

using namespace std;

int main(){
    string str;
    int answer = 0;
    
    cin >> str;
    
    for(int i = 1; i < str.length(); i++ ){
        if(str[i-1] != str[i]){
            answer++;
        }
    }
    
    cout << (answer+1)/2 << "\n";
}
