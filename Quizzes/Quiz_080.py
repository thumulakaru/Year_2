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
        for i in self.nums:
            temp += (i/len(self.nums))
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


temp_class = AverageList([1,2,3,4,5,6,7,8,9])
print(temp_class.method1())
print(temp_class.method2())
print(temp_class.method3())

