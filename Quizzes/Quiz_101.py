def cut_cake(cake:list, num_ppl:int)->list:
    length = len(cake)*len(cake[0])
    num_p_p = length//num_ppl
    remainder = length % num_ppl

    if num_p_p == 0:
        return "No cake"

    temp = [i for i in range(1, num_ppl+1) for _ in range(num_p_p)]
    temp += [0] * remainder

    for i in range(len(cake)):
        for j in range(len(cake[0])):
            cake[i][j] = temp[i * len(cake[0]) + j]

    return cake

cake = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(cut_cake(cake, 7))



