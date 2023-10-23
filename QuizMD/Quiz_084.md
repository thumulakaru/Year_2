# Quiz 84

## Python Solution 
```.py
class fourDigitNumber:
    def __init__(self, number:int):
        self.number = number
        self.thouDigit = number // 1000
        self.temp = number % 1000
        self.hundDigit = self.temp // 100
        self.temp = self.temp % 100
        self.tensDigit = self.temp // 10
        self.onesDigit = self.temp % 10
```

### Evidence
![](/Assets/Quiz_084_evidence.png)

**Fig.1:** Evidence for Quiz 84

## Paper Programming
![](/Assets/Quiz_084_papercode.jpeg)

**Fig.2:** Paper Programming for Quiz 84