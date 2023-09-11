# Quiz 74

## Python Solution 
```.py
class DataPackage:
    def __init__(self, Mac_rx:str, IP_rx:str, Mac_sx:str, IP_sx:str, data:str):
        self.Mac_rx = Mac_rx
        self.IP_rx = IP_rx
        self.Mac_sx = Mac_sx
        self.IP_sx = IP_sx
        self.data = data

    def build_data(self):
        out = []
        chunks = len(self.data) // 4
        leftover = len(self.data) % 4
        for i in range(chunks):
            temp_data = self.data[i*4:(i+1)*4]
            out.append(f"{self.Mac_rx}|{self.IP_rx}|{self.Mac_sx}|{self.IP_sx}|{temp_data}")
        if leftover:
            temp_data = self.data[-leftover:]
            out.append(f"{self.Mac_rx}|{self.IP_rx}|{self.Mac_sx}|{self.IP_sx}|{temp_data}")
        return out


temp_class = DataPackage("80:90:00:00:00:00","192.168.3.3","80:90:00:00:00:01","192.168.4.5","Hello World")
print(temp_class.build_data())
```

### Evidence
![](/Assets/Quiz_074_evidence.png)

**Fig.1** Evidence of completion of Quiz 74 in Python

## Paper Programming
![](/Assets/Quiz_074_papercode.jpeg)

**Fig.2:** Paper Programming for Quiz 74