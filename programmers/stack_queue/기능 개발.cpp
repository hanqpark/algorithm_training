#include <string>
#include <vector>
#include <deque>

using namespace std;

vector<int> mySolution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    deque<int> dqP(progresses.begin(), progresses.end());
    deque<int> dqS(speeds.begin(), speeds.end());
    
    while (dqP.size()) {
        for (int i = 0; i < dqP.size(); ++i) {
            dqP[i] += dqS[i];
        }
        
        int ans = 0;
        while (dqP.size() && dqP.front() >= 100) {
            dqP.pop_front();
            dqS.pop_front();
            ++ans;
        }
        
        if (ans) {
            answer.emplace_back(ans);
        }
    }
    
    return answer;
}

vector<int> gptSolution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    vector<int> days;

    for (int i = 0; i < progresses.size(); ++i) {
        int remain = 100 - progresses[i];
        int day = (remain + speeds[i] - 1) / speeds[i];
        days.emplace_back(day);
    }

    int cur = days[0];
    int cnt = 1;
    for (int i = 1; i < days.size(); ++i) {
        if (days[i] <= cur) {
            ++cnt;
        } else {
            answer.push_back(cnt);
            cur = days[i];
            cnt = 1;
        }
    }
    answer.emplace_back(cnt);

    return answer;
}