#include<iostream>
#include<cmath>
#include<algorithm>
#include<string>
#include<queue>
#include<vector>

using namespace std;

priority_queue<int, vector<int>, greater<int>> card;

int main(){
    int n;
    
    cin >> n;
    
    for(int i = 0; i<n; i++){
        int a;
        
        cin >> a;
        
        card.push(a);
        
    }
    
    int count_sum = 0;
    
    for(int i =0; i< n-1; i++){
        int a, b;
        
        a = card.top();
        card.pop();
        b = card.top();
        card.pop();
        
        card.push(a+b);
        count_sum += (a+b);
    }
    
    cout << count_sum;
    
}
