/**
 * @file anagram groups.cpp
 * @author hanqpark
 * @link  https://neetcode.io/problems/anagram-groups
 * @date 2025-02-22
 */

#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<vector<string>> myAnswer(vector<string>& strs) {
        map<string, vector<string>> m;
        for (const string& str: strs) {
            string s = str;
            sort(s.begin(), s.end());
            m[s].push_back(str);
        }

        vector<vector<string>> answer;
        for (const auto& [key, value]: m) {
            answer.push_back(value);
        }

        return answer;
    }

    vector<vector<string>> bestAnswer(vector<string>& strs) {
        unordered_map<string, vector<string>> m;
        
        for (const string& str : strs) {
            string key = getAnagramKey(str);
            m[key].push_back(str);
        }

        vector<vector<string>> answer;
        answer.reserve(m.size());

        for (auto& [_, value] : m) {
            answer.push_back(move(value));
        }

        return answer;
    }

private:
    string getAnagramKey(const string& s) {
        array<int, 26> count = {0};
        for (char c : s) {
            count[c - 'a']++;
        }
        
        string key;
        key.reserve(52);
        for (int i = 0; i < 26; ++i) {
            if (count[i] > 0) {
                key += 'a' + i;
                key += to_string(count[i]);
            }
        }
        return key;
    }
};

int main() {
    Solution sol; // Solution 객체 생성

    vector<string> input = {"eat", "tea", "tan", "ate", "nat", "bat"};
    
    vector<vector<string>> result = sol.groupAnagrams(input);

    // 결과 출력
    cout << "[\n";
    for (const auto& group : result) {
        cout << "  [";
        for (size_t i = 0; i < group.size(); ++i) {
            cout << "\"" << group[i] << "\"";
            if (i != group.size() - 1) cout << ", ";
        }
        cout << "]\n";
    }
    cout << "]\n";

    return 0;
}