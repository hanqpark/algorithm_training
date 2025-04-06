#include <string>
#include <vector>
#include <algorithm>

using namespace std;

/**
 * @brief sort -> O(k log k)
 * @param array 
 * @param commands 
 * @return vector<int> 
 */
vector<int> mySolution(vector<int> array, vector<vector<int>> commands) {
    vector<int> answer;
    
    for (const auto& cmd: commands) {
        vector<int> temp(array.begin() + (cmd[0] - 1), array.begin() + cmd[1]);
        sort(temp.begin(), temp.end());
        answer.push_back(temp[cmd[2] - 1]);
    }
    
    return answer;
}

/**
 * @brief nth_element -> 평균 O(k), 최악 O(k^2)
 * @param array 
 * @param commands 
 * @return vector<int> 
 */
vector<int> gptSolution(vector<int> array, vector<vector<int>> commands) {
    vector<int> answer;

    for (const auto& cmd: commands) {
        vector<int> temp(array.begin() + (cmd[0] - 1), array.begin() + cmd[1]);
        nth_element(temp.begin(), temp.begin() + (cmd[2] - 1), temp.end());
        answer.push_back(temp[cmd[2] - 1]);
    }

    return answer;
}