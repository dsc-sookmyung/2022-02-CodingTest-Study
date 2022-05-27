## 그리디 알고리즘

그리디 알고리즘은 **탐욕법**이라이라 불리우는 것으로 "현재 상황에서 지금 당장 좋은 것만을 고르는 방법"을 의미한다.
```
- 가장 큰 순서대로
- 가장 작은 순서대로
```

### 예제1) 거스름돈

문제: 카운터에서 거스름돈으로 500원, 100원, 50원, 10원짜리 동전이 무한히 존재할 때 N원을 거스러줄 경우, 가장 적은 동전의 개수로 거스름돈을 거슬러 줄 때 거스름 돈으로 주는 동전의 개수.
<br />
해설: 가장 큰 화폐 단위부터 거슬러 준다. 
정당성: 큰 단위가 작은 단위의 배수의 형태이기 떄문에 '가장 큰 단위의 화폐부터 가장 작은 단위의 화폐까지 차례대로 확인하여 거슬러 주면 된다'

``` c++
#include "iostream"

using namespace std;

int coin[4] = {500, 100, 50, 10};

int main(){
    
    int n, cnt = 0;
    
    cin >> n;
    
    for(int i = 0; i< 4; i++){
        
        cnt += (n / coin[i]);
        
        n %= coin[i];
    }
    
    cout << cnt;
}

```
### 예제 2) 큰 수의 법칙

문제: 다양한 수로 이루어진 배열에서 주어진 수들을 M번 더하여 가장 큰 수를 만들려고 할 때, 배열의 특정한 인덱스에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없도록 해야 한다. 이 때 나올 수 있는 가장 큰 수.
<br />
해설: 가장 큰 수와 두 번째로 큰 수를 저장하고 가장 큰 수를 K번 더하고 두 번째로 큰 수를 한 번 더하는 연산을 반복한다.

``` c++
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main(){
    
    int n, m,  k;
    vector<int> v;
    
    cin >> n >> m >> k;
    
    for(int i = 0; i< n; i++){
        int a;
        
        cin >> a;
        
        v.push_back(a);
    }
    
    sort(v.begin(), v.end());
    
    int max1 = v[n-1];
    int max2 = v[n-2];
    
    int sum = 0;
    
    int cnt = (m/(k+1))*k;
    cnt += m % (k+1);
    
    sum += (cnt * max1);
    sum += ((m-cnt)* max2);
    
    cout << sum;
    
}

```

### 예제3) 숫자 카드 게임
문제: 여러개의 숫자 카드 중 가장 높은 숫자가 쓰인 카드 한장을 뽑는 문제. 뽑고자 하는 카드가 포함되어 있는 행을 선택하여 선택한 행에 포함되어 있는 카드들 중 숫자가 가장 낮은 카드를 뽑아야 한다. 
<br />
해설: 각 행마다 가장 작은 수를 찾은 뒤 이 수들 중 가장 큰 수

``` c++
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
    int n, m;
    vector<vector<int>> card;
    vector<int> v;
    
    cin >> n >> m;
    
    for(int i = 0; i< n; i++){
        card.push_back(v);
    }
    
    for(int i = 0; i< n; i++){
        for(int j = 0; j < m; j++){
            int a;
            
            cin >> a;
            
            card[i].push_back(a);
        }
    }
    
    int max = 0;
    
    for(int i = 0; i < n; i++){
        sort(card[i].begin(), card[i].end());
        if(max < card[i][0]){
            max = card[i][0];
        }
    }
    
    cout << max;
    
}
```

### 예제4) 1이 될 때까지
문제: 어떤 수 n이 1이 될 때까지 두 과정 중 하나를 반복적으로 선택하여 수행하려 할 때 1번 혹은 2번의 과정을 수행해야 하는 최소 횟수
1. N에서 1을 뺀다.
2. N을 K로 나눈다. (N이 K로 나누어 떨어질 때만 선택 가능)
해설: '최대한 많이 나누기를 수행하도록 한다.' N이 K의 배수가 될 때까지 1씩 빼고 N을 K로 나누는 횟수를 구하여 해결한다.

``` c++
#include <iostream>

using namespace std;

int main(){
    int n, k, cnt = 0;
    
    cin >> n >> k;
    
    while(n != 1){
        if(n >= k){
            cnt += (n%k);
            n -= (n %k);
        }else{
            cnt += (n % k - 1);
            break;
        }
        
        
        if(n >= k){
            n /= k;
            cnt ++;
        }
    }
    
    cout << cnt;
}

```



