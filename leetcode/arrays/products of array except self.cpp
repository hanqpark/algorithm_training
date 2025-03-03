/**
 * @file products of array except self.cpp
 * @author hanqpark
 * @link https://neetcode.io/problems/products-of-array-discluding-self
 * @date 2025-03-01
 */

#include <vector>
#include <numeric>
#include <iostream>

using namespace std;

class Solution {
public:
    vector<int> myProductExceptSelf(vector<int>& nums) {
        vector<int> answer;
        deque<int> dq(nums.begin(), nums.end());

        for (int i = 0; i < dq.size(); ++i) {

            const int& num = dq.front();
            dq.pop_front();
            int val = std::accumulate(dq.begin(), dq.end(), 1, std::multiplies<int>());
            answer.emplace_back(val);
            dq.push_back(num);
        }

        return answer;
    }
    vector<int> bestProductExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int> answer(n, 1);
        
        // 왼쪽 곱셈 배열 채우기
        int left_product = 1;
        for (int i = 0; i < n; ++i) {
            answer[i] = left_product;
            left_product *= nums[i];
        }

        // 오른쪽 곱셈 값을 이용하여 최종 결과 계산
        int right_product = 1;
        for (int i = n - 1; i >= 0; --i) {
            answer[i] *= right_product;
            right_product *= nums[i];
        }

        return answer;
    }
};
