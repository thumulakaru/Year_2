# Quiz 72

## Python Solution 
```.py
from random import randint


class Mac:
    def __init__(self, N:int):
        self.num = N
        self.all_char = "0123456789ABCDEFG"

    def MacGen(self):
        out = []
        while len(out) < self.num:
            temp = ""
            for i in range(0,6):
                for j in range(0,2):
                    temp = f"{temp}{self.all_char[randint(0, 16)]}"
                if i != 5:
                    temp += ":"
            if temp not in out:
                out.append(temp)
        return out


a = Mac(1)
print(a.MacGen())
```

## Paper Programming
![](Assets/Quiz_072_papercode.jpeg)

**Fig.1:** Paper Programming for Quiz 72