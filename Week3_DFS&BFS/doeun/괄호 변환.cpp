#include <string>
#include <vector>
#include <stack>

using namespace std;

bool check(string p) {
    stack<char> st;
    
    for(auto c : p) {
        // 왼쪽 괄호 문자열일 경우, 스택에 넣고 오른쪽 괄호 문자열일 경우, 스택에 있는 골호를 꺼낸다.
        // 단, 괄호가 비어있을 경우, false를 반환한다.
        if(c == '('){
            st.push(c);
        } 
        else {
            if(st.empty()){
                return false;
            }
            
            st.pop();
        }
    }
    
    // 스택이 비어있을 경우, 올바른 문자열이므로 true를 반환하도록 하고
    // 스택이 비어있지 않을 경우, 올바르지 않은 문자열이므로 false를 반환한다.
    return st.empty();    
}

string solution(string p) {
    // 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환한다.
    if(p.empty()){
        return p;
    }
    string answer = "";
    
    string u = "";
    string v = "";
    
    int l = 0, r = 0;
    
    // 2. 균형잡힌 괄호 문자열 u, v로 분리
    for(int i = 0; i < p.length(); i++) {
        if(p[i] == '(') {
            l++;
        }
        else {
           r++; 
        }
        
        if(l == r) {
            u = p.substr(0, i+1);
            v = p.substr(i+1);
            break;
        }
    }
    
    // 3. 올바른 문자열일 경우, 문자열 v에 대해 1단계 부터 수행한 문자열을 u에 이어 붙인다.
    if(check(u)){
        answer = u + solution(v);
    }
    // 4. 올바른 괄호 문자열이 아닐 경우, 
    else {
        // 4-1. 빈 문자열에 첫 번째 문자로 ( 를 붙인다.
        // 4-2. 문자열 v에 대해 1단계 부터 수행한 문자열을 이어 붙인다.
        // 4-3. ) 를 다시 붙인다.
        answer = "(" + solution(v) + ")";
        
        // 4-4. u의 첫 번째와 마지막 문자를 제거해야 하므로 i를 1부터 확인하도록 하고 
        // (u의 길이 - 1) 보다 작은 i 만 확인한다.
        for(int i=1; i < u.length()-1; i++) {
            // 나머지 문자열의 괄호 방향을 뒤집어서 붙인다. 
            if(u[i] == '('){
                answer += ')';
            }
            else{
                answer += '(';
            }
        }
    }
    
    // 4-5. 생성된 문자열을 반환한다.
    return answer;
}
