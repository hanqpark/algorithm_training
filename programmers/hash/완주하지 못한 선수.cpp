/**
 * @file 완주하지 못한 선수.cpp
 * @author hanqpark
 * @link https://school.programmers.co.kr/learn/courses/30/lessons/42576 
 * @date 2025-04-04
 */

#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

string mySolution(vector<string> participant, vector<string> completion) {
    unordered_map<string, int> umap;
    
    for (const string& p: participant)
        umap[p]++;
    
    for (const string& c: completion)
        umap[c]--;
    
    for (const auto& pair: umap) {
        if (pair.second == 1) {
            return pair.first;
        }
    }
}

string gptSolution1(vector<string> participant, vector<string> completion) {
    unordered_map<string, int> umap;

    for (const auto& p : participant)
        ++umap[p];

    for (const auto& c : completion)
        --umap[c];

    for (const auto& [name, count] : umap) {
        if (count > 0)
            return name;
    }

    return "";
}

string gptSolution2(vector<string> participant, vector<string> completion) {
    sort(participant.begin(), participant.end());
    sort(completion.begin(), completion.end());

    for (int i = 0; i < completion.size(); ++i) {
        if (participant[i] != completion[i])
            return participant[i];
    }

    return participant.back();
}