class CalorieCount():
    def __init__(self, daily_limit):
        self.daily_limit = daily_limit
        self.daily_intake = 0
        self.protein = 0
        self.carbs = 0
        self.fat = 0

    def addMeal(self, daily_intake, protein, carbs, fat):
        self.daily_intake += daily_intake
        self.protein += protein
        self.carbs += carbs
        self.fat += fat

    def getProteininPercantage(self):
        return round(4*self.protein/self.daily_intake, 2)

    def onTrack(self): return self.daily_intake <= self.daily_limit


sunday = CalorieCount(1500)
sunday.addMeal(716, 38, 38, 45)
sunday.addMeal(230, 16, 8, 16)
sunday.addMeal(568, 38, 50, 24)

print(sunday.onTrack())
print(sunday.getProteininPercantage())

