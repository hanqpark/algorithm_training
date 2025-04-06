#include <string>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

int mySolution(vector<int> scoville, int K) {
    priority_queue<int, vector<int>, greater<int>> pq(scoville.begin(), scoville.end());
    
    int answer = 0;
    while (pq.size() >= 2) {
        int min1 = pq.top(); pq.pop();
        if (min1 >= K) return answer;
        
        int min2 = pq.top(); pq.pop();
        pq.push(min1 + 2 * min2);
        ++answer;
    }
    
    if (!pq.empty() && pq.top() >= K)
        return answer;
    
    return -1;
}

int gptSolution(vector<int> scoville, int K) {
    priority_queue<int, vector<int>, greater<int>> pq(scoville.begin(), scoville.end());

    int answer = 0;
    while(pq.size() >= 2 && pq.top() < K) {
        int min1 = pq.top(); pq.pop();
        int min2 = pq.top(); pq.pop();
        pq.push(min1 + 2 * min2);
        ++answer;
    }

    return (pq.top() >= K) ? answer : -1;
}