class LRUCache:

    def __init__(self, capacity: int):
        self.d={}
        self.c=capacity 
        self.l=0
    def get(self, key: int) -> int:
        if key in self.d:
            p=self.d.pop(key)
            self.d[key]=p
            return self.d[key]
        else :
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key not in self.d:
            if len(self.d)==self.c:
                o=list(self.d.keys())
                self.d.pop(o[0])
            self.d[key]=value
        else:
            self.d.pop(key)
            self.d[key]=value
            
            
            
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
