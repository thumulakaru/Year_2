class fourDigitNumber:
    def __init__(self, number:int):
        self.number = number
        self.thouDigit = number // 1000
        self.temp = number % 1000
        self.hundDigit = self.temp // 100
        self.temp = self.temp % 100
        self.tensDigit = self.temp // 10
        self.onesDigit = self.temp % 10

tempc = fourDigitNumber(1234)
print(tempc.thouDigit)
print(tempc.hundDigit)
print(tempc.tensDigit)
print(tempc.onesDigit)