a, b, v = map(int, input().split())
print((v-a)//(a-b)+2 if (v-a)%(a-b) else (v-a)//(a-b)+1)
