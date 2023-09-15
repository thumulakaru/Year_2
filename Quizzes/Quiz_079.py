class PalindromicNumbers:
    def __init__(self, start:int, end:int):
        self.start = start
        self.end = end

    def checker(self, str_in):
        rev = ""
        for elem in str_in:
            rev = elem + rev
        if str_in == rev:
            return True
        else:
            return False

    def num_gen(self):
        out = []
        for elem in range(self.start, self.end+1):
            if self.checker(str(elem)):
                 out.append(elem)
        return out