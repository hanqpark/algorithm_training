#include <string>
#include <vector>
#include <algorithm>

using namespace std;

/**
 * @brief O(n log n) + O(n)
 * 
 * @param citations 
 * @return int 
 */
int solution(vector<int> citations) {
    int answer = 0;
    
    sort(citations.rbegin(), citations.rend());
    
    for (int i = 0; i < citations.size(); ++i) {
        if (citations[i] < i+1)
            return i;
    }
    
    return citations.size();
}

/**
 * @brief O(n)
 * 
 * @param citations 
 * @return int 
 */
int solution(vector<int> citations) {
    int n = citations.size();
    vector<int> count(n+1, 0);

    for (int c: citations) {
        (c >= n) ? ++count[n] : ++count[c];
    }

    int total = 0;
    for (int i = n; i >= 0; --i) {
        total += count[i];
        if (total >= i)
            return i;
    }

    return 0;
}