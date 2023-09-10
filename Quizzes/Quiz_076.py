class BinChecker:
    def __init__(self, data:str):
        self.data = data

    def error_checker(self):
        data = self.data
        num_chars = len(data)//3
        error = False
        s1 = ""
        for i in range(0, num_chars):
            if data[i] == data[i+num_chars] == data[i+2*num_chars]:
                s1 += data[i]
            else:
                error = True
                if data[i] == data[i+num_chars] and data [i] != data[i+2*num_chars]:
                    s1 += data[i]

                elif data[i]!= data[i+num_chars] and data[i] == data[i+2*num_chars]:
                    s1 += data[i]

                else:
                    data[i] = data[i+num_chars]
                    s1 += data[i+num_chars]

        output = s1 * 3
        return output, error


data = "011101111101110111110111001111"
a = BinChecker(data=data)
print(a.error_checker())