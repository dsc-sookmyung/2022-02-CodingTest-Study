#include <iostream>
#include <algorithm>
#include <queue>
#include <vector>
#include <string>

using namespace std;

int main(){
    string str;
    
    cin >> str;
    
    queue<long long> q;
    
    for(int i = 0; i < str.length(); i++){
        q.push(str[i]-'0');
    }
    
    long long answer = 0;
    
    answer = q.front();
    q.pop();
    
    while (!q.empty()) {
        long long a = q.front();
        
        q.pop();
        
        if((answer + a) > (answer * a)){
            answer += a;
        }
        else{
            answer *= a;
        }
    }
    
    cout << answer;
    
}
