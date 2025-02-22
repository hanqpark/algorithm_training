class Solution {
public:
    bool isAnagram(string s, string t) {
        map<char, int> smap;
        map<char, int> tmap;

        for (const char &ss: s)
            smap[ss]++;
        
        for (const char &tt: t)
            tmap[tt]++;
        
        return smap == tmap;
    }
};
