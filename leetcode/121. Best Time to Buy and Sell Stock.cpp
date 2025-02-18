/**
 * @file 121. Best Time to Buy and Sell Stock.cpp
 * @author hanqpark
 * @link https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description
 * @date 2025-02-18
 */

#include <vector>
#include <iostream>

using namespace std;

int maxProfit(vector<int>& prices) {
    int answer = 0;
    int maxi = -1;
    int mini = -1;

    for (const int price: prices) {
        if (mini == -1) {
            mini = price;
        } else if (mini > price) {
            if (maxi != -1) {
                answer = max(answer, maxi-mini);
            }
            maxi = -1;
            mini = price;
        } else {
            maxi = max(price, maxi);
        }
    }
    return max(answer, maxi-mini);
}

int bestAnswer(vector<int>& prices) {
    int a = prices.back();
    int ans = 0;
    for(int i=prices.size()-2;i>=0;i--){
        a = max(a,prices[i]);
        ans = max(a-prices[i],ans);
    }
    return ans;
}

int main() {
    vector<int> temp = {7,1,5,3,6,4};
    auto answer = maxProfit(temp);
    cout << answer << endl;

    return 0;
}