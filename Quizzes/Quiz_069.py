def net_profit(sales:list):
    min, max = sales[0], sales[0]
    for i in range(1, len(sales)):
        if sales[i] < min:
            min = sales[i]
        elif sales[i] > max:
            max = sales[i]

    return (max-min)


a =[100, 45, 12, 3, 56, 7]

print(f"The net profit is ¥ {net_profit(a)}.")