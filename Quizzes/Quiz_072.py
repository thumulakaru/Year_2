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


a = Mac(2)
print(a.MacGen())
