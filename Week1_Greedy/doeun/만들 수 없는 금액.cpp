#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int>coin;

int main(){
    int n;
    
    cin >> n;
    
    for(int i = 0; i < n; i++){
        int a;
        
        cin >> a;
        
        coin.push_back(a);
    }
    
    sort(coin.begin(), coin.end());
    
    int check = 1;
    
    for(int i = 0; i < n; i++){
        if(check < coin[i]){
            break;
        }
        check += coin[i];
    }
    
    cout << check;
}
