class MyHashMap:
    
    def __init__(self):
        self.hashmap = dict()   # dictionary() 아님

    def put(self, key: int, value: int) -> None:
        self.hashmap[key] = value

    def get(self, key: int) -> int:
        try:
            return self.hashmap[key]
        except:
            return -1

    def remove(self, key: int) -> None:
        try: 
            del self.hashmap[key]            # del로 삭제하는 거임
        except:
            return -1

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)