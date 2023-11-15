import random
import time

marks = [random.randint(0, 100) for i in range(10)]
levels = ["Fail", "Pass", "Credit", "Distinction"]
grades = []
start = time.time()
for m in range(0, len(marks)):
    crit = 80
    ind = 3
    while not (marks[m]//crit) and ind != 0:
        crit -= 20
        ind -= 1
    grades.append(levels[ind])

end = time.time()
print(grades)
print(f"Time taken: {end-start}")

