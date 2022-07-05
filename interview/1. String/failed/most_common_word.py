# https://leetcode.com/problems/most-common-word
# 실패!!!

from collections import defaultdict
from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]
        counts = Counter(words)
        return counts.most_common(1)[0][0]

class Solution1:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]
        counts = defaultdict(int)
        for word in words:
            counts[word] += 1
        return max(counts, key=counts.get)