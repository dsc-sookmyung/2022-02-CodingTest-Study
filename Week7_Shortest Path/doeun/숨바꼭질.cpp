#include <iostream>
#include <algorithm>
#include <queue>
#include <vector>

using namespace std;

int n, m;
int dist[20001];

vector<int> mapp[20001];

void dijkstra() {
    
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    
    pq.push({1, 0});
    dist[1] = 0;

    while(!pq.empty()) {
        
        int cur = pq.top().first;
        int cost = pq.top().second;
        
        pq.pop();

        if (dist[cur] < cost){
            continue;
        }
        
        for (const int& itr : mapp[cur]){
            if (dist[itr] > cost + 1) {
                dist[itr] = cost + 1;
                pq.push({itr, cost + 1});
            }
        }
    }
}


int main() {
    
    cin >> n >> m;
    
    for (int i = 0; i < m; ++i) {
        
        int a, b;
        cin >> a >> b;
        
        mapp[a].push_back(b);
        mapp[b].push_back(a);
    }
    
    fill(dist + 1, dist + n + 1, 1e9);
    
    dijkstra();
    
    auto itr = max_element(dist + 1, dist + n + 1);
    
    int answer = *itr;
    int hidePlace = itr - dist;
    int cnt = 0;
    
    for (int i = 1; i <= n; ++i){
        if ( mapp[i] == answer ){
            cnt++;
        }
    }
    cout << hidePlace << ' ' << answer << ' ' << cnt << '\n';
}
