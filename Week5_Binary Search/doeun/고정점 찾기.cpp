#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

vector<int> points;

int main(){
    int n;
    
    cin >> n;
    
    for(int i = 0; i < n; i++){
        int a;
        
        cin >> a;
        
        points.push_back(a);
    }
    
    int left = 0, right = n-1;
    
    while(left <= right){
        int mid = (left + right) / 2;
        
        if(points[mid] == mid){
            cout << mid;
            return 0;
        }
        
        if(points[mid] > mid ){
            right = mid - 1;
        }
        else{
            left = mid + 1;
        }
    }
    
    cout << -1;
}
