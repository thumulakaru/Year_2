def net_profit(sales:list):
    min, max = sales[0], sales[0]
    for i in range(1, len(sales)):
        if sales[i] < min:
            min = sales[i]

        elif sales[i] > max:
            max = sales[i]

    return (max-min)


a =[0, 12, 122, 121, 123, 1]

print(net_profit(a))