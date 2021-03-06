//문제: 회전판에 먹어야 할 N개의 음식이 있고 K초 후에 몇 번 음식 부터 먹으면 되는지 반환하는 문제
//1번 음식부터 음식번호가 증가하는 순서대로 음식을 먹는다. 마지막 번호 후에는 1번 음식을 먹는다.


#include <string>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

int solution(vector<int> food_times, long long k) {
    int answer = 0;
    
    priority_queue<pair<int, int>> priority_food_times;
    
    
    long long sum = 0;
    long long before = 0;
    
    for(int i= 0; i < food_times.size(); i++){
        sum += food_times[i];
        priority_food_times.push({-food_times[i], i+1});
    }
    
    // 더 이상 먹어야 할 음식이 없는 경우
    if(sum <= k){
        return -1;
    }
    
    while((-priority_food_times.top().first - before) * priority_food_times.size() <= k){
        k -= (-priority_food_times.top().first - before) * priority_food_times.size();
        before = -priority_food_times.top().first;
        priority_food_times.pop();
    }
    
    vector<pair<int, int>> times;
    
    while(!priority_food_times.empty()){
        times.push_back({priority_food_times.top().second, -priority_food_times.top().first});
        priority_food_times.pop();
    }
    
    sort(times.begin(), times.end());
    
    answer = times[k % times.size()].first;
    
    return answer;
}
