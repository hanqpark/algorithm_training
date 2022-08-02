words = list(set(input() for _ in range(int(input()))))
words.sort(key=lambda x: (len(x), x))
for word in words: print(word)