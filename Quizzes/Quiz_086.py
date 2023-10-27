class Pixel():
    def __init__(self, row:int, col:int, active:bool):
        self.row = row
        self.col = col
        self.active = active

    def getRow(self): return self.row

    def getCol(self): return self.col

    def __repr__(self):
        return str("■" if self.active else "□")


class Screen():
    def __init__(self, width, length):
        self.width = width
        self.length = length
        temp = []
        for i in range(width):
            row = []
            for j in range(length):
                row.append(Pixel(i, j, False))
            temp.append(row)
        self.grid = temp

    def flipPixel(self, row, col):
        self.grid[row][col].active = not self.grid[row][col].active

    def __repr__(self):
        out_str = ""
        for i in range(self.width):
            for j in range(self.length):
                out_str += str(self.grid[i][j])
            out_str += "\n"
        return out_str

test = Screen(500, 500)
print(test)