/**
 * @file Top K Frequenct Elements.cpp
 * @author hanqpark
 * @link https://neetcode.io/problems/top-k-elements-in-list
 * @date 2025-02-24
 */

#include <vector>
#include <unordered_map>
#include <queue>
#include <algorithm>
#include <iostream>

using namespace std;

class Solution {
public:
    vector<int> myAnswer(vector<int>& nums, int k) {
        unordered_map<int, int> m;
        for (const int& n: nums) {
            ++m[n];
        }

        vector<pair<int, int>> v(m.begin(), m.end());

        sort(v.begin(), v.end(), [](const pair<int, int>& a, const pair<int, int>& b) { return a.second > b.second; });

        int flag = 0;
        vector<int> sortedKeys;
        for (const auto& [key, val]: v) {
            if (flag++ == k) break;
            sortedKeys.push_back(std::move(key));
        }

        return sortedKeys;
    }

    vector<int> bestAnswer(vector<int>& nums, int k) {
        unordered_map<int, int> freqMap;
        for (const int& num : nums) {
            ++freqMap[num];
        }

        // Min-Heap (최소 힙) 사용하여 상위 K개만 유지
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> pq;
        
        for (const auto& [num, freq] : freqMap) {
            pq.push({freq, num});  // 힙에 (빈도, 숫자) 저장
            if (pq.size() > k) pq.pop(); // k개 초과 시 가장 작은 빈도를 제거
        }

        // 최종 k개의 요소를 결과 벡터에 저장
        vector<int> result;
        while (!pq.empty()) {
            result.push_back(pq.top().second);
            pq.pop();
        }

        reverse(result.begin(), result.end()); // 높은 빈도 순으로 정렬

        return result;
    }
};


int main() {
    Solution sol;

    vector<int> v = {1,2,2,3,3,3};
    int k = 2;

    for (const auto& i: sol.myAnswer(v, k))
        cout << i << " ";
    cout << endl;
    return 0;
}