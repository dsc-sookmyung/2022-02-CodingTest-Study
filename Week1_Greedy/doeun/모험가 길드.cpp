#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> people;

int main(){
    int n;
    
    cin >> n;
    
    for(int i = 0; i< n; i++){
        int a;
        
        cin >> a;
        
        people.push_back(a);
    }
    
    sort(people.begin(), people.end());
    
    int count = 0;
    int answer = 0;
    
    for(int i = 0; i < people.size(); i++){
        count++;
        if(count >= people[i]){
            answer++;
            count = 0;
        }
    }
    
    cout << answer;
}
