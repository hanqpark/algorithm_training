#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string gptSolution(vector<int> numbers) {
    vector<string> strNum;
    
    for (const int& n: numbers) {
        strNum.push_back(to_string(n));
    }
    
    sort(strNum.begin(), strNum.end(), [](const string& a, const string& b) {
        return a+b > b+a;
    });
    
    string answer;
    for (const string& s: strNum) {
        answer += s;
    }
    
    return (strNum[0] == "0") ? "0" : answer;
}