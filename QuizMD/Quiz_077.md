# Quiz 77

## Python Solution 
```.py
class PhysicalLayer:
    def __init__(self, data:str):
        self.data = data

    def checker(self):
        error = False
        num = 0
        for i in range(1, len(self.data)):
            num += int(self.data[i])

        if num % 2 != int(self.data[0]):
            error = True
        return error


temp_class1 = PhysicalLayer("100111001011001110010110011100101")
temp_class2 = PhysicalLayer("011101111101110111110111001111")

print(temp_class1.checker())
print(temp_class2.checker())
```

### Evidence
![](/Assets/Quiz_077_evidence.png)

**Fig.1:** Evidence for Quiz 77

## Paper Programming
![](/Assets/Quiz_077_papercode.jpeg)

**Fig.2:** Paper Programming for Quiz Num