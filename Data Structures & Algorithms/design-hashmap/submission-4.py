class MyHashMap:

    def __init__(self):
        self.arr = []

    def put(self, key: int, value: int) -> None:
        for i in range(len(self.arr)):
            if self.arr[i][0] == key:
                self.arr[i][1] = value
                return 
        self.arr.append([key, value])

    def get(self, key: int) -> int:
        for k in self.arr:
            if k[0] == key:
                return k[1]

        return -1

    def remove(self, key: int) -> None:
        for ele in self.arr:
            if ele[0] == key:
                self.arr.remove(ele)
                return