#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int ball[11];

int main(){
    int n, m;
    
    cin >> n >> m;
    
    for(int i = 0; i < n; i++){
        int a;
        
        cin >> a;
        
        ball[a]++;
    }
    
    int result = 0;
    
    for(int i = 1; i <= m; i++){
        n -= ball[i];
        result += ball[i] * n;
    }
    
    cout << result;
}
