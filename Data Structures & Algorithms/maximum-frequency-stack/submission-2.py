class FreqStack:

    def __init__(self):
        self.count={}
        self.maxcount=0
        self.stack={}

        

    def push(self, val: int) -> None:
        valcount=1+self.count.get(val,0)
        self.count[val]=valcount
        if valcount>self.maxcount:
            self.maxcount=valcount
            self.stack[valcount]=[]
        self.stack[valcount].append(val)

        

    def pop(self) -> int:
        res=self.stack[self.maxcount].pop()
        self.count[res]-=1
        if not self.stack[self.maxcount]:
            self.maxcount-=1
        return res

        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()