/**
 * @file longest consecutive sequence.cpp
 * @author hanqpark
 * @link https://neetcode.io/problems/longest-consecutive-sequence
 * @date 2025-03-05
 */

#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>

using namespace std;

class Solution {
public:
    int myLongestConsecutive(vector<int>& nums) {
        unordered_map<int, int> um;
        countingSort(nums);

        for (const int& n: nums) {
            if (um[n-1]) {
                um[n] = um[n-1]+1;
            } else {
                um[n] = 1;
            }
        }

        int answer = 0;
        for (const auto [_, v]: um) {
            answer = answer > v ? answer : v;
        }

        return answer;
    }

    int bestLongestConsecutive(vector<int>& nums) {
        unordered_set<int> numSet(nums.begin(), nums.end()); // O(n)

        int longest = 0;
        for (const int& num : numSet) {
            // 이전 숫자가 없으면 새로운 시퀀스 시작
            if (numSet.find(num - 1) == numSet.end()) {
                int currentNum = num;
                int currentStreak = 1;

                // 연속된 숫자가 존재하는지 확인
                while (numSet.find(currentNum + 1) != numSet.end()) {
                    currentNum += 1;
                    currentStreak += 1;
                }

                longest = max(longest, currentStreak);
            }
        }
        return longest;
    }

private:
    void countingSort(vector<int>& nums) {
        if (nums.empty()) return;

        // 1. 최댓값, 최솟값 찾기
        int minVal = *min_element(nums.begin(), nums.end());
        int maxVal = *max_element(nums.begin(), nums.end());
        int range = maxVal - minVal + 1;

        // 2. 카운트 배열 생성
        vector<int> count(range, 0);

        // 3. 각 숫자의 빈도 계산
        for (int num : nums) {
            count[num - minVal]++;
        }

        // 4. 정렬된 결과를 원본 벡터에 복사
        int index = 0;
        for (int i = 0; i < range; ++i) {
            while (count[i]-- > 0) {
                nums[index++] = i + minVal;
            }
        }
    }
};
    