/**
 * @file encode and decode strings.cpp
 * @author hanqpark
 * @link https://neetcode.io/problems/string-encode-and-decode
 * @date 2025-02-27
 */

#include <string>
#include <vector>
#include <sstream>
#include <numeric>

using namespace std;

class Solution {
public:
    string myEncode(vector<string>& strs) {
        string answer;
        for (const string& str: strs) {
            answer += str;
            answer += "-";
        }
        return answer;
    }

    string bestEncode(vector<string>& strs) {
        string answer;
        answer.reserve(accumulate(strs.begin(), strs.end(), 0, [](int sum, const string& str) { 
            return sum + str.size() + 1; 
        }));

        for (const string& str : strs) {
            answer.append(str);
            answer.push_back('-');
        }
        return answer;
    }

    vector<string> myDecode(string s) {
        string str;
        stringstream ss(s);
        vector<string> answer;

        while (getline(ss, str, '-')) answer.push_back(str);

        return answer;
    }

    vector<string> bestDecode(string s) {
        vector<string> answer;
        size_t start = 0, end;
        
        while ((end = s.find('-', start)) != string::npos) {
            answer.emplace_back(s.substr(start, end - start));
            start = end + 1;
        }
        return answer;
    }
};
