class listnode:
    def __init__(self, val: int, next = None):
        self.value = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None

    
    def get(self, index: int) -> int:
        val = -1
        if index >= 0:
            curr = 0
            currNode = self.head
            while currNode is not None and curr != index:
                curr+=1 
                currNode = currNode.next
            if currNode is not None:
                val = currNode.value
        return val

    def insertHead(self, val: int) -> None:
        newNode = listnode(val)
        if self.head is None: 
            self.head = newNode
            self.tail = self.head
        else: 
            newNode.next = self.head
            self.head = newNode
        

    def insertTail(self, val: int) -> None:
        newNode = listnode(val)
        if self.head is None:  
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
            

    def remove(self, index: int) -> bool:
        if self.head is None or index < 0:
            return False

        # remove head
        if index == 0:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return True

        currNode = self.head
        currIndex = 0

        # stop at node BEFORE the one we want to delete
        while currNode.next is not None and currIndex < index - 1:
            currNode = currNode.next
            currIndex += 1

        if currNode.next is None:
            return False

        # update tail if needed
        if currNode.next == self.tail:
            self.tail = currNode

        currNode.next = currNode.next.next
        return True


    
    def getValues(self) -> List[int]:
        vals = []
        currNode = self.head
        while currNode is not None: 
            vals.append(currNode.value)
            currNode = currNode.next
        return vals
        
