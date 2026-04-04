class DynamicArray:

    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.array = [0] * capacity


    def get(self, i: int) -> int:
        return self.array[i]


    def set(self, i: int, n: int) -> None:
        self.array[i] = n


    def pushback(self, n: int) -> None:
        if self.size >= self.capacity:
            self.resize()
        self.array[self.size] = n 
        self.size = self.size + 1


    def popback(self) -> int:
        if self.size > 0:
            self.size = self.size -1
        return self.array[self.size] 

    def resize(self) -> None:
        arr = [0] * self.capacity * 2
        self.capacity = self.capacity*2
        for i in range(self.size):
            arr[i] = self.array[i]
        self.array = arr    


    def getSize(self) -> int:
        return self.size
        
    
    def getCapacity(self) -> int:
        return self.capacity
