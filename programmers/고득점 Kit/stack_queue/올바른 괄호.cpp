#include <string>
#include <iostream>
#include <vector>

using namespace std;

bool mySolution(string s)
{
    vector<char> vowel;
    
    for (const char& ch: s) {
        if (ch == '(') {
            vowel.emplace_back(ch);
        } else if (ch == ')' && !vowel.empty()) {
            vowel.pop_back();
        } else {
            return false;
        }
    }
    
    return vowel.empty();
}

bool gptSolution(string s) {

    int left = 0;

    for (const char& ch: s) {
        if (ch == '(') {
            ++left;
        } else {
            if (left == 0) return false;
            --left;
        }
    }

    return left == 0;
}