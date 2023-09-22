from Lessons.adts import queue


def sort(in_q:queue):
    y = []

    while not in_q.isEmpty():
        y.append(in_q.dequeue())

    for i in range(0, len(y)):
        for j in range(i, len(y)):
            if y[i] > y[j]:
                temp = y[i]
                y[i] = y[j]
                y[j] = temp

    for element in y:
        in_q.enqueue(element)

    return in_q.data


q = queue()
z = ["Smith, John", "Doe, Bob"]
for elem in z:
    q.enqueue(elem)
print(sort(q))