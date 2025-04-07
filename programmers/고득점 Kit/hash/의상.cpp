#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

int mySolution(vector<vector<string>> clothes) {
    unordered_map<string, vector<string>> umap;
    
    for (const auto& c: clothes) {
        umap[c[1]].push_back(c[0]);
    }
    
    int answer = 1;
    for (const auto& pair: umap) {
        answer *= pair.second.size()+1;
    }
    
    return answer-1;
}

int gptSolution(vector<vector<string>> clothes) {
    unordered_map<string, int> umap;
    
    for (const auto& c: clothes) {
        ++umap[c[1]];
    }
    
    int answer = 1;
    for (const auto& pair: umap) {
        answer *= (pair.second + 1);
    }
    
    return answer-1;
}