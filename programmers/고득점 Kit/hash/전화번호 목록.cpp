#include <string>
#include <vector>
#include <algorithm>

using namespace std;

/**
 * @brief O(n^2) Solution
 * 
 * @param book 
 * @return true 
 * @return false 
 */
bool mySolution(vector<string> book) {
    bool answer = true;
    sort(book.begin(), book.end(), [](const string& a, const string& b) {
        return a.size() < b.size();
    });
    
    for (int i = 0; i < book.size(); ++i) {
        const string prefix = book[i];
        for (int j = i+1; j < book.size(); ++j) {
            const string full = book[j];
            if (equal(prefix.begin(), prefix.end(), full.begin()))
                return false;
        }
    }
    
    return true;
}

/**
 * @brief O(N log N) + O(N * L) 
 * 
 * @param book 
 * @return true 
 * @return false 
 */
bool gptSolution(vector<string> book) {
    sort(book.begin(), book.end());

    for (size_t i = 0; i+1 < book.size(); ++i) {
        const string& cur = book[i];
        const string& next = book[i+1];

        if (next.compare(0, cur.size(), cur) == 0)
            return false;
    }

    return true;
}