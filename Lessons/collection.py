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

        return item
