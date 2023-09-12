# Quiz 70

## Python Solution 
```.py
def ipV4machine():
    output = []
    for i in range(0,256):
        for j in range(0, 256):
            for k in range(0, 256):
                for l in range(0, 256):
                    output.append(f"{i}.{j}.{k}.{l}")

    return output
```

### Evidence
**The code is shortened for displaying the output.**
#### The modified Code
```.py
def ipV4machine():
    output = []
    for i in range(0,1):
        for j in range(0, 1):
            for k in range(0, 1):
                for l in range(0, 256):
                    output.append(f"{i}.{j}.{k}.{l}")

    return output


print(ipV4machine())
```
![](/Assets/Quiz_070_evidence.png)

**Fig.1:** Evidence for Quiz 70(The emitted code's output)

## Paper Programming
![](/Assets/Quiz_070_papercode.jpeg)

**Fig.2:** Paper Programming for Quiz 70