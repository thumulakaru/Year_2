# Quiz 80

## Python Solution 
```.py
class AverageList:
    def __init__(self, A:list):
        self.nums = A

    def method1(self):
        temp = 0
        for i in self.nums:
            temp += i
        return temp / len(self.nums)

    def method2(self):
        temp = 0
        for i in self.A:
            temp += (i/len(self.A))
        return temp

    def method3(self):
        sum_even = 0
        sum_odd = 0
        for i in range(len(self.nums)):
            if i % 2 == 0:
                sum_even += self.nums[i]
            else:
                sum_odd += self.nums[i]
        return (sum_even+sum_odd)/len(self.nums)
```

### Evidence
![](/Assets/Quiz_80_evidence.png)

**Fig.1:** Evidence for Quiz 80

## Paper Programming
![](/Assets/Quiz_80_papercode.jpeg)

**Fig.2:** Paper Programming for Quiz 80