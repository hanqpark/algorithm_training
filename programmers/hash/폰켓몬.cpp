/**
 * @file 폰켓몬.cpp
 * @author hanqpark
 * @link https://school.programmers.co.kr/learn/courses/30/lessons/1845
 * @date 2025-04-04
 */

#include <vector>
#include <unordered_set>

using namespace std;

int solution(vector<int> nums)
{   
    unordered_set<int> uset(nums.begin(), nums.end());

    return nums.size()/2 < uset.size() ? nums.size()/2 : uset.size();
}