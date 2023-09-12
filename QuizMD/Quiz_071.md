# Quiz 71

## Python Solution 
```.py
from random import randint


class InternetProtocol():
    def __init__(self, num):
        self.out_list = []
        self.num_in = num

    def ipv6machine(self):
        num = self.num_in
        all_elem = "abcdefg0123456789"
        while num > len(self.out_list):
            temp = ""
            for i in range(8):
                for j in range(4):
                    a = randint(0, 16)
                    temp = f"{temp}{all_elem[a]}"
                if i != 7:
                    temp += ":"
            if temp not in self.out_list:
                self.out_list.append(temp)
        return self.out_list


a = InternetProtocol(10)
print(a.ipv6machine())

```

### Evidence
![](/Assets/Quiz_071_evidence.png)

**Fig.1:** Evidence for Quiz 71

## Paper Programming
![](/Assets/Quiz_071_papercode.jpeg)

**Fig.2:** Paper Programming for Quiz 71