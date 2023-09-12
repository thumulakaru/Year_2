# Quiz 75

## Python Solution 
```.py
class osi_phsyical():
    def __init__(self, input:str):
        self.unprocessed = input

    def dec2bin(self,letter):
        temp = ord(letter)
        bin = ""
        while temp != 0:
            bin = f"{temp % 2}" + bin
            temp = temp // 2
        if len(bin) != 8:
            bin = "0"*(8-len(bin))+bin
        return bin

    def get_output(self):
        out_str = ""
        for letter in self.unprocessed:
            out_str += self.dec2bin(letter) + " "
        return out_str[:-1]


temp_class = osi_phsyical("Please Do Not Throw Sausage Pizza Away")
print(temp_class.get_output())
```
### Evidence
![](/Assets/Quiz_075_evidence.png)

**Fig.1:** Evidence for Quiz 75

## Paper Programming
![](/Assets/Quiz_075_papercode.jpeg)

**Fig.2:** Paper Programming for Quiz Num