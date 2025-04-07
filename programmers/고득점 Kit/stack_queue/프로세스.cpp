#include <string>
#include <vector>
#include <deque>
#include <queue>

using namespace std;

/**
 * @brief O(n log n) ~ O(n^2) 사이
 * 
 * @param priorities 
 * @param location 
 * @return int 
 */
int mySolution(vector<int> priorities, int location) {
    int answer = 0;
    deque<int> dq(priorities.begin(), priorities.end());
    priority_queue<int, vector<int>> pq(priorities.begin(), priorities.end());
    
    while (true) {
        int temp = dq.front(); dq.pop_front();
        if (temp != pq.top()) {
            dq.push_back(temp);
            if (location == 0) {
                location = dq.size()-1;
            } else {
                --location;
            }
        } else {
            pq.pop(); ++answer;
            if (location == 0) {
                return answer;
            } else {
                --location;
            }
        }
    }
    
    return answer;
}

int gptSolution(vector<int> priorities, int location) {
    queue<pair<int, int>> q;
    priority_queue<int> pq;

    for (int i = 0; i < priorities.size(); ++i) {
        q.push({i, priorities[i]});
        pq.push(priorities[i]);
    }

    int answer = 0;
    while (!q.empty()) {
        int idx = q.front().first;
        int pri = q.front().second;
        q.pop();

        if (pri < pq.top()) {
            q.push({idx, pri});
        } else {
            ++answer;
            pq.pop();
            if (idx == location) return answer;
        }
    }
}
