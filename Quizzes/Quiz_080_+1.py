from Lessons.collection import collection

def sort():
    in_col = collection(["bob", "alice", "zoe"])
    a = []
    while in_col.hasNext():
        b = in_col.getNext()
        a.append(b)

    swap = True
    while swap:
        swap = False
        for i in range(len(a)-1):
            if a[i] > a[i+1]:
                swap = True
                temp = a[i]
                a[i] = a[i+1]
                a[i+1] = temp

    out_col = collection([])
    for j in range(len(a)):
        out_col.addItem(a[j])

    return out_col.data

print(sort())