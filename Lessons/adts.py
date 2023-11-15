# Collection
class collection:
    def __init__(self, data:list):
        self.data = data
        self.location = 0

    def addItem(self, item):
        self.data.append(item)

    def isEmpty(self):
        return len(self.data) == 0

    def hasNext(self) -> bool:
        return self.location < len(self.data)

    def getNext(self):
        end_code = "\033[00m"
        red = "\033[0;31m"
        if self.hasNext():
            item =  self.data[self.location]
            self.location += 1

        else:
            item = f"{red}[ERROR]Collection out of index{end_code}"

    def Nuke(self):
        self.data.clear()
        self.location = 0


class queue:
    def __init__(self):
        self.data = []

    def enqueue(self, item):
        self.data.append(item)
        return

    def dequeue(self):
        item = self.data[0]
        self.data = self.data[1:len(self.data)]
        return item

    def isEmpty(self):
        return bool(len(self.data) == 0)

    def __repr__(self):
        return f"<Queue> {self.data}"


class stack:
    def __init__(self):
        self.data = []

    def push(self, item):
        self.data.append(item)
        return

    def pop(self):
        item = self.data[len(self.data)-1]
        self.data = self.data[0:len(self.data)-1]
        return item

    def isEmpty(self):
        if not self.data:
            return True
        else:
            return False

    def __repr__(self):
        return f"<Stack> {self.data}"


# Single Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

    def __repr__(self):
        out_str = f"Node[{self.data}]"
        temp = self.next
        while temp is not None:
            out_str += f" -> Node[{temp.data}]"
            temp = temp.next
        return out_str

    def addNode(self, node):
        if self.next:
            temp = self.next
            node.next = temp
            self.next = node
        else:
            self.next = node

# Binary Tree
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return f"Node[{self.data}]"

    def addNode(self, node):
        if node.data < self.data:
            if self.left:
                self.left.addNode(node)
            else:
                self.left = node
        else:
            if self.right:
                self.right.addNode(node)
            else:
                self.right = node
