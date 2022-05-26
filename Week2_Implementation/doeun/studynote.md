## 구현
```
'머리속에 있는 알고리즘을 소스코드로 바꾸는 과정'
```

- 완전 탐색: 모든 경우의 수를 다 계산하는 해결 방법
- 시뮬레이션: 문제에서 제시한 알고리즘을 한 단계씩 차례대로 직접 수행해야 하는 문제 유형

### 예제1) 시각
- 문제: 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램
- 해설: 모든 시각의 경우를 세서 푼다.
``` c++
#include <iostream>

using namespace std;

int main() {

	int answer = 0;
	int n;
  
	cin >> n;
  
	for (int i = 0; i <= n; i++) {
  
		if (i == 3 || i == 13 || i == 23) {
			answer += 3600;
			continue;
		}
    
		answer += 1575;
	}
  
	cout << answer;
}
```

### 예제2) 왕실의 나이트
- 문제: 나이트의 위치가 주어졌을 때 나이트가 이동할 수 있는 경우의 수
- 해설: 나이트가 이동할 수 있는 경로를 하나씩 확인하며 이동한다.
``` c++
#include <iostream>
#include <string>

using namespace std;

int dx[8] = {-2, -2, -1, 1, 2,  2, 1, -1};
int dy[8] = {-1, 1, 2, 2, -1, 1, -2, -2};

int main() {

	int answer = 0;

	string str;
	cin >> str; 
  
	int x = (str[1]-'0') -1; 
	int y = str[0] - 'a';

	for (int i = 0; i < 8; i++) {
  
		int xx = x + dx[i];
		int yy = y + dy[i];
    
		if (xx < 0 || xx >7 || yy < 0 || yy >7){
			continue;
    }
		else{
			answer++;
    }
    
	}
  
	cout << answer;
}
```

### 예제3) 게임 개발
- 문제: 캐릭터가 상하좌우로 움직일 수 있고 바다로 되어 있는 공간에는 갈 수 없다. 게임 메뉴얼 대로 수행한 후 캐릭터가 방문한 칸의 수를 구하는 문제
- 해설: 시뮬레이션 문제로 문제에서 요구하는 내용을 구현하면 된다.
``` c++ 
#include <iostream>

using namespace std;

int map[50][50];

int dx[4] = { -1, 1, 0, 0 };
int dy[4] = {0, 0, 1,  -1 };

int main() {
	
  int move = 1;
	int m, n, x, y, d;
  
	cin >> m >> n; 
	cin >> x >> y >> d;
	
  for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cin >> map[i][j];
		}
	}

	while (1) {
		map[x][y] = 1;
		for (int i = 1; i <= 4; i++) {
    
			int dd = (d + i) % 4;
      
			int xx = x + dx[dd];
			int yy = y + dy[dd];
      
			if (xx >= 0 && yy >= 0 && xx < n && yy < m && map[xx][yy] == 0) { 
				d = dd;
				x = xx; 
        y = yy;
        
				move++;
				break; 
			}
			if (i == 4) {
				d = dd;
				dd = (dd + 2) % 4; 
        
				xx = x + dx[dd];
				yy = y + dy[dd];
        
				if ( xx >= 0 && yy >= 0 && xx < n && yy < m && map[xx][yy] == 1) { 
					cout << move;
          
					return 0;
				}
				else { 
					x = xx;
          y = yy;
          
					move++;
				}
			}
		}

	}
}
```
