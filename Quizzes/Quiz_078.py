class FireWall:
    def __init__(self, data:str):
        self.data = data
        self.ports = [80, 22123]

    def bin2dec(self):
        power = 0
        sum = 0
        for i in range(15, -1, -1):
            sum += int(self.data[i]) * (2 ** power)
            power += 1
        return sum

    def validity(self):
        num = self.bin2dec()
        error = "Filtered"
        msg = None
        if num in self.ports:
            error = "Allowed"
            msg = self.data[16:]
        return error, msg


data1 = "100111001011001110010110011100101"
data2 = "010101100110101111110111001111"


temp_class_1 = FireWall(data1)
temp_class_2 = FireWall(data2)

print(temp_class_1.validity())
print(temp_class_2.validity())